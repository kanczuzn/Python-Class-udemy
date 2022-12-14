import random
import time
from art import logo


cards = [
    {"\033[30;47m A": 11},
    {"\033[30;47m K": 10},
    {"\033[30;47m Q": 10},
    {"\033[30;47m J": 10},
    {"\033[30;47m10": 10},
    {"\033[30;47m 9": 9},
    {"\033[30;47m 8": 8},
    {"\033[30;47m 7": 7},
    {"\033[30;47m 6": 6},
    {"\033[30;47m 5": 5},
    {"\033[30;47m 4": 4},
    {"\033[30;47m 3": 3},
    {"\033[30;47m 2": 2},
]
suit = ['♥\033[m', '♦\033[m', '♤\033[m', '♧\033[m']


def main():
    play = choice("Code by c0yot3\n"
                  "\n\nFor best results, run in a program (like pycharm) that can process color code."
                  "\nWould you like to play a game of blackjack? (Y/N) ")
    if play is True:
        blackjack()
    else:
        print("Okay! Come back if you want to play a game!")


def choice(message):
    """Creates a True/False out of an input choice of yes or no."""
    choice_con = True
    while choice_con:
        try:
            yes_or_no = input(message).strip().lower()[0]
            if yes_or_no == "y":
                return True
            elif yes_or_no == "n":
                return False
            else:
                raise IndexError
        except IndexError:
            print("Please return yes or no.")


def blackjack():
    """Checks for win conditions and runs game."""
    playing = True
    print(logo)
    time.sleep(.5)
    player_hand = {}
    comp_hand = {}
    for _ in range(2):
        player_hand.update(select_card())
    comp_hand.update(select_card())
    while playing:
        player_total = print_hand(player_hand, "Your cards: ")
        if len(player_hand) == 2 and player_total == 21:    # Blackjack win condition, only two cards in the players
            comp_hand.update(select_card())                 # hand and score is equal to 21.
            print_hand(comp_hand, "Computer's hand: ")
            another_round("BLACKJACK! YOU WIN!!")
        else:
            print_hand(comp_hand, "Computer's first card: ")
            if player_total > 21:
                another_round("You bust! You lose this hand.")
            else:
                take_card = choice("Would you like another card?(Y/N) ")
                if take_card is True:
                    player_hand.update(select_card())
                else:
                    print_hand(player_hand, "Your cards: ")
                    time.sleep(.25)
                    comp_hand.update(select_card())
                    comp_turn = True
                    while comp_turn:                        # runs until the computer's turn is done.
                        comp_total = print_hand(comp_hand, "Computer's hand: ")
                        time.sleep(.25)
                        if len(comp_hand) == 2 and comp_total == 21:
                            another_round("The Dealer got Blackjack. You lose. . .")
                        elif comp_total > 21:
                            another_round("You win!")
                        elif comp_total < 17:
                            comp_hand.update(select_card())
                        elif comp_total > player_total:
                            another_round("You lose. . .")
                        elif comp_total == player_total:
                            another_round("It's a draw.")
                        else:
                            another_round("You win!")


def another_round(message):
    """Checks if the player wishes to play another round"""
    time.sleep(.5)
    play_again = choice(f"\n{message}\n\nWould you like to play again?(Y/N) ")
    if play_again is True:
        blackjack()
    else:
        print("\nThanks for playing!")
        exit(0)


def hit_21(hand):
    """If the hand is greater than 21, checks for an ace."""
    for hand_card in hand:
        if hand[hand_card] == 11:
            return hand_card
    return False


def print_hand(hand, message):
    """Prints out the hand and passes back the total score."""
    total_hand = message
    hand_count = 0
    for hand_card in hand:
        total_hand += hand_card + " "
        hand_count += hand[hand_card]
    if hand_count > 21:
        ace_card = hit_21(hand)
        if ace_card is not False:
            hand[ace_card] = 1
            hand_count = 0
            for hand_card in hand:
                hand_count += hand[hand_card]
    print(f"     {total_hand.strip()}, current score: {hand_count}")
    return hand_count


def select_card():
    """Adds a new card to the hand."""
    new_card_rand = random.randint(0, 12)
    new_card_face = next(iter(cards[new_card_rand]))
    new_card_val = cards[new_card_rand][new_card_face]
    new_card_suit = random.choice(suit)
    new_card_total = new_card_face + new_card_suit
    new_card = {new_card_total: new_card_val}
    return new_card


if __name__ == "__main__":
    main()
