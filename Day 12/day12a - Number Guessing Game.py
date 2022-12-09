from art import logo
from random import randint


EASY = 10
HARD = 5


def main():
    print(f"{logo}\nWelcome to the Number Guessing Game!"
          f"\nI'm thinking of a number between 1 and 100.")
    game()


def usr_choice(choice1, choice2):
    """Takes user input, sets to lower case, strips of leading/trailing whitespace,
    and grabs the first character. If it matches the first character of the choices,
    return True or False respectively. If not, raises an IndexError. Index error
    because just hitting 'enter' will result in this as well, making it the most
    common error to try and catch.

    Choice1 and Choice2 should be lowercase or numbers."""
    check = False
    while check is False:
        try:
            check = input().strip().lower()[0]
            if check == choice1[0]:
                return True
            elif check == choice2[0]:
                return False
            else:
                raise IndexError
        except IndexError:
            print(f"Please select either '{choice1}' or '{choice2}'")
            check = False


def game():
    """Runs through the game, choosing random numbers, runs functions to compare, etc."""
    chances = set_difficulty()
    comp_num = randint(1, 100)
    game_on = True
    while game_on:
        print(f"\nYou have {chances} attempts remaining to guess the number.")
        check_answer(comp_num)
        chances -= 1
        if chances == 0:
            print("You've run out of guesses, you lose. D:"
                  f"\nThe number was: {comp_num}")
            play_again()


def set_difficulty():
    """Sets the difficulty of the game based on user input.

    Returns either EASY or HARD global variables."""
    print("Choose a difficulty. Type 'easy' or 'hard': ")
    difficulty = usr_choice("easy", "hard")
    if difficulty is True:
        return EASY
    else:
        return HARD


def check_answer(comp_num):
    """Checks the answer to see if you've guessed right or if the number is too high or low.
    Takes the number that is being guessed against to check against."""
    check_on = True
    while check_on:
        try:
            guess = int(input("Make a guess: "))
            if guess > comp_num:
                print("Too high.")
            elif guess < comp_num:
                print("Too low.")
            else:
                print(f"You guessed right! The number was {comp_num}!")
                play_again()
            return
        except ValueError:
            print("\nPlease type in a whole number.\n")


def play_again():
    """Checks if the user wishes to play again, if not, prints 'Thanks for playing!'"""
    print("Would like to play again?")
    play = usr_choice("yes", "no")
    if play is True:
        game()
    else:
        print("\nThanks for playing!")
        exit(0)


if __name__ == "__main__":
    main()
