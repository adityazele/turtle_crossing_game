from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.turtle = Turtle('turtle')
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(0, -280)

    def forward(self):
        self.turtle.forward(10)
