from art import logo


# Calculator

# Add
def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2


def sub(n1, n2):
    """Subtracts two numbers."""
    return n1 - n2


def mult(n1, n2):
    """Multiplies two numbers."""
    return n1 * n2


def div(n1, n2):
    """Divides two numbers."""
    return n1 / n2


def power(n1, n2):
    """The first number to the power of the second"""
    return n1 ** n2


Operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "^": power,
}


usr_input = ['y', 'n']


def main():
    use_res = False
    answer = 0
    num1 = 0
    num2 = 0
    user_op = 0
    calc_ck = True
    while calc_ck:
        usr_enter = True
        while usr_enter:
            try:
                if use_res:
                    num1 = answer
                else:
                    num1 = float(input("What's the first number? "))
                print("\nPlease select an operation from below:")
                for keys in Operations:
                    print(keys)
                user_op = input("Which of the above operations would you like to use? ")
                while user_op not in Operations:
                    user_op = input("Please select a valid operation: ")
                num2 = float(input("What's the second number? "))
                if num1 == "" or num2 == "":
                    raise ValueError
                else:
                    usr_enter = False
            except ValueError:
                print("Please select a valid number.")
        calculation_func = Operations[user_op]
        answer = calculation_func(num1, num2)
        print(f"{num1} {user_op} {num2} = {answer}")
        print("Would you like to continue?")
        calc_ck = choice()
        if calc_ck:
            print(f"Would you like to use {answer} in the next operation?")
            use_res = choice()
        else:
            return calc_ck


def choice():
    choices = ""
    choice_check = True
    while choice_check:
        try:
            choices = input("(Yes/No) ").strip().lower()[0]
            if choice not in usr_input:
                raise IndexError
            else:
                choice_check = False
        except IndexError:
            print("That's not a valid choice. Please try again.")
    if choices == "y":
        return True
    else:
        return False


if __name__ == "__main__":
    print(logo)
    calc_on = True
    while calc_on:
        calc_on = main()
