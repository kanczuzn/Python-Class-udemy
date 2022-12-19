from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.lines()
        self.goto(-280, 260)
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def lines(self):
        self.goto(-300, 260)
        self.pd()
        self.goto(300, 260)
        self.pu()
        self.goto(-300, -260)
        self.pd()
        self.goto(300, -260)
        self.pu()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def win(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n"
                   f" YOU WIN!", align="center", font=FONT)

    def lose(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n"
                   f" YOU LOST", align="center", font=FONT)
