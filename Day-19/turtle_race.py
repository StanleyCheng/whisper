from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle win win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y = [-70,-40,-10,20,50,80]
turtle_list=[]

for turtle_index in range (0,6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[turtle_index])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=y[turtle_index])
    turtle_list.append(newTurtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0,10))
        if turtle.pos()[0] >= 220:
            winner = turtle.color()[0]
            is_race_on = False
            if winner == user_bet:
                print(f"Your bet is {user_bet} and you WON! Congrats!")
            else:
                print(f"Your bet is {user_bet} and the winner is {winner}, so you lost!")


screen.exitonclick()