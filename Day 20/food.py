from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")


    def refresh(self):
        color = (randint(50, 255), randint(50, 255), randint(50, 255))
        self.color(color)
        position = (randint(-280, 280), randint(-280, 280))
        self.goto(position)
        return color
