import random
import string
from hangman_art import logo, stages
from hangman_words import word_list

game_on = True
win = 0
loss = 0

def main():
    while game_on:
        print(logo)
        play()

def play():
    global game_on
    if win + loss > 0:
        play = input("Would you like to play again? Y/N\n").lower()[0]
    else:
        play = input("Would you like to play? Y/N\n").lower()[0]

    if play == "y":
        hangman()
    else:
        game_on = False
        print("Thanks for playing!"
              f"\nYou won:  {win} times."
              f"\nYou lost: {loss} times.")

def hangman():
    global win
    global loss
    game_word = random.choice(word_list).lower()
    hang_word_list = ['_'] * len(game_word)
    lives = 6
    guesses = []
    print(stages[lives])
    while lives > 0 and "_" in hang_word_list:
        print(f"{' '.join(hang_word_list)}")
        guess = input("Guess a letter: ").lower()[0]
        if guess in guesses:
            print(f"\nYou already guessed: {guess}")
        elif guess in string.digits:
            print("\nFuck off! That's a number!")
        else:
            guesses += [guess]
            if guess in game_word:
                for ct in range(len(game_word)):
                    if game_word[ct] == guess:
                        hang_word_list[ct] = guess
            else:
                print(f"You guessed {guess}, that's not in the word.")
                lives -= 1
            print(stages[lives])
    print(f"The word is: {game_word.title()}")
    if lives == 0:
        print("You lose. D:")
        loss += 1
    else:
        print("You win!")
        win += 1
    play()

main()
