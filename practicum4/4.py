print('Вы поедете на бал?')


answer = input("Ответ: ").lower()


if not ("да" in answer or "нет" in answer):
    print("Верно")
else:
    print("Неверно")