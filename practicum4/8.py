print('Здравствуйте! Как Вас зовут?', end=' ')
name = input()

print(f'Очень приятно, {name}! Меня зовут Марк.')

print('Сколько Вам лет?', end=' ')
age = int(input())


mark_age = 80

if age < mark_age:
    difference = mark_age - age
    print(f'Да, {name}, я старше Вас на {difference} лет.')
else:
    difference = age - mark_age
    print(f'Да, {name}, Вы старше меня на {difference} лет.')

print('Вам нравится программировать?', end=' ')
answer = input().lower()

if answer == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
else:
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')