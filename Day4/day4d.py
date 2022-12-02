rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game_RPS = [rock,paper,scissors]
game = 1
tie = 0
win = 0
loss = 0
while game == 1:
    player_RPS = -1
    while player_RPS == -1:
        player_RPS = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
        if player_RPS < 0 or player_RPS > 2:
            player_RPS = -1
            print("Please select 0, 1, or 2.")
    comp_RPS = random.randint(0,2)
    print(game_RPS[player_RPS])
    print(f"Computer chose:{game_RPS[comp_RPS]}")

    if player_RPS - comp_RPS == 0:
        print("It's a tie.")
        tie += 1
        #tie
    elif player_RPS - comp_RPS == 1 or player_RPS - comp_RPS == -2:
        print("You win!")
        win += 1
        #win
    else:
        print("You lose. D:")
        loss += 1
        #loss
    keep_playing = input("\nWould you like to play again? Y/N\n").lower()[0]
    if keep_playing != "y":
        print("\nThanks for playing!"
              f"\nYou won a total of: {win} times"
              f"\nYou lost a total of: {loss} times"
              f"\nYou tied a total of: {tie} times")
        game = 0
    else:
        print("\nOK! Let's go again!\n")