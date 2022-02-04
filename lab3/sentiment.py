#!/usr.bin.env python3

import re


txt_dictionary = {}
output_string = []


def load_score_dict(text_file = 'sentiment.txt'):
    global txt_dictionary
    with open(text_file) as open_text:
        for line in open_text:
            if line[0] != '#' and line[0] != '\n':
                key, value = line.split()
                txt_dictionary[key] = float(value)
        return txt_dictionary


"""
Test section for load_score_dict() func
    load_score_dict()
    load_score_dict('test_neutral.txt')
    load_score_dict('test_negative.txt')
    load_score_dict('test_positive.txt')
"""

def get_words(string_input):
    global output_string
    remove_punctuation_string = re.sub(r'[^\w\s]', '', string_input)
# how to use re in python ^^^
# https://datagy.io/python-remove-punctuation-from-string/
    lower_case_string = remove_punctuation_string.lower()
    new_string = lower_case_string.split()
    output_string = sorted(set(new_string), key=lambda x: new_string.index(x))
    return output_string


def score_sentence(string_input, dictionary_input = 'sentiment.txt'):
    global output_string
    global txt_dictionary
    get_words(string_input)
    load_score_dict(dictionary_input)
    total = 0
    for word in output_string:
        if word not in txt_dictionary:
            output_string.remove(word)
            total += txt_dictionary[word]
    return total, print(total)


"""
#my_sentence = "Grocery list:    3 boxes Land-o-lakes butter, Aunt Jemima's butter pancake mix"
my_sentence = 'welcome, welcome to my house!'
get_words(my_sentence)
scores = {'welcome': 0.5,  'house': -0.25}
score_sentence('welcome, welcome house!', scores)
#inal_score = score_sentence(my_sentence, scores)
"""

def open_string_file(txt_file):
    file = open(txt_file)
    import_string = file.read().replace('\n',' ')
    file.close()
    return import_string
