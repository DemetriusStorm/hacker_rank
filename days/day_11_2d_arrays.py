"""
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
The hourglass with the maximum sum (19) is:
2 4 4
  2
1 2 4
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
