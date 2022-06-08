def search_mark(m1, m2, m3, mark_sum):
    mark_sum[0] += float(m1)
    mark_sum[1] += float(m2)
    mark_sum[2] += float(m3)
    return (float(m1) + float(m2) + float(m3)) / 3


with open('students.txt', "r", encoding='utf-8') as f:              # Сначала выводим среднюю оценку из трех дисциплин
    students = [line.strip().split(';') for line in f.readlines()]  # для каждого студента, последней строкой -
    count = len(students)                                           # среднюю оценку за каждый предмет среди всех
    result = [0, 0, 0]
    for student in students:
        print(search_mark(student[1], student[2], student[3], result))

print(result[0] / count, result[1] / count, result[2] / count)
