known_count = int(input())
known_words = {input().lower() for i in range(known_count)}
n = int(input())
words = {w.lower() for j in range(n) for w in input().split()}

result = words - known_words
print(*result, sep='\n')
