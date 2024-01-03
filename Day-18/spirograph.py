import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
t = Turtle()
t.speed("fastest")
tilt_angle = 5
radius = 100
angle = 0

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


while angle < 360:
    t.pencolor(random_color())
    t.circle(radius)
    t.left(tilt_angle)
    angle += tilt_angle













s = Screen()
s.exitonclick()




























