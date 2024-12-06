import turtle
import ball
import random
import math

class rb:
    def __init__(self, size, x, y, vx, vy, color, id):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100*size**2
        self.count = 0
        self.id = id
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.dt = 0.2

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y-self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def bounce_off_vertical_wall(self):
            self.vx = -self.vx
            self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1

    def bounce_off(self, that):
        dx  = that.x - self.x
        dy  = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx*dvx + dy*dvy
        dist = self.size + that.size

        magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)

        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        self.vx += fx / self.mass
        self.vy += fy / self.mass
        that.vx -= fx / that.mass
        that.vy -= fy / that.mass
        
        self.count += 1
        that.count += 1

    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2-y1)**2 + (x2-x1)**2)
        return d

    def move(self):
        self.x += self.vx*self.dt
        self.y += self.vy*self.dt

    def time_to_hit(self, that):
        if self is that:
            return math.inf
        dx  = that.x - self.x
        dy  = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx*dvx + dy*dvy
        if dvdr > 0:
            return math.inf
        dvdv = dvx*dvx + dvy*dvy
        if dvdv == 0:
            return math.inf
        drdr = dx*dx + dy*dy
        sigma = self.size + that.size
        d = (dvdr*dvdr) - dvdv * (drdr - sigma*sigma)
        if d < 0:
            return math.inf
        t = -(dvdr + math.sqrt(d)) / dvdv

        if t <= 0:
            return math.inf

        return t

    def time_to_hit_vertical_wall(self):
        if self.vx > 0:
            return (self.canvas_width - self.x - self.size) / self.vx
        elif self.vx < 0:
            return (self.canvas_width + self.x - self.size) / (-self.vx)
        else:
            return math.inf

    def time_to_hit_horizontal_wall(self):
        if self.vy > 0:
            return (self.canvas_height - self.y - self.size) / self.vy
        elif self.vy < 0:
            return (self.canvas_height + self.y - self.size) / (-self.vy)
        else:
            return math.inf

# num_balls = 5
# turtle.speed(0)
# turtle.tracer(0)
# turtle.hideturtle()
# canvas_width = turtle.screensize()[0]
# canvas_height = turtle.screensize()[1]
# print(canvas_width, canvas_height)
# ball_radius = 0.05 * canvas_width
# turtle.colormode(255)
# xpos = []
# ypos = []
# vx = []
# vy = []
# ball_color = []

# create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
# for i in range(num_balls):
#     xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
#     ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
#     vx.append(10*random.uniform(-1.0, 1.0))
#     vy.append(10*random.uniform(-1.0, 1.0))
#     ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# def draw_border():
#     turtle.penup()
#     turtle.goto(-canvas_width, -canvas_height)
#     turtle.pensize(10)
#     turtle.pendown()
#     turtle.color((0, 0, 0))
#     for i in range(2):
#         turtle.forward(2*canvas_width)
#         turtle.left(90)
#         turtle.forward(2*canvas_height)
#         turtle.left(90)

# dt = 0.2 # time step
# while (True):
#     turtle.clear()
#     draw_border()
#     for i in range(num_balls):
#         ball.draw_ball(ball_color[i], ball_radius, xpos[i], ypos[i])
#         ball.move_ball(i, xpos, ypos, vx, vy, dt)
#         ball.update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
#     turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
