list_i = []
while True:
    data = input()
    if data == 'end':
        break
    list_i.append([int(i) for i in data.split()])

width = len(list_i[0])
height = len(list_i)


def neighbour_sum(x: int, y: int):
    return list_i[x - 1][y] + list_i[(x + 1) % height][y] + list_i[x][y - 1] + list_i[x][(y + 1) % width]


for i in range(height):
    for j in range(width):
        print(neighbour_sum(i, j), end=' ')
    print()
