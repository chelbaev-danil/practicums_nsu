import turtle
def dr(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y1)
    turtle.goto(x2, y2)
    turtle.goto(x1, y2)
    turtle.goto(x1, y1)

x1, y1, x2, y2 = map(float, input("Координаты верхней левой и правой нижней вершин первого прямоугольника (x1 y1 x2 y2): ").split())
x3, y3, x4, y4 = map(float, input("Координаты верхней левой и правой нижней вершин второго прямоугольника (x3 y3 x4 y4): ").split())
left1, right1 = min(x1, x2), max(x1, x2)
top1, bottom1 = max(y1, y2), min(y1, y2)
left2, right2 = min(x3, x4), max(x3, x4)
top2, bottom2 = max(y3, y4), min(y3, y4)

if right1 < left2 or right2 < left1 or bottom1 > top2 or bottom2 > top1:
    position = "Прямоугольники лежат вне друг друга, не касаясь"
elif (right1 == left2 or right2 == left1) and not (bottom1 > top2 or bottom2 > top1):
    position = "Прямоугольники имеют касание"
elif not (right1 < left2 or right2 < left1 or bottom1 > top2 or bottom2 > top1):
    if (left1 >= left2 and right1 <= right2 and bottom1 >= bottom2 and top1 <= top2):
        position = "Один прямоугольник лежит внутри другого, не касаясь"
    elif (left2 >= left1 and right2 <= right1 and bottom2 >= bottom1 and top2 <= top1):
        position = "Один прямоугольник лежит внутри другого, не касаясь"
    else:
        position = "Прямоугольники пересекаются"
else:
    position = "Прямоугольники лежат вне друг друга, не касаясь"

print(position)

turtle.speed(0)
dr(x1, y1, x2, y2)
dr(x3, y3, x4, y4)
turtle.done()