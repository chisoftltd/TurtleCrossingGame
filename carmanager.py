from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "violet", "black", "gold"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.right(180)
        self.goto(280, STARTING_MOVE_DISTANCE * position)

        self.move_car()

    def move_car(self):
        self.forward(MOVE_INCREMENT + random.randint(0, 10))
