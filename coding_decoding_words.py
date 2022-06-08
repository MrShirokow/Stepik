code_vocabulary = dict(zip(input(), input()))
code_word = ''.join(code_vocabulary[char] for char in input())

decode_vocabulary = {v: k for (k, v) in code_vocabulary.items()}
decode_word = ''.join(decode_vocabulary[char] for char in input())

print(f'{code_word}\n{decode_word}')
