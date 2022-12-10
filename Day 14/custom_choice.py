def main():
    print(usr_choice("Testing ","abcdefghij12345"))

def usr_choice(message, choices):
    """Takes user input, sets to lower case, strips of leading/trailing whitespace,
    and grabs the first character. If it matches a character in the choices,
    return the choice. If not, raises an IndexError. Index error
    because just hitting 'enter' will result in this as well, making it the most
    common error to try and catch.

    Choices should be a string of lowercase characters or numbers."""
    check = False
    while check is False:
        choices_lst = list(choices)
        error_choices = ""
        try:
            check = input(message).strip().lower()[0]
            for choice in choices_lst:
                if choice == check:
                    return choice
            raise IndexError
        except (IndexError or UnboundLocalError):
            for choice in choices_lst:
                error_choices += f"{choice}, "
            error_choices = error_choices[:-2]
            print(f"Please select one of these choices: {error_choices}.")
            check = False


if __name__ == "__main__":
    main()