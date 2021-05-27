"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name
on a new line.
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""

if __name__ == '__main__':
    journal_scores = {'Harry': 37.21,
                      'Berry': 37.21,
                      'Tina': 37.2,
                      'Akriti': 41,
                      'Harsh': 39,
                      'Trash': 37.2,
                      'Clash': 37.2,
                      'Slash': 37.21,
                      'Clisnash': 37.21,
                      'Smash': 37.21,
                      }
    sorted_journal = {k: v for k, v in sorted(journal_scores.items(), key=lambda x: x[1], reverse=True)}
    list_of_names = []
    counter = 0
    minimum = min(sorted_journal.values())

    while sorted_journal:
        name, score = sorted_journal.popitem()
        if score == minimum:
            if counter == 0:
                continue
            elif counter == 1:
                list_of_names.append(name)
                minimum = score
        elif score > minimum:
            if counter == 2:
                break
            elif counter == 0:
                list_of_names.append(name)
                minimum = score
                counter += 1

    print('\n'.join(sorted(list_of_names)))
