import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


def main():
    game_is_on = True
    score = Scoreboard()
    player = Player()
    cars = CarManager()
    cars.start()
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.cars_go()
        screen.onkeypress(key="Up", fun=player.move_forward)
        if player.ycor() >= 280:
            if score.level == 5:
                game_is_on = False
                score.win()
            else:
                player.move_forward()
                score.level_up()
                cars.level_up()
        elif player.ycor() >= -270:
            for car in cars.cars:
                if car.distance(player) <= 20:
                    game_is_on = False
                    score.lose()


if __name__ == "__main__":
    main()
    screen.exitonclick()
