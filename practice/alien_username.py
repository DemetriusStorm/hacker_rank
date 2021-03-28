"""
In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:

It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
The first character must be immediately followed by one or more digits in the range 0 through 9.
After some number of digits, there must be 0 or more English letters (uppercase and/or lowercase).
It may be terminated with an optional _ (ASCII value 95). Note that if it's not terminated with an underscore,
then there should be no characters after the sequence of 0 or more English letters.
"""

import re

if __name__ == '__main__':
    count_of_names = int(input())
    alien_names = [input() for _ in range(count_of_names)]
    pattern = r'^(_|.)\d+(([a-zA-Z]+)_|0)(?<!\d)$'
    for name in alien_names:
        print('VALID' if re.search(pattern, name) else 'INVALID')
