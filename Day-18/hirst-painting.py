import random
import turtle
from turtle import Turtle, Screen

# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r,g,b))

# Remember to change color scheme to 255 to use RGB tuple
turtle.colormode(255)
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

print(color_list[0])

t = Turtle()
t.speed("fastest")
t.hideturtle()
x = -250
y = -250

while y <= 250:
    while x <= 250:
        t.teleport(x,y)
        # t.penup()
        # t.forward(100)
        t.dot(20,random.choice(color_list))
        x += 50
    if x > 250:
        x = -250
    y += 50


s = Screen()
s.exitonclick()
