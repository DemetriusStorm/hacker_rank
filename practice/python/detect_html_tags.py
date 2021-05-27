"""
In this challenge, we're using regular expressions to detect the various tags used in an HTML document.
"""

import re

result = set()
for _ in range(int(input())):
    pattern = re.findall(r'((?<=<)[a-z]+)|(?<=/)[a-z](?=>)', input())
    result.update(filter(None, pattern))

print(';'.join(sorted(result)))
