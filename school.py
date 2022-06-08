classes: dict = {k + 1: [0, 0] for k in range(11)}

with open('school.txt', 'r', encoding='utf-8') as f:
    class_info: list = [line.strip().split('\t') for line in f.readlines()]

for cl in class_info:
    class_number, name, height = int(cl[0]), cl[1], int(cl[2])
    classes[class_number][0] += height
    classes[class_number][1] += 1

for key, heights in classes.items():
    average_height = heights[0] / heights[1] if  heights[1] else '-'
    print(f'{key} {average_height}')
