from turtle import Turtle
UP = 90


class Paddle(Turtle):

    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.setheading(UP)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.speed("fastest")
        self.goto(location)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(20)

    def move_down(self):
        if -240 < self.ycor():
            self.backward(20)
