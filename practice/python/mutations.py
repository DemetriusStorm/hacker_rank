"""
Read a given string, change the character at a given index and then print the modified string.
"""


def mutate_string(string, position, character):
    return '{before}{char}{after}'.format(
        before=string[:position],
        char=character,
        after=string[position + 1:],
    )


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    print(mutate_string(s, int(i), c))
