"""
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
"""
import re


def count_substring(string, sub_string):
    pattern = r'(?={0})'.format(sub_string)
    return len(re.findall(pattern, string))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
