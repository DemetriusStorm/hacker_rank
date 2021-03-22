"""
Charlie has been given an assignment by his Professor to strip the links and the text name from the html pages.
"""

import re

for _ in range(int(input())):
    html_link_match = re.findall(r'<a href="([^"]+)[^>]*>(?:<[^>]+>)*([^<]*)', input())
    for html, title in html_link_match:
        print('{0},{1}'.format(html, title))
