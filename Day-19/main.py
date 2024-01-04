from turtle import Turtle,Screen

t = Turtle()

def moveForward():
    t.forward(10)

def moveBackward():
    t.backward(10)

# def counterClockwise():
#     t.circle(50,10)
#
# def clockwise():
#     t.circle(-50,10)


def turn_right():
    t.right(10)

def turn_left():
    t.left(10)



def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


s = Screen()
s.onkey(moveForward,"w")
s.onkey(moveBackward,"s")
s.onkey(turn_left,"a")
s.onkey(turn_right,"d")
s.onkey(clear,"c")
s.listen()
s.exitonclick()






