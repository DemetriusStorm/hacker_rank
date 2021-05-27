"""
We define a word as a non-empty maximum sequence of characters that can contain only lowercase letters,
uppercase letters, digits and underscores '_' (ASCII value 95).
Maximum sequence means that the word has to be immediately preceeded by a character not allowed to occur in a word
or by the left boundary of the sentence, and it has to be immediately followed by a character not allowed to occur
in a word or by the right boundary of the sentence.
"""
import re

if __name__ == '__main__':
    count_of_sentence = int(input())
    sequence = '\n'.join(input() for _ in range(count_of_sentence))
    count_of_words = int(input())
    pattern = r'\b{0}\b'
    for _ in range(count_of_words):
        print(len(re.findall(pattern.format(input().strip()), sequence)))
