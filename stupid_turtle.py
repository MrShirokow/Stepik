coordinates: dict = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
n: int = int(input())

for i in range(n):
    info = input().split()
    coordinates[info[0]] += int(info[1])

print(f'{coordinates["восток"] - coordinates["запад"]} {coordinates["север"] - coordinates["юг"]}')
