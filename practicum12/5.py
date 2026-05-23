def mod_number(a, b):
    '''
    Рекурсивная функция для нахождения остатка от 
    деления натурального числа a на натуральное число b
    '''
    if a < b:
        return a
        
    return mod_number(a - b, b)
