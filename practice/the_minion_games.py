"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""

string = input()

vowels = ('A', 'E', 'I', 'O', 'U')
first_player = 0
second_player = 0
for i in range(len(string)):
    if string[i] in vowels:
        first_player += len(string) - i
    else:
        second_player += len(string) - i

if first_player > second_player:
    print('Kevin {0}'.format(first_player))
elif first_player < second_player:
    print('Stuart {0}'.format(second_player))
else:
    print('Draw')
