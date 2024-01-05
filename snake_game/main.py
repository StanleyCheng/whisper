from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # stop the default animation
screen.update()


snake = Snake()
food = Food()

screen.update()

screen.listen()
# keymap key case sensitive
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # only update the screen when all segments of the snakes are ready
    time.sleep(0.1)

    snake.move()

    # snake[0].left(90)

screen.exitonclick()
