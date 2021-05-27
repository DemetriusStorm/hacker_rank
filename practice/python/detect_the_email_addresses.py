"""
You will be provided with a block of text, spanning not more than hundred lines.
Your task is to find the unique e-mail addresses present in the text.
You could use Regular Expressions to simplify your task.
And remember that the "@" sign can be used for a variety of purposes! Requirements are simplified versus real world.
There can be a number of strings separated by dots before and after the "@" symbol.
Strings will be made up of characters in the ranges a-z, A-Z, 0-9, _ (underscore).
"""

import re

if __name__ == '__main__':
    string = ''

    for _ in range(int(input())):
        string += '{0}\n'.format(input())

    pattern = r'[\w.]+@[\w.]+\w+'
    print(';'.join(sorted(set(re.findall(pattern, string)))))
