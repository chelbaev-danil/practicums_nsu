num = int(input())

if num // 1000 == num % 10 and (num // 10) % 10 == (num // 100) % 10: 
    print("Настоящее")
else:
    print("Кривое")

