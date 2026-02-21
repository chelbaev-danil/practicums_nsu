print("Ведущий вводит две строки: подсказку и загаданное слово.")

tip = input() 
word = input() 

for i in range(25):
    print("")

print("Игрок пытается отгадать слово:")
print(tip)
print("*" * len(word))
guessing_word = "*" * len(word)
attempts = 10

while attempts > 0:
    char_or_word = input("Буква или слово (0 - буква, 1 - слово)? ")

    if char_or_word == "0":
        char = input("Введите букву: ")
        if char in word:
            print("Есть такая буква!")
            for i in range(len(word)):
                if word[i] == char:
                    guessing_word = guessing_word[:i] + char + guessing_word[i+1:]
            print(guessing_word)
            if guessing_word == word:
                print("Вы угадали слово!")
                break
        else:
            print("Нет такой буквы!")
            attempts -= 1
            if attempts == 0:
                print("У вас закончились попыток! Загаданное слово было:", word)
                break
            else:
                print("Осталось попыток:", attempts)
    elif char_or_word == "1":
        guess = input("Введите слово: ")
        if guess == word:
            print("Вы угадали слово!")
            break
        else:
            print("Неправильное слово! Вы проиграли! Загаданное слово было:", word)
            break
