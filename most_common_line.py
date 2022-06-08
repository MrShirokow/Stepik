result = {}
max_count = 1
max_key = ''        # переменная для хранения ключа, по которому лежит самое частое слово

with open('data.txt') as f:
    data = f.read()
    words = sorted(data.replace('\n', ' ').split())     # Сортировка, т.к. нужно лексикографически первое
    for word in words:                                  # Поиск самого частого слова
        key = word.lower()
        if key in result:
            result[key][0] += 1
            result[key][1].append(word)
            if result[key][0] > max_count:
                max_key = key
                max_count = result[key][0]
        else:
            result[key] = [1, [word]]


print('{} {}'.format(result[max_key][1][0], result[max_key][0]))
