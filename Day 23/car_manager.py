from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = 0

    def start(self):
        self.car_speed = STARTING_MOVE_DISTANCE

    def cars_go(self):
        new_car = randint(0, 30)
        if new_car < 6:
            y = randint(0, 25) * 20
            y -= 250
            x = 300
            for car in self.cars:
                if car.ycor() == y and car.xcor() >= 260:
                    x = car.xcor() + 50
            position = (x, y)
            self.new_car(position, new_car)
        for car in self.cars:
            car.forward(self.car_speed)

    def new_car(self, position, color):
        car = Turtle()
        car.setheading(180)
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.pu()
        car.goto(position)
        car.color(COLORS[color])
        self.cars.append(car)

    def level_up(self):
        for car in self.cars:
            car.hideturtle()
        self.car_speed += MOVE_INCREMENT
        self.cars.clear()
