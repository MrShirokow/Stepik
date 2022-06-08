known_count: int = int(input())
known_words: set = {input().lower() for i in range(known_count)}
n: int = int(input())
words: set = {w.lower() for j in range(n) for w in input().split()}

result: set = words - known_words
print(*result, sep='\n')
