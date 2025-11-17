from turtle import *
import math

center_x = float(input())
center_y = float(input())
radius = float(input())
point_x = float(input())
point_y = float(input())

screensize = (500, 500)
tracer(0)

up()
goto(center_x, center_y - radius)  # Move to the starting point of the circle
down()
circle(radius)

up()
goto(point_x, point_y)
down()
dot(6, "red")  # Draw a red dot for the point


distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)
if distance < radius:
    print("Точка внутри окружности ")
elif distance == radius:
    print("Точка на окружности")
else:
    print("Точка вне окружности")

done()