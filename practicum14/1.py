words = map(str, input().split())

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_words = sorted(freq, key=lambda w: freq[w], reverse=True)

for word in sorted_words:
    print(word)