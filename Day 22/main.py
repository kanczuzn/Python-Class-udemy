from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from random import choice
from scoreboard import Scoreboard


screen = Screen()
screen.clearscreen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong by c0yot3")
screen.listen()
screen.tracer(0)
START_DIR = [45, 135, 225, 315]


def main():
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    screen.onkeypress(key="Up", fun=r_paddle.move_up)
    screen.onkeypress(key="Down", fun=r_paddle.move_down)
    screen.onkeypress(key="w", fun=l_paddle.move_up)
    screen.onkeypress(key="s", fun=l_paddle.move_down)
    game_on = True
    ball.start(choice(START_DIR))
    while game_on:
        time.sleep(.025)
        ball.move()
        screen.update()
        # detect collision with top/bottom wall.
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce()
        # detect collision with right paddle
        if (ball.distance(r_paddle) < 60 and 330 < ball.xcor() < 345) or \
                (ball.distance(l_paddle) < 60 and -345 < ball.xcor() < -330):
            ball.bounce_paddle()
        if ball.xcor() > 380:
            new_heading = ball.heading() - 180
            ball.start(new_heading)
            game_on = scoreboard.lpoint()
        if ball.xcor() < -380:
            new_heading = ball.heading() + 180
            ball.start(new_heading)
            game_on = scoreboard.rpoint()


if __name__ == "__main__":
    main()
    screen.exitonclick()
