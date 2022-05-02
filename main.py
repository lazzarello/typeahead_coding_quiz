import sys

i_terminator = '#'
i_file_contents = ""
i_num_phrases = 0
i_num_characters = 0
phrase_freq = {}
space_replacement = '_'

for line in sys.stdin:
    i_file_contents += line

# splitlines into a list, but this can totally be done up there ^^
i_splitlines = i_file_contents.splitlines()

def get_num_phrases(input):
    # return the first line of the input and stop
    for line in input:
        i_num_phrases = input
        # funny hack
        break
    return i_num_phrases

def get_frequencies(input):
    # input is a string seperated by a comma, one line at a time
    # return a dict with form { 'phrase' : frequency }
    split_input = input.split(',')
    phrase_freq[split_input[0]] = split_input[1] 
    return phrase_freq

def simulated_input_characters(input):
    # count i_num_phrases + 1 offset from input
    # i_num_characers is the next line
    # read i_num_characters into a string
    # split the string on i_terminator character
    inputs = input.split(i_terminator)

# not really necessary but nice
def replace_underscore_to_space(phrase):
    return phrase.replace(space_replacement, ' ')

def output(input):
    # output should be i_num_characters lines long with a blank line for each occurance of i_terminator
    return input

def main():
    print(output(i_splitlines))

if __name__ == "__main__":
    main()
