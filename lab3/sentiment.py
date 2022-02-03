#!/usr.bin.env python

import re

txt_dictionary = {}

def load_score_dict(text_file = 'sentiment.txt') :
    global txt_dictionary
    with open(text_file) as open_text:
        for line in open_text:
            key, value = line.split()
            txt_dictionary[key] = float(value)
        return txt_dictionary, print(txt_dictionary)


"""
Test section for load_score_dict() func
    load_score_dict()
    load_score_dict('test_neutral.txt')
    load_score_dict('test_negative.txt')
    load_score_dict('test_positive.txt')
"""

def get_words(string_input) :
    remove_punctuation_string = re.sub(r'[^\w\s]', '', string_input)
        # how to use re in python ^^^
        # https://datagy.io/python-remove-punctuation-from-string/
    lower_case_string = remove_punctuation_string.lower()
    output_string = lower_case_string.split()

    return output_string, print(output_string)


# my_sentence = "Grocery list:    3 boxes Land-o-lakes butter, Aunt Jemima's butter pancake mix"
# get_words(my_sentence)

load_score_dict('test.txt')
