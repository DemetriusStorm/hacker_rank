#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import defaultdict


def plusMinus(arr):
    # Write your code here
    length = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    result = []
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeros += 1
    result.append(positive / length)
    result.append(negative / length)
    result.append(zeros / length)

    return [print(f'{num:.6f}') for num in result]


def plusMinus_ver2(array):
    result = defaultdict(int)
    for num in array:
        if num > 0:
            result['positive'] += 1
        elif num < 0:
            result['negative'] += 1
        else:
            result['zeros'] += 1

    return list(map(
        lambda x: print(f'{(x / len(array)):.6f}'), result.values()
    ))


plusMinus_ver2([-4, 0, 1, -6, 8, 9])

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
