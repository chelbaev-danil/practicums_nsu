sentence = input().strip()

words = []
seen = set()

for word in sentence.split():
    clean_word = word.strip(".,!?;:'\"-()[]{}").lower()
    if clean_word and clean_word not in seen:
        seen.add(clean_word)
        words.append(clean_word)

print(words)