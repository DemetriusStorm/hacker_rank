"""
On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise,
print the full NAME and Phone Number in the format name=phoneNumber.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    name_numbers = [input().split() for _ in range(n)]
    phone_book = {k: v for k, v in name_numbers}
    while True:
        try:
            name = input()
            if name in phone_book:
                print('{}={}'.format(name, phone_book[name]))
            else:
                print('Not found')
        except EOFError:
            break
