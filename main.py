import sys
import string

# Lean on a fancy lib for search algorithm,
# which is TOO FANCY to output the exact results in the examples
# https://pypi.org/project/fast-autocomplete/
from fast_autocomplete import AutoComplete, autocomplete_factory


# globals,
# could be instance/class variables but my intuition is not OOP, so I started like this
dict_offset = 0
input_offset = 0
words = {}
# Use private convention even though we're not OO right now.
_split_character = ","
_i_file_contents = ""
_i_terminator = "#"
_num_results = 10
_valid_chars = "_" + string.ascii_lowercase
# prolly don't need these ever
phrase_freq = {}
space_replacement = "_"

# get standard input. ez pz.
for line in sys.stdin:
    _i_file_contents += line

# splitlines into a list, but this can totally be done up there ^^
i_splitlines = _i_file_contents.splitlines()


def get_words(i):
    global dict_offset
    # convention in the rules says the first line is a data offset this num lines + 1 long
    dict_offset = int(i[0]) + 1
    return i[1:dict_offset]


def get_inputs(i):
    global input_offset
    # convention in the rules says dict_offset + 1 is a data offset for user input
    input_offset = int(i[dict_offset])
    return i[dict_offset + 1 :]


def format_words(i):
    # get previously input words
    global words
    i_w = get_words(i)
    for i in i_w:
        # split into [phrase, count] then format words dict for our autocomplete lib
        w = i.split(_split_character)
        # The fast-autocomplete lib picks alphabetical order ascending as tie-breaker.
        # The instructions say: "To break ties, use the alphabetical ordering of the phrases."
        # The example output used different convention to define sorting alphabetically.
        # TODO modify the library to filp the alphabetical to sort asc, not desc,

        # Q: why is the 8th result always sorted backwards using example input 1?
        # A: fast-autocomplete lib prefers an exact match for sorting above frequency,
        #    so 'vertical' will always sort 'vertical' first regardless of count.
        #    issue reported in library https://github.com/seperman/fast-autocomplete/issues/28

        # pass in count to word dict for autocomplete lib to use for sorting later
        words[w[0]] = {"count": int(w[1])}
    return words


def load_autocomplete(words):
    # Q: why is the result in example output 2 just like, wrong?
    # A: fast-autocomplete lib is matching 'iron_' to ironman, and a few others.
    #    The default is only alphbetical ASCII. This should be fixed with the
    #    valid_chars_for_string parameter but in practice it doesn't do what
    #    I expect. Issue reported, might take a swing at it.
    #    https://github.com/seperman/fast-autocomplete/issues/37
    # print(f'Valid Characers: {_valid_chars}')
    return AutoComplete(words=words, synonyms={}, valid_chars_for_string=_valid_chars)


def flatten_list(i):
    # totally unreadable but does what the name says
    return [item for sublist in i for item in sublist]


def join_list_of_strings(l):
    # use formatting convention to match example output files
    return ", ".join(l)


def write_file_from_string(filename, i_string):
    # write an input string to filename
    f = open(filename, "w")
    f.write(i_string)
    f.close()


def output(i):
    # locals for later
    search_string = ""
    output_string = ""
    # fill up the dict of previously input words
    words = format_words(i)
    # load up autocomplete with the historical dict
    autocomplete = load_autocomplete(words)
    # get a list of our simulated user input
    search_input = get_inputs(i)
    # print(f'Previous Words and Frequency: {words}')
    # print(f'Search inputs" {search_input}')
    # loop through simulated user input as if typing characters, reset on _i_terminator character
    for c in search_input:
        if c == _i_terminator:
            # Effective Python page 68 "Prefer get Over in..."
            if words.get(search_string) is None:
                words[search_string] = {"count": 1}
                autocomplete = load_autocomplete(words)
            else:
                words[search_string]["count"] += 1
                autocomplete.update_count_of_word(
                    word=search_string, count=words[search_string]["count"]
                )
            # print(f'Previous Words and Frequency: {words}')
            # reset search input
            search_string = ""
            output_string += "\n"
        else:
            # keep stackin' chars into search input
            search_string += c
            # call autocomplete lib search,
            # autocomplete lib returns a list of lists of characters, flatten into a single list,
            list_output = flatten_list(
                autocomplete.search(word=search_string, max_cost=1, size=_num_results)
            )
            # join the list in each line to match our example output
            # output_string += f"Search Input '{search_string}' : {join_list_of_strings(list_output)}\n"
            output_string += f"{join_list_of_strings(list_output)}\n"
    return output_string[: output_string.rfind("\n")]


def main():
    # call the output function with splitlines as input
    o = output(i_splitlines)
    # does print count as stdout? I think so.
    print(o)
    # write_file_from_string('test_output_1.txt', o)


# push the old stuff into a class so I can read this file better.
# I started this way and quickly leaned on a library after looking for
# some prior art. Check fast-autocomplete branch history.
class NoLibraryVersion:
    def __init__(self):
        self.foo = 0

    def get_num_phrases(self, i):
        # return the first line of the input and stop
        i_num_phrases = i[0]
        return i_num_phrases

    def get_frequencies(self, i):
        # input is a string seperated by a comma, one line at a time
        # return a dict with form { 'phrase' : frequency }
        split_input = input.split(",")
        phrase_freq[split_input[0]] = split_input[1]
        return phrase_freq

    def simulated_input_characters(self, i):
        # count i_num_phrases + 1 offset from input
        # i_num_characers is the next line
        # read i_num_characters into a string
        # split the string on _i_terminator character
        inputs = i.split(_i_terminator)

    # not really necessary but nice
    def replace_underscore_to_space(self, phrase):
        return phrase.replace(space_replacement, " ")


if __name__ == "__main__":
    main()
