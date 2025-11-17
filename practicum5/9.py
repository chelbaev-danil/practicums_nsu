# Ввод высот трёх башен через пробел
a,b,c = map(int, input().split())

# Упорядочивание высот от наибольшей к наименьшей
if a > b and a > c:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > a and b > c:
    if a > c:
        print(b, a, c)
    else:
        print(b, c, a)
if c > b and c > a:
    if b > c:
        print(c, b, a)
    else:
        print(c, a, b)
