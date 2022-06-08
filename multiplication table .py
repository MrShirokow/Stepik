# таблица умножения чисел от 'a' до 'b' на числа от 'c' до 'd'

a, b, c, d = (int(input()) for _ in range(4))

print('\t', end='')
for x in range(c, d + 1):
    print(x, end='\t')
    x += 1
print()

i, j = a, c

while i <= b:
    print(i, end='\t')
    while j <= d:
        print(i * j, end='\t')
        j += 1
    print()
    j = c
    i += 1
