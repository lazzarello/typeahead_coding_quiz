import sys
from fast_autocomplete import AutoComplete,autocomplete_factory

i_terminator = '#'
i_file_contents = ""
phrase_freq = {}
space_replacement = '_'
split_character = ','
# we don't know the values of these until we call the functions
dict_offset = 0
input_offset = 0
words = {}

for line in sys.stdin:
    i_file_contents += line

# splitlines into a list, but this can totally be done up there ^^
i_splitlines = i_file_contents.splitlines()

def get_words(i):
    # lulz, scope.
    global dict_offset
    dict_offset = int(i[0]) + 1
    # dict_offset = last
    return i[1:dict_offset]

def get_inputs(i):
    global input_offset
    input_offset = int(i[dict_offset])
    # print(dict_offset)
    return i[dict_offset+1:]

def format_words(i):
    i_w = get_words(i)
    for i in i_w:
        w = i.split(split_character)
        words[w[0]] = {}
    return words
    
def load_autocomplete(words):
    return AutoComplete(words=words)

def search_autocomplete(i):
    inputs = get_inputs(i)
    return inputs

def flatten_list(i):
    return 'list comprehensions are cool'

def output(i):
    words = format_words(i)
    autocomplete = load_autocomplete(words)
    # print(search_autocomplete(i))
    search_input = search_autocomplete(i)
    w = ''
    for c in search_input:
        if(c == i_terminator):
            w = ''
            print(w)
        else:
            w += c
            # This doesn't produce the expected output to match output_2 but it matches output_1.
            # Investigate the trick question part of input_2.
            print(autocomplete.search(word=w))
    return search_input

def main():
    output(i_splitlines)

# push the old stuff into a class so I can read better
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
