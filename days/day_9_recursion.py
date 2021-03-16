"""
Complete the factorial function in the editor below. Be sure to use recursion.
factorial has the following paramter:
int n: an integer
"""

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)
