def search(a, x):
    ''' рекурсивную функцию search(a,x), определяющую, имеется ли среди целочисленных значений списка a, число x '''
    if not a:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)
