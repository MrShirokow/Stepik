n = int(input())
dimension = n       # Размерность матрицы (чтобы не трогать n)
k_x, k_y = -1, 1    # Указание направление, куда будем двигаться по матрице
x, y = n-1, 0       # Стартовые (x, y) для заполнения матрицы после заполнения 1ой строки
element = n + 1     # число, с которого начинаем заполнять матрицу по кругу (будет изменяться в дальнейшем)

matrix = [[0 for i in range(n)] for j in range(n)]
matrix[0][:] = [x + 1 for x in range(n)]    # заполнение первой линии, дальше алгоритм сводится к циклу

while dimension != 0:
    dimension -= 1
    for step_y in range(dimension):     # по сути, можно этот и нижний цикл как отдельную функцию сделать
        y += k_y
        matrix[y][x] = element
        element += 1
    for step_x in range(dimension):
        x += k_x
        matrix[y][x] = element
        element += 1
    k_x, k_y = k_y, k_x                 # Меняем направление

for j in range(n):
    for i in range(n):
        print(matrix[j][i], end=' ')
    print()
