#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    result_sentence = []
    new_sentence = sentence.split()[::-1]
    tempo = []
    for word in new_sentence:
        for char in word:
            if char.isupper():
                tempo.append(char.lower())
            else:
                tempo.append(char.upper())
        result_sentence.append(tempo)
        tempo = []

    return ' '.join(''.join(word) for word in result_sentence)


print(reverse_words_order_and_swap_cases('aWESOME is cODING'))

