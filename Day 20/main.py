from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)



def snake_game():
    snake = Snake()
    food = Food()
    color = food.refresh()
    score = Scoreboard()
    game_on = True
    while game_on:
        time.sleep(.03)
        screen.update()
        snake.move()
        if -300 >= snake.head.xcor() or snake.head.xcor() >= 300 or \
                -300 >= snake.head.ycor() or snake.head.ycor() >= 300:
            game_on = False
            score.game_over()
        if snake.head.distance(food) < 15:
            score.point()
            snake.extend(color)
            color = food.refresh()
        for seg in snake.segment[1:]:
            if snake.head.distance(seg) < 5:
                game_on = False
                score.game_over()
        screen.listen()
        screen.onkeypress(key="Right", fun=snake.snake_right)
        screen.onkeypress(key="Left", fun=snake.snake_left)
        screen.onkeypress(key="Up", fun=snake.snake_up)
        screen.onkeypress(key="Down", fun=snake.snake_down)


def main():
    snake_game()


if __name__ == "__main__":
    main()
    screen.exitonclick()
