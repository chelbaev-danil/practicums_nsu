def color(c):
    col_num = ord(c[0]) - ord('a') + 1
    row_num = int(c[1])

    # Проверка цвета клетки
    if (col_num + row_num) % 2 == 0:
        return "черная"
    else:
        return "белая"
    
def hod(h1, h2):
    if color(h1) != color(h2):
        if abs(int(h1[1]) - int(h2[1])) == 2 or abs(int(h1[0]) - int(h2[0])) == 2:
            return "верно"
    return "неверно"

a, b = map(str, input().split("-"))

print(hod(a, b))