from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car = None
        self.car_list = []
        self.i = 0

    def generate_cars(self):
        generate = random.randint(0,5)
        if generate == 1:
            self.car = Turtle('square')
            self.car.penup()
            self.car.shapesize(1, 3)
            self.car.color(random.choice(COLORS))
            self.car.goto(300, random.randint(-240, 250))
            self.car_list.append(self.car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE + self.i*MOVE_INCREMENT)
