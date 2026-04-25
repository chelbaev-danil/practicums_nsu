def degree5(n):
    if n == 1:
        return 0
    if n < 1 or n % 5 != 0:
        return -1
    res = degree5(n // 5)
    return res + 1 if res != -1 else -1
