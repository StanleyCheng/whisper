from turtle import Turtle
# Example CONSTANTS in Python in all CAPS
delta_x = 0
delta_y = 0
starting_position = [(delta_x, delta_y), (delta_x-20, delta_y), (delta_x-40, delta_y)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        # self.x=0
        # for _ in range(3):
        for item in starting_position:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.setposition(item)
            # turtle.setx(self.x)
            # self.x -= 20
            self.snake.append(turtle)

    def move(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
