"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
"""


# Complete the solve function below.
def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))


if __name__ == '__main__':
    # s = input()
    print(solve('chris alan'))
    print(solve('123 avb'))
