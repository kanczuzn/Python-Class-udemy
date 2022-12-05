print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
game_on = 0
start = 0
location = 0
key = 0
name = ""
art = 0

while game_on == 0:
    match location:
        case -2:
            rst = input("\nWould you like to start over? Yes/No ").lower()
            if rst == "y" or rst == "yes":
                print("\n\nWith a swirl of lights you find yourself reborn.\n")
                print('''
                       .       . 
                     +  :      .
                               :       _
                           .   !   \'  (_)
                              ,|.\' 
                    -  -- ---(-O-`--- --  -
                             ,`|\'`.
                           ,   !    .
                               :       :  " 
                               .     --+--
                     .:        .       !

                    ''')
                location = 0
                start = 0
            else:
                print("\n\nThank you for playing!")
                game_on = 1
        case 0:
            if start == 0:
                key = 0
                rst = "*"
                start += 1
                name = input("\nYour adventure begins! \nWhat's your name? ")
                if name == "":
                    name = "Unknown Hero"
                print(f"\nWelcome {name}. Best of luck, try not to die!\n")
            print("\nYou are near the edge of a forest, you can see a lake off to the left, and a hill to the right.")
            direction = input("Would you like to go left or right? ").lower()
            if direction == "left":
                location += 1
            elif direction == "right":
                location -= 1
            else:
                print("\nYou can't do that...")
        case -1:
            print("\nYou see a spooky cave at the base of the hill and key on the ground.")
            direction = input("Would you like to go left? ").lower()
            if direction == "get key":
                if key == 1:
                    print("\nYou already picked up the key.")
                else:
                    print("\nYou pick up the key!")
                    print(''' 
                      ooo,    .---.
                     o`  o   /    |\\________________
                    o`   \'oooo()  | ________   _   _)
                    `oo   o` \\    |/        | | | |
                      `ooo\'   `---\'         "-" |_|
                    ''')
                    key = 1
            elif direction == "yes" or direction == "left":
                location += 1
            else:
                print("\nYou can't do that...")
        case 1:
            if art == 0:
                print('''
                                         |
                                       \\ _ /
                                     -= (_) =-
    .\\/.                               /   \\
 .\\\\//o\\\\                      ,\\/.      |              ,~
 //o\\\\|,\\/.   ,.,.,   ,\\/.  ,\\//o\\\\                     |\\
   |  |//o\\  /###/#\\  //o\\  /o\\\\|                      /| \\
 ^^|^^|^~|^^^|\' \'|:|^^^|^^^^^|^^|^^^""""""""("~~~~~~~~/_|__\\~~~~~~~~~~
  .|\'\' . |  \'\'\'""\'"\'\'. |`===`|\'\'  \'"" "" " (" ~~~~ ~ ~======~~  ~~ ~
  jgs^^   ^^^ ^ ^^^ ^^^^ ^^^ ^^ ^^ "" """( " ~~~~~~ ~~~~~  ~~~ ~
                ''')
                art = 1
            print("\nYou are near the edge of a lake. A rickety rowboat is nearby."
                  "\nYou see an island out in the middle of the lake. Maybe you can swim to it."
                  "\nYou can always go back to the right, where you started.")
            direction = input("What would you like to do? ").lower()
            if direction == "right" or direction == "go back":
                location -= 1
                art = 0
            elif direction == "swim":
                print("\nYou begin to swim out into the lake. It looked a lot closer from land...")
                location = 2
                art = 0
            elif direction == "use boat":
                print("\nYou push the rickety boat out into the water. It starts to leak...")
                location = 3
                art = 0
            elif direction == "wait" or direction == "boatman" or direction == "wait for boatman":
                print("\nYou wait around on the shore, looking around for any other option."
                      "\nAfter a bit of time, you see a boatman. He waves to you and offers a ride to the island.")
                location = 5
                art = 0
            elif direction == "unicorn":
                print("\nWho do you think you are? Arpy? Wait... is that you Arpy?"
                      "\nWell, sure. Have a unicorn. It flies down all shimmery and carries you off to the island."
                      "\nIt neighs a few times and tosses its epic mane."
                      "\nSeriously. It's hair is glorious with glitter and everything.")
                location = 6
                art = 0
            else:
                print("\nYou can't do that...")
        case 2:
            direction = input("\nDo you want to keep going? You can always go back. ").lower()
            if direction == "back" or direction == "go back":
                location -= 1
            elif direction == "keep going" or direction == "swim":
                print("\nYou keep trying to swim toward the island and soon grow tired. With a blurble... you drown.")
                location = -2
            elif direction == "stay" or direction == "think":
                print("\nYou don't think this is the wisest course... maybe you should go back.")
            else:
                print("\nYou can't do that...")
        case 3:
            direction = input("What would you like to do? ").lower()
            if direction == "stop leak" or direction == "plug leak":
                print("\nYou spend a bit of time plugging the leak. Phew... let's get back to rowing."
                      "\nYou get closer to the island, but your boat sinks. Oh no!")
                location = 4
            elif direction == "keep rowing" or direction == "keep going":
                print("\nYou keep paddling as quickly as you can, your arms tiring out and soon your boat sinks."
                      "\nTry as you might... you drown. D:")
                location = -2
            elif direction == "swim" or direction == "swim to island":
                print("\nYou start trying to swim to the island, but your arms are already a bit tired.")
                location = 2
            else:
                print("\nYou can't do that...")
        case 4:
            direction = input("What would you like to do? ").lower()
            if direction == "go back" or direction == "back":
                print("\nYou keep paddling as quickly as you can, your arms tiring out and soon your boat sinks."
                      "\nTry as you might... you drown. D:")
                location = -2
            elif direction == "swim" or direction == "swim to island":
                print("\nCoughing and spluttering you swim your way to the island."
                      "\nYou barely pull yourself up onto the island's shore, catching your breath.")
                location = 6
            elif direction == "call for help" or direction == "help":
                print("\nYou call out for help! Waving your arms, and luckily a boatman picks you up!!")
                location = 5
            else:
                print("\nYou can't do that...")
        case 5:
            print("\nThe boatman yammers at you while taking you to the island. Telling you of tough times."
                  "\n...It's incredibly boring...")
            location = 6
        case 6:
            if art == 0:
                print('''                                                   .       .
                                                    \\     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \\
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~''')
                art = 1
            print("\nYou stand on the beach of the island. It's peaceful. Ahead is a cave."
                  "\nA boatman is on the island, whistling as he tends to his boat.")
            direction = input("Would you like go to the cave or take the boat back? ").lower()
            if direction == "back" or direction == "take the boat" or \
                    direction == "boatman" or direction == "take the boatman":
                print("\nYou clamour back on the boat for a very boring boat ride."
                      "\nSeriously..."
                      "\nIt's INCREDIBLY boring.")
                location = 1
                art = 0
            elif direction == "cave" or direction == "go cave" or direction == "go to cave":
                print("\nYou head into the cave. It's cold and damp, but as you travel further in-- "
                      "\n                   You see a chest!\n")
                location = 7
                art = 0
            else:
                print("\nYou can't do that...")
        case 7:
            direction = input("What would you like to do? ").lower()
            if direction == "open chest":
                if key == 1:
                    print("\nYou open the chest!! Congratulations! You've won!!!"
                          f"\n\nGOOD JOB {name.upper()}!!!")
                    print('''
                                                       .\'\'.       
                           .\'\'.      .        *\'\'*    :_\\/_:     . 
                          :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .\'.:.\'.
                      .\'\'.: /\\ :   ./)\\   \':\'* /\\ * :  \'..\'.  -=:o:=-
                     :_\\/_:\'.:::.    \' *\'\'*    * \'.\\\'/.\' _\\(/_\'.\':\'.\'
                     : /\\ : :::::     *_\\/_*     -= o =-  /)\\    \'  *
                      \'..\'  \':::\'     * /\\ *     .\'/.\\\'.   \'
                          *            *..*         :
                    jgs     *
                            *
                    ''')
                    game_on = 1
                else:
                    print("\nHrm... you don't seem to have the key...")
            elif direction == "go back" or direction == "back" or direction == "beach":
                print("\nYou head back to the beach.")
                location = 6
            else:
                print("\nYou can't do that...")
        case _:
            print("Woops! Not sure how you got here... Let's take you back to the start.")
            location = 0
