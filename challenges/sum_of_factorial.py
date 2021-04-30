# Complete the factorial function below.
def f(n):
    if n == 1:
        return 1
    # print(n)
    return n * f(n - 1)


def sf(num):
    sum_of_factorial = 0
    for n in str(num):
        sum_of_factorial += f(int(n))
    return sum_of_factorial


def sd(num):
    sum_of_digits = 0
    for n in str(num):
        sum_of_digits += int(n)
    return sum_of_digits


if __name__ == '__main__':
    n = int(input())
    print(sd(sf(n)))
    print(sf(5))
    print(f(5))
