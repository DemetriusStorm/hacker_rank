"""
An integer N such that N <= 50.
This is followed by N lines such that each the text in each line is either an IPv4 address or an IPv6 address,
or a chunk of text which does not equal either of these.
There will be no extra text or whitespace leading or trailing the IP address in a line (if it is an IP address).
The number of characters in each line will not exceed 500.
"""

import re


def is_ipv4(sequence):
    return re.search(r'^((1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$', sequence)


def is_ipv6(sequence):
    return re.search(r'^([\da-f]{1,4}:){7}[\da-f]{1,4}$', sequence)


# # second variant without regex expression
# for x in range(1, int(input("How many tests? ")) + 1):
#     string = input("Check: ")
#     try:
#         str_ipv4 = string.split(".")
#         str_ipv6 = string.split(":")
#         if len(str_ipv4) == 4 and all(0 <= int(n) <= 255 for n in str_ipv4):
#             print("IPv4")
#         elif len(str_ipv6) == 8 and all(0 <= int(n, 16) <= 65535 for n in str_ipv6):
#             print("IPv6")
#         else:
#             print("Neither")
#
#     except ValueError:
#         print("Neither")

if __name__ == '__main__':
    count_of_seq = int(input())
    list_of_seq = [input() for _ in range(count_of_seq)]
    for seq in list_of_seq:
        if is_ipv4(seq):
            print('IPv4')
        elif is_ipv6(seq):
            print('IPv6')
        else:
            print('Neither')
