from turtle import Turtle
from random import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.move_speed = 0

    def start(self, heading):
        self.move_speed = 5
        self.goto(0, 0)
        self.setheading(heading)

    def move(self):
        self.forward(self.move_speed)

    def bounce(self):
        self.setheading((self.heading() * -1) + random())

    def bounce_paddle(self):
        if 90 <= self.heading() <= 180:
            new_heading = 360 + (180 - self.heading()) - random()
            self.setheading(new_heading)
        else:
            new_heading = 180 + (360 - self.heading()) + random()
            self.setheading(new_heading)
        self.move_speed += 1
