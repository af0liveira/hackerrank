"""
Given the names and grades for each student in a class of  students, store
them in a nested list and print the name(s) of any student(s) having the
second lowest grade.

Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    sorted_unique_scores = sorted(set([s for n, s in records]))
    second_lowest_score = sorted_unique_scores[1]
    selected_names = sorted([n for n, s in records
                             if abs(second_lowest_score - s) < 1e-6])
    for name in selected_names:
        print(name)
