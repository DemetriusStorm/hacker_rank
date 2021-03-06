"""
Given an integer, n, print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n.
Each value should be space-padded to match the width of the binary value of n.
"""


def print_formatted(number):
    for i in range(1, number + 1):
        width = number.bit_length()
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
