def progress(a1, r, n):
    '''Рекурсивная функция для нахождения n-го члена прогрессии'''
    if n == 1:
        return a1
   
    return progress(a1, r, n - 1) + r

print(progress(2, 3, 5))  # Выведет 14
