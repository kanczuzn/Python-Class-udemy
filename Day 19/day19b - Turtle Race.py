from turtle import Turtle, Screen
from tkinter import messagebox
from random import randint


class RaceTurtle(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5)
        self.color(color)
        self.pu()


screen = Screen()
screen.setup(width=500, height=400)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def main():
    turtles = []
    winner = ""
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    for x in range(6):
        turtles.append(RaceTurtle(COLORS[x]))
        turtles[x].goto(x=-235, y=-125+50*x)
    if user_bet:
        winner = race_start(turtles)
    if winner == user_bet:
        mess_title = "You win!!"
    else:
        mess_title = "You lose. D:"
    mess_sub = f"The winner is: {winner.title()}"
    messagebox.showinfo(mess_title, mess_sub)


def race_start(turtles):
    winners = []
    race_on = True
    winner = ""
    while race_on:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() >= 220:
                race_on = False
                winners.append(turtle)
    if len(winners) > 1:
        win = 0
        for turtle in winners:
            if turtle.xcor() > win:
                win = turtle.xcor()
                winner = turtle.pencolor()
    else:
        winner = winners[0].pencolor()
    return winner


if __name__ == "__main__":
    main()
    screen.exitonclick()
