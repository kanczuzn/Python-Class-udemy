from random import choice
from art import logo, vs
from game_data import data
from os import system as sys
from os import name as sysname
from custom_choice import usr_choice


A_OR_AN_VOW = ['a', 'e', 'i', 'o', 'u']
A_OR_AN_ABBR = ['a', 'e', 'i', 'o', 'f', 'l', 'm', 'n', 'r', 's', 'x']


def main():
    game_on = True
    score = 0
    clear()
    print(logo)
    person_b = choice(data)
    while game_on:
        person_a = person_b
        while person_a == person_b:
            person_b = choice(data)
        print(f"Compare A: {print_str(person_a)}")
        print(vs)
        print(f"Against B: {print_str(person_b)}")
        a_follower_count = int(person_a['follower_count'])
        b_follower_count = int(person_b['follower_count'])
        guess = usr_choice("Who has more followers? Type 'A' or 'B': ", "ab")
        if check_answer(guess, a_follower_count, b_follower_count) is True:
            score += 1
            outcome(True, score)
        else:
            outcome(False, score)
            game_on = False
    plyr_choice = usr_choice("Would you like to play again? (Y/N) ", "yn")
    if plyr_choice == "y":
        clear()
        main()
    else:
        print("Thanks for playing!"
              "\n              Code by c0yot3")


def check_answer(guess, choice_a, choice_b):
    if choice_a > choice_b:
        return guess == "a"
    else:
        return guess == "b"


def outcome(win, score):
    """Prints whether it's a win or a loss."""
    clear()
    print(logo)
    if win is True:
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


def print_str(person):
    """Returns a print string to be displayed in the format 'Name', 'Description', from 'Country'.
    This is based on a dictionary."""
    final_string = f"{person['name']}, "
    pers_desc = person['description']
    pers_desc_ck = person['description'][:4].lower().strip()
    if len(pers_desc_ck) < 4:
        if any(letter in pers_desc_ck[0] for letter in A_OR_AN_ABBR):
            final_string += f"an {pers_desc}, "
        else:
            final_string += f"a {pers_desc}, "
    else:
        if any(letter in pers_desc_ck[0] for letter in A_OR_AN_VOW):
            final_string += f"an {pers_desc}, "
        else:
            final_string += f"a {pers_desc}, "
    final_string += f"from {person['country']}."
    return final_string


def clear():
    sys('cls' if sysname == 'nt' else 'clear')


if __name__ == "__main__":
    main()
