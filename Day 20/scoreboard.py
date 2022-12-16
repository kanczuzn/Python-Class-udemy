from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 265)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)