def pownum(a, n):
    ''' Считает степень через рекурсивную функцию '''
    if n == 1:
        return a
    
    return a * pownum(a, n - 1)

print(pownum(2.5, 3)) # 15.625
