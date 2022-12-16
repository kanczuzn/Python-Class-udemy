from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def turn_right():
    tim.right(5)


def turn_left():
    tim.left(5)


def clear_screen():
    tim.home()
    tim.clear()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()
