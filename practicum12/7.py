def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)
