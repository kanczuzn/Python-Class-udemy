from art import logo
from os import system as sys
from os import name as sysname

Auctions = []
auc_check_ls = ['y', 'n', 'yes', 'no']


def main():
    run_auction = True
    while run_auction:
        clear()
        print(logo)
        menu_options = [1, 2, 3, 4]
        menu_response = 0
        while menu_response not in menu_options:
            try:
                menu_response = int(input("Which option would you like to choose:"
                                          "\n1 - Add a new auction lot."
                                          "\n2 - Add a bid to an auction lot."
                                          "\n3 - End an auction and view a winner."
                                          "\n4 - End program\n"))
                if menu_response not in menu_options:
                    raise ValueError
            except ValueError:
                menu_response = 0
                print("Please input a valid option.\n")

        if menu_response == 1:
            auction_add()
        elif menu_response == 2:
            auction_bid()
        elif menu_response == 3:
            auction_end()
        else:
            run_auction = False


def clear():
    sys('cls' if sysname == 'nt' else 'clear')


def auction_add():
    auc_next = True
    while auc_next:
        clear()
        name = ""
        while name == "":
            name = input("\nWhat new item would you like to add to the auction?\n").strip().title()
        print(f"\n{name} added to the list of auctions!\n")
        new_auction = {"Item": name, "Bids": {}}
        Auctions.append(new_auction)
        auc_next = check("Would you like to add another item? (Yes/No)\n")


def check(message):
    auc_check = 0
    while auc_check not in auc_check_ls:
        auc_check = input(message).lower()
    if auc_check == "n" or auc_check == "no":
        return False
    else:
        return True


def auction_bid():
    auc_choice = auction_choices("bid on")
    auc_next = True
    if auc_choice > -1:
        while auc_next:
            clear()
            name = ""
            print(f"Bidding on item: {Auctions[auc_choice]['Item']}")
            while name == "":
                name = input("\nWhat is your name?\n").strip()
            try:
                bid = int(input("What is your bid?\n$"))
            except ValueError:
                bid = "Invalid"
                while isinstance(bid, int) is False:
                    print("That is not a valid number, please try again.")
                    try:
                        bid = int(input("How much would you like to bid?\n$"))
                    except ValueError:
                        continue
            Auctions[auc_choice]["Bids"][name] = bid
            auc_next = check("Would you like to add another bidder? (Yes/No)\n")


def auction_end():
    auc_end = True
    while auc_end:
        auc_choice = auction_choices("end")
        if auc_choice > -1:
            highest = 0
            name = ""
            right_auc = check("Is this the correct auction? (Yes/No)"
                              f"\n{Auctions[auc_choice]['Item']}"
                              "\n___________________\n")
            if right_auc is True:
                for entry in Auctions[auc_choice]['Bids']:
                    if Auctions[auc_choice]['Bids'][entry] > highest:
                        name = entry
                        highest = Auctions[auc_choice]['Bids'][entry]
                clear()
                print(f"The winner is {name}, with a bid of ${highest:,}\n")
                Auctions.pop(auc_choice)
                auc_end = False
                input("\n\nPress enter to continue...")
            elif right_auc is False:
                right_auc = check("Do you still want to end an auction? (Yes/No)\n")
                if right_auc is False:
                    auc_end = False


def auction_choices(choice_typ):
    clear()
    auc_choice = -1
    auc_options = []
    if len(Auctions) < 1:
        print(f"\nThere are no auctions to {choice_typ}!\n")
        input("\n\nPress enter to continue...")
    else:
        print("Please select one of these options:\n")
        for i, k in enumerate(Auctions):
            auc_options.append(i + 1)
            print(f"{i + 1} -- {Auctions[i]['Item']}")
        auc_choice = int(input(f"\nWhich Auction would you like to {choice_typ}?\n"))
        while auc_choice not in auc_options:
            auc_choice = int(input("That choice is invalid. Please try again.\n"))
        auc_choice -= 1
    return auc_choice


if __name__ == "__main__":
    main()
