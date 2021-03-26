"""
Find A Sub-Word.
"""

import re

if __name__ == '__main__':
    count_of_sentence = int(input())
    sequence = '\n'.join(input() for _ in range(count_of_sentence))
    count_of_subs = int(input())
    pattern = r'(?<=\w){0}(?=\w)'
    for _ in range(count_of_subs):
        print(len(re.findall(pattern.format(input().strip()), sequence)))
