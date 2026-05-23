n = int(input())

dictionary = {}

for _ in range(n):
    pair = input().split()
    ru, en = pair[0], pair[1]
    dictionary[ru] = en

phrase = input().split()
result = [dictionary.get(word, word) for word in phrase]
print(' '.join(result))