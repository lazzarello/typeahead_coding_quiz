# Typeahead coding quiz

## Running

1. Python > 3.6
2. `pip install -r requirements.txt`
3. `python main.py < input_1.txt > test_output_1.txt`
4. `diff output_1.txt test_output_1.txt`

## Dockerfile

Dependencies not installing or not interested in upgrading python version? Run it interactively inside a container.

1. Install docker
2. `docker build -t typeahead_quiz .`
3. `docker run --rm -it typeahead_quiz:latest /bin/bash`
4. `python main.py < input_1.txt > test_output_1.txt`
5. `diff output_1.txt test_output_1.txt`

## Results

My results are not perfect. This is caused by the library I integrated to do the matching/searching algorithms.

The first simulated input has these differences

```
# python main.py < input_1.txt > test_output_1.txt
# diff output_1.txt test_output_1.txt
8c8
< vertical_farm, vertical_farming, vertical
---
> vertical, vertical_farm, vertical_farming
26c26
< vertical_farming, vertical_farm, vapor_deficit, vertical
---
> vertical_farm, vertical_farming, vapor_deficit, vertical
```

This is a result of a convention the author used for sorting exact matches, [reported upstream](https://github.com/seperman/fast-autocomplete/issues/28).

The second simulated input has these differences

```
# python main.py < input_2.txt > test_output_2.txt
# diff output_2.txt test_output_2.txt
1c1,3
< i_love_code, i_love_machine_learning, i_love_coding, ironman, island
---
> i_love_code, i_love_machine_learning, island, ironman, i_love_coding
> ironman
> ironman
11,13c13
< 
< 
< i_love_code, i_love_machine_learning, i_love_coding, ironman, island, iron_maiden
---
> i_love_code, i_love_machine_learning, island, ironman, i_love_coding, iron_maiden
```

The first and last differences are the result of the library author sorting alphabetically in decending order. I chose not to modify the library though I agree this is a bit counter-intuitive. Probably worth my time to submit a PR.

The middle difference kind of looks like a bug, which I have [reported upstream](https://github.com/seperman/fast-autocomplete/issues/37) though the lib also uses a [library](https://github.com/ztane/python-Levenshtein) with a string similarity algorithm, which I don't fully understand. That might also influence the extra two matches after the underscore input character.

## Feedback

I'll discuss more in person but worth noting here, my skills do not lie in writing code all day, which you can probably see from my results. I'm aware of OOP in Python though it's not a methodology I intuitively use from memory. I could very likely get these same results by refactoring this to be OO, as indicated in the comments.

I included a git commit history and some time tracking through a little pomodoro script I like. You can see I spent more time then the suggested 60 to 90 minutes to arrive at these results.

I believe this is a good demonstration of how I approch real-world computer programming problems. I have also formatted the file using the defaults from the `black` python code formatter and vim plugins for python.
