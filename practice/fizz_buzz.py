"""
Complete the 'fizzBuzz' function below.
The function accepts INTEGER n as parameter.
"""


def fizz_buzz(n):
    # Write your code here
    n_range = [num for num in range(1, n + 1)]
    for num in n_range:
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0 and num % 5 != 0:
            print('Fizz')
        elif num % 5 == 0 and num % 3 != 0:
            print('Buzz')
        else:
            print(num)


if __name__ == '__main__':
    n = int(input().strip())
    # print(n)
    fizz_buzz(n)
