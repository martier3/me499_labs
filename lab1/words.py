#!/usr/bin/env python

# Write a function called letter_count(word, letter) in a file words.py that
# takes two string arguments. The first string is a bunch of text, and the
# second is a letter. The function returns the number of occurrences of the
# letter in the text.


def letter_count(word, letter):
    word_input = word.lower()
    letter_input = letter.lower()
    total_occurrences = word_input.count(letter_input)
    return total_occurrences


letter_count('helloworld', 'l')
