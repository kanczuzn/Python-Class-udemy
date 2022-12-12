def main():
    print(usr_choice("Testing ", "#num# +"))
    print(usr_choice("Testing ", "#num# -"))
    print(usr_choice("Testing ", "#num# +-"))
    print(usr_choice("Testing ", "#num# asldkfh"))


def usr_choice(message, choices):
    """usr_choice(message, choices) where message should be the message displayed to the user,
    and choices is what choices you want the user to input.

    Takes user input, sets to lower case, and strips of leading/trailing whitespace.
    If it matches a character in the choices, return the choice. If not, raises an IndexError.
    Index error because just hitting 'enter' will result in this as well, making it the most
    common error to try and catch.

    Choices should be a string of lowercase characters or numbers, or a list of words
    separated by spaces. If Choices is #num# then it expects a number.
    '#num# +' expects a positive number.'
    '#num# -' expects a negative number.
    '#num# +-' will accept either positive or negative.
    if the item starts with then it will be hidden, this is only for a list broken by spaces.
    For instance:
    '*report, *off, itema, itemb' report and off will be hidden from the user."""
    check = False
    while check is False:
        choices.strip()
        if choices.find(" ") > 0:
            choices_lst = choices.split()
        else:
            choices_lst = list(choices)
        error_choices = ""
        if choices_lst[0] != "#num#":
            try:
                check = input(message).strip().lower()
                for choice in choices_lst:
                    if choice == check or choice == "*"+check:
                        return check
                raise IndexError
            except (IndexError or UnboundLocalError):
                for choice in choices_lst:
                    if choice[0] != "*":
                        error_choices += f"{choice}, "
                error_choices = error_choices[:-2]
                print(f"Please select one of these choices: {error_choices}.")
                check = False
        else:
            try:
                check = int(input(message).strip())
                if choices_lst[1] == "+-":
                    return check
                elif choices_lst[1] == "+":
                    if check >= 0:
                        return check
                    else:
                        print("Please input a positive integer.")
                elif choices_lst[1] == "-":
                    if check <= 0:
                        return check
                    else:
                        print("Please input a negative integer.")
                else:
                    print("usr_choices syntax error")
                    exit(1)
                check = False
            except ValueError:
                print(f"Please input a valid integer.")
                check = False


if __name__ == "__main__":
    main()