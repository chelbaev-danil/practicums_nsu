import turtle

def draw_star(size, color_fill, color_border):

    turtle.fillcolor(color_fill)
    turtle.pencolor(color_border)
    turtle.pensize(3)
    
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def draw_flower(size, color_petals, color_center):

    turtle.fillcolor(color_petals)
    turtle.pencolor("black")
    
    for _ in range(8):
        turtle.begin_fill()
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.left(180)
        turtle.end_fill()
        turtle.right(45)
    
    # Центр цветка
    turtle.fillcolor(color_center)
    turtle.begin_fill()
    turtle.circle(size // 2)
    turtle.end_fill()


def draw_hexagon(size, color_fill, color_border):

    turtle.fillcolor(color_fill)
    turtle.pencolor(color_border)
    turtle.pensize(4)
    
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()


def draw_ornament():
    turtle.speed(0)     
    turtle.bgcolor("#1a0033")
    turtle.hideturtle()
    

    spacing = 120          
 
    for row in range(-2, 3):          
        for col in range(-3, 4):  
            
            x = col * spacing
            y = row * spacing - 30
            
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            
            
            element = (row + col) % 3
            
            if element == 0:
           
                draw_star(45, "#ffd700", "#ffaa00")
            elif element == 1:
       
                draw_flower(28, "#ff69b4", "#ffff00")
            else:
       
                draw_hexagon(50, "#40e0d0", "#008080")
    
    turtle.penup()
    turtle.goto(-380, -280)
    turtle.pendown()
    turtle.pencolor("#ffd700")
    turtle.pensize(8)
    for _ in range(4):
        turtle.forward(760)
        turtle.left(90)
    
    turtle.hideturtle()


draw_ornament()

turtle.done()