print("Ведущий вводит число")

number = input()

for i in range(25):
    print("")

attempts = 10
print("Игрок пытается отгадать число")
while attempts > 0:
    if attempts == 0:
        print("У вас закончились попытки! Вы проиграли!, число было", number)
        break
    guess = input()
    cows = 0
    bulls = 0

    for a, b in zip(number, guess):
        if a == b:
            bulls += 1
        elif a in guess:
            cows += 1
    print(f"Быков: {bulls}, Коров: {cows}")
    if bulls == len(number):
        print("Победа")
        break
    attempts -= 1
    

