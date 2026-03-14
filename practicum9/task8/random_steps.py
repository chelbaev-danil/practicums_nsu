import random
with open ("task8/input.txt", "w", encoding='utf-8') as f:
    for i in range(1, 366):
        f.write(f"{random.randint(2000, 10000)}\n")
