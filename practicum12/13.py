def odd_list(a, n):
    if n == 0:
        return []
    res = odd_list(a, n - 1)
    if a[n - 1] % 2 == 0:
        res.append(a[n - 1])
    return res
