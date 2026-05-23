def ind_maxlist(a):
    '''для вычисления индекса максимального элемента списка целочисленных элементов'''
    if len(a) == 1:
        return 0
        
    idx = ind_maxlist(a[1:]) + 1
    return 0 if a[0] >= a[idx] else idx
