def sum_progress(a1, r, n):
    '''Рекурсивная функцию для нахождения суммы n членов прогрессии'''
    if n == 1:
        return a1
        
    curr_n = a1 + (n - 1) * r
    
    return curr_n + sum_progress(a1, r, n - 1)
