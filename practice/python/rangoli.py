"""
You are given an integer, n. Your task is to print an alphabet rangoli of size n.
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

import string


def print_rangoli(size):
    letters = string.ascii_lowercase[0:size]
    letters = letters[::-1]
    lines = []
    width = ((size * 2) - 1) + ((size * 2) - 2)

    for index, letter in enumerate(letters):
        lines.append(letters[:index] + letter + ''.join(reversed(letters[:index])))

    lines += lines[::-1]
    lines.pop(size)

    for i in lines:
        print('-'.join(i).center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
