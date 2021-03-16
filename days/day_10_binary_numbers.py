"""
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
When working with different bases, it is common to show the base as a subscript.

Example
n = 125
The binary representation of 125(base=10) is 1111101(base=2).
In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary = '{0:b}'.format(n)
    print(binary)
    pattern = re.compile(r'[1]+')
    matches = pattern.findall(binary)
    print(matches)
    print(len(max(matches)))
