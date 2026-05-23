count = int(input())

antonyms = {}

for i in range(count):
    pair = input().split()
    word1, word2 = pair[0], pair[1]
    antonyms[word1] = word2
    antonyms[word2] = word1

word = input()
print(antonyms.get(word, word))