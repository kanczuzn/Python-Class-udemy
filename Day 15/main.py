from custom_choice import usr_choice
from ast import literal_eval
from time import sleep
from os import system as sys
from os import name as sysname


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


COINS = {
    "quarter": .25,
    "dime": .10,
    "nickel": .05,
    "penny": .01,
}


def clear():
    sys('cls' if sysname == 'nt' else 'clear')


def main():
    with open("resources.txt", "r") as file_read:
        if file_read.read(1):
            resources = literal_eval(open("resources.txt", "r").read())
        else:
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
                "quarter": 0,
                "dime": 0,
                "nickel": 0,
                "penny": 0,
            }
    machine_on = True
    while machine_on:
        clear()
        option = usr_choice("What would you like? (espresso/latte/cappuccino): ",
                            "espresso latte cappuccino *off *report")
        if option == "off":
            machine_on = machine_off(resources)
        elif option == "report":
            machine_report(resources)
        else:
            resources = coffee_start(resources, option)


def coffee_start(resources, option):
    coffee_cont = check_resources(resources, option)
    while coffee_cont is not True:
        print(f"There's not enough {coffee_cont}, please add more.")
        fix_choice = usr_choice("Would you like to add more? (Y/N) ", "yn")
        if fix_choice == "y":
            fix_choice = usr_choice("How much would you like to add? ", "#num# +")
            resources[coffee_cont] += fix_choice
        else:
            return resources
        coffee_cont = check_resources(resources, option)
    coffee_cont, resources = process_coins(resources, option)
    if coffee_cont is True:
        make_coffee(resources, option)
    elif coffee_cont == "M":
        coffee_start(resources, option)
    return resources


def process_coins(resources, option):
    choice = ""
    change_list = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
    print("Please insert coins.")
    change_list['quarter'] = usr_choice("How many quarters? ", "#num# +")
    change_list['dime'] = usr_choice("How many dimes? ", "#num# +")
    change_list['nickel'] = usr_choice("How many nickels? ", "#num# +")
    change_list['penny'] = usr_choice("How many pennies? ", "#num# +")
    money = (change_list['quarter'] * COINS['quarter'] + change_list['dime'] * COINS['dime'] +
             change_list['nickel'] * COINS['nickel'] + change_list['penny'] * COINS['penny'])
    if money < MENU[option]['cost']:
        clear()
        print(f"Return: ${money:.2f}"
              f"\n{change_list['quarter']} quarters, {change_list['dime']} dimes, "
              f"{change_list['nickel']} nickels, {change_list['penny']} pennies.")
        print(f"That wasn't enough money. A {option.title()} is ${MENU[option]['cost']:.2f}.")
        choice = usr_choice("Would you like to order something different? (Y/N) ", "yn")
        if choice == "n":
            return "M", resources
        else:
            return False, resources
    else:
        money = round(money - MENU[option]['cost'], 2)
        for coin in change_list:
            resources[coin] += change_list[coin]
    print("WHY?!")
    if money > 0:
        finished, resources = process_chng(resources, money)
        if finished is False:
            for coin in change_list:
                resources[coin] -= change_list[coin]
            clear()
            print(f"Return: ${money:.2f}"
                  f"\n{change_list['quarter']} quarters, {change_list['dime']} dimes, "
                  f"{change_list['nickel']} nickels, {change_list['penny']} pennies."
                  f"\nNot enough change in the machine.\n")
            input()
            return False, resources
        return True, resources
    else:
        return True, resources


def make_coffee(resources, option):
    for item in MENU[option]['ingredients']:
        resources[item] -= MENU[option]['ingredients'][item]
    print(f"\n\nHere is your {option.lower()}. ☕ Enjoy!")
    sleep(4)
    return resources


def process_chng(resources, money):
    orig_money = money
    change_list = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
    for coin in change_list:
        if money > 0:
            change_list[coin] = int(money / COINS[coin])
            if change_list[coin] >= resources[coin]:
                change_list[coin] = resources[coin]
            resources[coin] -= change_list[coin]
            if resources[coin] >= 0:
                money = round(money - change_list[coin] * COINS[coin],2)
    if money == 0:
        clear()
        print(f"Dispense change for ${orig_money:.2f}:")
        for coin in change_list:
            print(f"{coin}: {change_list[coin]}")
        return True, resources
    for coin in change_list:
        resources[coin] += change_list[coin]
    return False, resources


def check_resources(resources, option):
    for opt_res, amt in MENU[option]['ingredients'].items():
        if resources[opt_res] < amt:
            return opt_res
    return True


def machine_off(resources):
    with open("resources.txt", "w") as file_write:
        file_write.write(str(resources))
    return False


def machine_report(resources):
    money = 0
    for x in range(4):
        clear()
        print("Checking " + "."*x)
        sleep(.5)
    clear()
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    for coin in COINS:
        print(f"{coin.title()}: {resources[coin]}")
        money += resources[coin] * COINS[coin]
    money = f'${(money):.2f}'
    print(f"Money: {money}\n")
    input("Press enter to continue...")


if __name__ == "__main__":
    main()
