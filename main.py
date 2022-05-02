import sys
from fast_autocomplete import AutoComplete,autocomplete_factory

# globals,
# could be instance variables but my intuition is not OOP, so I started like this
i_terminator = '#'
i_file_contents = ""
phrase_freq = {}
space_replacement = '_'
split_character = ','
# we don't know the values of these until we call the functions
dict_offset = 0
input_offset = 0
words = {}

# get standard input. ez pz.
for line in sys.stdin:
    i_file_contents += line

# splitlines into a list, but this can totally be done up there ^^
i_splitlines = i_file_contents.splitlines()

def get_words(i):
    # lulz, scope. check commit history for me being dumb.
    global dict_offset
    # convention in the rules says the first line is a data offset this lines + 1 long
    dict_offset = int(i[0]) + 1
    return i[1:dict_offset]

def get_inputs(i):
    global input_offset
    # convention in the rules says dict_offset + 1 is a data offset for user input
    input_offset = int(i[dict_offset])
    return i[dict_offset+1:]

def format_words(i):
    # get previously input words
    i_w = get_words(i)
    for i in i_w:
        # split into [phrase, count] then format words dict for our DWG library
        w = i.split(split_character)
        # TODO debug this (is this the tie-breaker trick question in the instructions?)
        # why is the 7th result sorted backwards in example output 1?
        # why is the result in example output 2 just like, wrong?
        
        # pass in count to word dict for autocomplete lib to use for sorting later
        words[w[0]] = {'count': w[1]}
    # this is a bit weird, scope wise. TODO try adding global words to function
    return words

def load_autocomplete(words):
    # pass previously input words dict into autocomplet lib
    return AutoComplete(words=words)

def flatten_list(i):
    # totally unreadable but does what the name says
    return [item for sublist in i for item in sublist]

def join_list_of_strings(l):
    # use formatting convention to match example output files
    return ', '.join(l)

def write_file_from_string(filename, i_string):
    # write an input string to filename
    f = open(filename, "w")
    f.write(i_string)
    f.close()

def output(i):
    # locals for later
    search_string = ''
    output_string = ''
    # fill up the dict of previously input words
    words = format_words(i)
    # load up autocomplete with the dict
    autocomplete = load_autocomplete(words)
    # get a list of our simulated user input
    search_input = get_inputs(i)
    # loop through simulated user input as if typing characters, reset on i_terminator character
    for c in search_input:
        if(c == i_terminator):
            search_string = ''
            output_string += '\n'
        else:
            # keep stackin' chars into search input
            search_string += c
            # call autocomplete lib search,
            # autocomplete lib returns a list of lists of characters, flatten into a single list,
            list_output = flatten_list(autocomplete.search(word=search_string))
            # join the list in each line to match our example output
            output_string += f'{join_list_of_strings(list_output)}\n'
    return output_string

def main():
    # call the output function with splitlines as input
    o = output(i_splitlines)
    # does print count as stdout? I think so.
    print(words)
    print(o)
    # write_file_from_string('test_output_1.txt', o)

# push the old stuff into a class so I can read this file better
class NoLibraryVersion():
    def __init__(self):
        self.foo = 0

    def get_num_phrases(self, i):
        # return the first line of the input and stop
        i_num_phrases = i[0]
        return i_num_phrases

    def get_frequencies(self, i):
        # input is a string seperated by a comma, one line at a time
        # return a dict with form { 'phrase' : frequency }
        split_input = input.split(',')
        phrase_freq[split_input[0]] = split_input[1] 
        return phrase_freq

    def simulated_input_characters(self, i):
        # count i_num_phrases + 1 offset from input
        # i_num_characers is the next line
        # read i_num_characters into a string
        # split the string on i_terminator character
        inputs = i.split(i_terminator)

    # not really necessary but nice
    def replace_underscore_to_space(self, phrase):
        return phrase.replace(space_replacement, ' ')

if __name__ == "__main__":
    main()
