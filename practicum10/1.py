
def calculate_letters(s):

    glasn = 'аеёиоуыэюя'
    soglasn = 'бвгдкжзлмнпрстфхцчшщъьй'

    gl = 0
    sogl = 0

    for letter in s:
        if letter in glasn:
            gl += 1
        elif letter in soglasn:
            sogl += 1
            
    print('Гласных букв: ' + str(gl))
    print('Согласных букв: ' + str(sogl))

s = input('Введите строку: ')
calculate_letters(s)