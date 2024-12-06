import turtle
import ball
import random
import run_ball
import seven_segments_proc

class RS:
    def __init__(self) -> None:
        num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.color = []
        for i in range(num_balls):
            self.x.append(random.uniform(-1*self.canvas_width + ball_radius, self.canvas_width - ball_radius))
            self.y.append(random.uniform(-1*self.canvas_height + ball_radius, self.canvas_height - ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def run(self):
        run_ball(size, self.x, self.y, self.vx, self.vy, self.color)
