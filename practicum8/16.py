text = input()
balance = 0

for char in text:
    if char == "(":
        balance += 1
    elif char == ")":
        balance -= 1
    if balance < 0:
        print("Несбалансированно")
        break
else: 
    if balance == 0:
        print("Сбалансированно")
    elif balance > 0:
        print("Несбалансированно")