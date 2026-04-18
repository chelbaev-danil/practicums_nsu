import string

text = []
while True:
    line = input().strip()
    if not line:        
        break
    text.append(line)

full_text = ' '.join(text)

clean_text = full_text.translate(str.maketrans('', '', string.punctuation))

words = clean_text.lower().split()

freq = {}
order = []

for word in words:
    if word not in freq:
        freq[word] = 0
        order.append(word)
    freq[word] += 1

sorted_words = sorted(order, key=lambda x: (-freq[x], order.index(x)))

for word in sorted_words:
    print(word)