import turtle
import math

x1, y1, r1 = map(float, input("координаты центра и радиус первой окружности (x1 y1 r1) ").split())
x2, y2, r2 = map(float, input("координаты центра и радиус второй окружности (x2 y2 r2) ").split())

d = math.hypot(x2 - x1, y2 - y1)
if d > r1 + r2:
    position = "Окружности лежат одна вне другой, не касаясь"
elif math.isclose(d, r1 + r2):
    position = "Окружности имеют внешнее касание"
elif d < abs(r1 - r2):
    position = "Одна окружность лежит внутри другой, не касаясь"
elif math.isclose(d, abs(r1 - r2)):
    position = "Окружности имеют внутреннее касание"
else:
    position = "Окружности пересекаются"
print(position)

t = turtle.Turtle()
t.speed(0)
def draw_circle(x, y, r):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.circle(r)
draw_circle(x1, y1, r1)
draw_circle(x2, y2, r2)
turtle.done()