# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
strings = []
even = ''
odd = ''
for _ in range(n):
    strings.extend(input().split())

for elements in strings:
    for index, word in enumerate(elements):
        if index % 2 == 0:
            even += word
        else:
            odd += word
    print(''.join(even + ' ' + odd))
    even, odd = '', ''
