from turtle import Turtle
from random import randint
MOVE_DISTANCE = 10
SNAKE_START = [(0, 0), (-10, 0), (-20, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()


    def create_snake(self):
        for position in SNAKE_START:
            color = [randint(25, 255), randint(25, 255), randint(25, 255)]
            self.new_seg(position, color)
        self.head = self.segment[0]

    def new_seg(self,position, color):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(.5)
        new_segment.pu()
        new_segment.color(color)
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self, color):
        self.new_seg(self.segment[-1].position(), color)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_coord = self.segment[seg_num - 1].position()
            self.segment[seg_num].goto(new_coord)
        self.head.forward(MOVE_DISTANCE)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.segment:
            seg.hideturtle()
        self.segment.clear()
        self.create_snake()
