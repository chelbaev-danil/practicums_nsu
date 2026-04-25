def mod_number(a, b):
    if a < b:
        return a
    return mod_number(a - b, b)
