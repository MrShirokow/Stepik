import math

pi = 3.14


def geron(x: int, y: int, z: int) -> float:
    p = (x + y + z) / 2
    return math.sqrt(p * (p - x) * (p - y) * (p - z))


formulas = {
    "круг": (1, lambda x: pi * x ** 2),
    "прямоугольник": (2, lambda x, y: x * y),
    "треугольник": (3, lambda x, y, z: geron(x, y, z))
}

figure = input()
i = 0
if figure in formulas.keys():
    i = formulas[figure][0]

if i == 1:
    r = int(input())
    print(formulas[figure][1](r))
elif i == 2:
    a, b = (int(input()) for _ in range(2))
    print(formulas[figure][1](a, b))
elif i == 3:
    a, b, c = (int(input()) for _ in range(3))
    print(formulas[figure][1](a, b, c))
else:
    print("Try again bob")
