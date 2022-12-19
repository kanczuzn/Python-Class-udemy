from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("green")
        self.new_level()

    def new_level(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > 280:
            self.new_level()
