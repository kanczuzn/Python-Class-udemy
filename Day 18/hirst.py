from turtle import Turtle, Screen, colormode
import colorgram
from random import choice


COLORS_EXT = colorgram.extract("hirst.jpg", 100)
COLORS = []
screen = Screen()
turtle = Turtle()
turtle.speed(0)
turtle.pu()
turtle.hideturtle()


for color in COLORS_EXT:
    COLORS.append((color.rgb.r, color.rgb.g, color.rgb.b))
for _ in range(3):
    COLORS.pop(0)
print(COLORS)

def main():
    colormode(255)
    turtle.setheading(225)
    turtle.forward(350)
    for _ in range(10):
        turtle.setheading(0)
        for _ in range(10):
            turtle.dot(20,choice(COLORS))
            turtle.forward(50)
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)


if __name__ == "__main__":
    main()
    screen.exitonclick()
