import turtle


class ssp:
    def __init__(my_turtle, color):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        
        my_turtle.color(color)
        my_turtle.penup()
        my_turtle.setheading(0)
        my_turtle.goto(0, 0)
        my_turtle.pensize(10)

    def draw(my_turtle, digit):
        if digit == 0:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 1:
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 2:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 3:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 4:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 5:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 6:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()
        
        if digit == 7:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 8:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 9:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        def clear(my_turtle):
            my_turtle.clear()

        # def my_delay(dt):
        #     import time
        #     start =  time.time()
        #     while time.time() - start < dt:
        #     pass

# Tom = turtle.Turtle()
# tom_color = (255, 0, 0)
# init(Tom, tom_color)
# delay_in_seconds = 0.2
# while True:
#     for i in range(0, 10):
#         clear(Tom)
#         draw(Tom, i)
#         my_delay(delay_in_seconds)
#         turtle.update()

# turtle.done()

