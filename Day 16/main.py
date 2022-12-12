from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
coffee_money = MoneyMachine()


def main():
    machine_on = True
    while machine_on:
        order = input(f"What would you like? ({coffee_menu.get_items()}): ")
        if order == "off":
            machine_on = False
        elif order == "report":
            coffee_maker.report()
            coffee_money.report()
        else:
            order = coffee_menu.find_drink(order)
            if order is not None:
                if coffee_maker.is_resource_sufficient(order) and coffee_money.make_payment(order.cost):
                    coffee_maker.make_coffee(order)


if __name__ == "__main__":
    main()
