# Unfold coding quiz

A typeahead search autocomplete system using text files as input. There is a frequency for each phrase (not word?). Input is terminated with a `#` character. For the purpose of this
assignment, you will be running your code with input files, passed on stdin.

There is a [python library that suggests](https://pypi.org/project/fast-autocomplete/) it could "just work".

## Problem Groups

1. User Input From Special File [x]
2. Processing
  1. Search Algorithm
    1. Acquire number of phrases
    1. [Trie](https://pypi.org/project/PyTrie/)
    2. [Fast Autocomplete](https://pypi.org/project/fast-autocomplete/) (DWG)
    3. Something else based on input file conventions
  3. Result Ranking
    1. Acquire frequency
    1. Fast Autocomplete does this as an example
3. Caching (optional)
  1. Cache type
4. Output [ ]
5. Test Cases
6. Performance Optimization (optional)

## Study Subjects

This is a common corporate interview quiz, which likely originated circa 2004/5 when Google debuted the typeahead feature of their search homepage we all know and love. It appears that the input file format is designed to prevent drop-in library usage and also to define predictable results.

There are many examples of solutions found online through StackOverflow, [corporate blogs](https://medium.com/double-pointer/system-design-interview-autocomplete-type-ahead-system-for-a-search-box-1ac968f9f121) and [for-profit educational websites](https://www.educative.io/courses/grokking-the-system-design-interview/mE2XkgGRnmp#1.-What-is-Typeahead-Suggestion?). There are some attempts at providing this functionality in language-specific libraries. [Zepworks, for example](https://pypi.org/project/fast-autocomplete/) includes sorting order through a count context. That might be fun to start with.

This exercise specifically requests I/O to be done with stdin and stdout, so we're not concerned with a GUI text box or a web app backing service. I suspect most implementations for web frond ends will be exclusively JavaScript.

It seems that the input file format is a portion of the challenge as it requires reading, splitting lines, splitting strings, counting from an offset based on a parameter from the list and interpreting special input characters.
