"""
Find A Sub-Word.
"""

import re

if __name__ == '__main__':
    num_of_sentence = int(input())
    sequence = '\n'.join(input() for _ in range(num_of_sentence))
    num_of_subs = int(input())
    for _ in range(num_of_subs):
        print(len(re.findall(r'(?<=\w){0}(?=\w)'.format(input().strip()), sequence)))
