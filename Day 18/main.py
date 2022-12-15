import turtle
from turtle import Turtle, Screen, colormode
from random import randint, choice

tim = Turtle()
tim.shape("classic")
tim.shapesize(.1)
tim.color("green")
direction = [0, 90, 180, 270]
screen = Screen()


def main():
    colormode(255)
    for x in range(3, 11): # Creates shapes from 3 to 10 sided.
        tim.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
        for _ in range(x):
            tim.forward(100)
            tim.right(360/x)
    for _ in range(200): # random walk.
        tim.speed(0)
        tim.pensize(10)
        color = (randint(1, 255), randint(1, 255), randint(1, 255))
        tim.pencolor(color)
        tim.setheading(choice(direction))
        tim.forward(50)
    tim.pu()
    tim.home()
    tim.pd()
    circle = 3.6
    for _ in range(int(360/circle)):
        tim.pensize(1)
        tim.speed(0)
        tim.setheading(tim.heading() + circle)
        color = (randint(1, 255), randint(1, 255), randint(1, 255))
        tim.pencolor(color)
        tim.circle(100,360,100)


if __name__ == "__main__":
    main()
    screen.exitonclick()
