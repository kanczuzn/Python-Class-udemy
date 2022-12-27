import turtle
import write_state

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=720, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
write_state = write_state.StateWrite()


def main():
    turtle.shape(image)
    game_on = True
    answer_state = screen.textinput(title="Guess a State", prompt="What's the name of a state?").title().strip()
    while game_on:
        write_state.write_state(answer_state)
        if write_state.score == 50:
            write_state.win()
            break
        elif write_state.score == -1:
            write_state.exit()
            break
        else:
            answer_state = screen.textinput(title=f"{write_state.score}/50 States Correct",
                                            prompt="What's the name of another state?").title().strip()


if __name__ == "__main__":
    main()
    screen.exitonclick()
