"""
Given an integer, n, print its first 10 multiples. Each multiple n * i (where 1<=i<=10) should be printed on a new line
in the form: n x i = result.
"""

if __name__ == '__main__':
    n = int(input())
    for num in range(1, 11):
        print('{} x {} = {}'.format(n, num, n * num))
        # print(f'{n} x {num} = {n * num}')
