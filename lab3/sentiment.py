#!/usr.bin.env python3

import re

dictionary = {}
output_string = []


def load_score_dict(text_file = 'sentiment.txt'):
    global dictionary
    with open(text_file) as open_text:
        for line in open_text:
            if line[0] != '#' and line[0] != '\n':
                key, value = line.split()
                dictionary[key] = float(value)
        return dictionary


def get_words(string_input):
    global output_string
    remove_punctuation_string = re.sub(r'[^\w\s]', '', string_input)
# how to use re in python ^^^
# https://datagy.io/python-remove-punctuation-from-string/
    lower_case_string = remove_punctuation_string.lower()
    new_string = lower_case_string.split()
    output_string = sorted(set(new_string), key=lambda x: new_string.index(x))
    return output_string


def score_sentence(string_input, dictionary_input):
    global output_string
    global dictionary
    get_words(string_input)
    load_score_dict(dictionary_input)
    total = 0
    for word in output_string:
        if word not in dictionary:
            output_string.remove(word)
            total += dictionary[word]
    return total, print(total)


def open_string_file(txt_file):
    file = open(txt_file)
    import_string = file.read().replace('\n',' ')
    file.close()
    return import_string
