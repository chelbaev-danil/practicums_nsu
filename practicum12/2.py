def counnnt(n):
    '''Рекурсивная функция для вычисления количества цифр натурального числа.'''
    if n < 10:
        return 1

    return 1 + counnnt(n // 10)

print(counnnt(12345))  # 5
