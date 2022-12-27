from turtle import Turtle
import pandas

FONT_WIN = ("Courier", 24, "normal")
FONT = ("Courier", 8, "normal")


class StateWrite(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.score = 0
        self.guessed_states = []
        self.states = pandas.read_csv("50_states.csv")

    def write_state(self, guess):
        if guess == "Exit":
            self.score = -1
        elif self.is_state(guess):
            if guess not in self.guessed_states:
                self.score += 1
                self.guessed_states.append(guess)
                state_data = self.states[self.states.state == guess]
                self.goto(int(state_data.x), int(state_data.y))
                self.write(guess, align="left", font=FONT)

    def is_state(self, guess):
        return guess in self.states.state.values

    def win(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n"
                   f" YOU WIN!", align="center", font=FONT_WIN)

    def exit(self):
        self.goto(0, 0)
        self.write(f"    GAME OVER\n"
                   f"THANKS FOR PLAYING!", align="center", font=FONT_WIN)
        missing_states = [state for state in self.states.state if state not in self.guessed_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv('states_to_learn.csv')
