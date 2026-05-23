def ten_to_n(x, n):
    '''Функцию для перевода натурального числа x из десятичной системы счисления в n-ричную (2≤n≤16)''' 
    digits = "0123456789ABCDEF"
    if x < n:
        return digits[x]
    return ten_to_n(x // n, n) + digits[x % n]
