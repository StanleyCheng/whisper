import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["bisque3","coral","cyan2","deeppink","DarkOrchid","darkolivegreen2","brown","burlywood","DarkRed"]
tim.color("black")

# def drawPolygon(no_of_sides):
#     turn_angle = 360/no_of_sides
#     for i in range(1,no_of_sides+1):
#         tim.fd(100)
#         tim.right(turn_angle)
#
# for sides in range(3,11):
#     tim.color(random.choice(colors))
#     drawPolygon(sides)
turtle.colormode(255)
tim.pensize("15")
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)





for _ in range(200):
    tim.setheading(random.choice([0,90,180,270]))
    tim.color(random_color())
    tim.forward(30)



screen = Screen()
screen.exitonclick()
