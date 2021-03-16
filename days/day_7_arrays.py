"""
Print the elements of array A in reverse order as a single line of space-separated numbers.
"""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(' '.join([str(num) for num in arr][::-1]))
