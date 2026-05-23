def simmetr(s, i, j):
    '''
    Функция, определяющую, является ли симметричной 
    часть строки s, начиная с i-го символа и заканчивая j-м
    '''
    if i >= j: 
        return True
    if s[i] != s[j]: 
        return False
    return simmetr(s, i + 1, j - 1)
