sentence = input().strip()

words = []
for word in sentence.split():
    clean_word = word.strip(".,!?;:'\"-()[]{}")
    if clean_word:  
        words.append(clean_word)

print(words)