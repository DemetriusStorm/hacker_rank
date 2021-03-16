"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name
on a new line.
"""

if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])
        print(result)

    counter = 0
    for scores in sorted(result):
        name, score = scores
        print(name, score)
        counter = score

