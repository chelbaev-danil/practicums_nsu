rec = input("Введите рекорды трех игроков через пробел: ")


a, b, c = map(int, rec.split())


best_score = a  

if b > best_score:
    best_score = b

if c > best_score:
    best_score = c

print(best_score)