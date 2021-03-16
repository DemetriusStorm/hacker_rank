"""
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.
"""


def wrap2(string, max_width):
    new_list = []
    while string:
        max_width_block = string[:max_width]
        string = string[max_width::]
        new_list.append(max_width_block)

    return '\n'.join(new_list)


def wrap(string, max_width):
    return '\n'.join([string[i:i + max_width] for i in range(0, len(string), max_width)])


if __name__ == '__main__':
    # string, max_width = input(), int(input())
    print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))
