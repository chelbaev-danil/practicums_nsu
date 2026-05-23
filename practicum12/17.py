def function1(x):
    '''функция, определяющую, является ли заданное натуральное число x простым'''
    if x < 2: return 0
        
    def check(d):
        if d * d > x: return 1  # Делителей не нашли
        if x % d == 0: return 0 # Нашли делитель
        return check(d + 1)
        
    return check(2)
