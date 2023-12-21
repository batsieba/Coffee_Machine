# import
from sources import MENU, resources


def get_drink(drink):
    """function to import the drink details"""
    details = MENU[drink]
    return details


def print_resources():
    """function prints remaining resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return (f"Water : {water}ml \nMilk : {milk}ml \n"
            f"Coffee : {coffee}ml \nMoney: ${money}")


def calc_resources(drink):
    """updates the remaining resources"""
    resources["water"] -= drink["water"]
    resources["coffee"] -= drink["coffee"]
    if "milk" in drink:
        resources["milk"] -= drink["milk"]
    print("Remaining resources have been updated🍵")


def suffecient_resources(drink):
    if "milk" in drink:
        if drink["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
        elif drink["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        elif drink["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    else:
        if drink["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        elif drink["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True


def process_coin():
    """Calculates how much money a user have after inserting coins"""
    print("Insert Coins!")
    quarter = int(input("Insert quarters: "))
    dime = int(input("Insert dimes: "))
    nickle = int(input("Insert nickle: "))
    pennies = int(input("Inset pennies: "))

    total = (quarter*0.25) + (dime*0.1) + (nickle*0.05) + (pennies*0.01)
    return total


def process_payment(inserted, cost):
    """this function will process if inserted coin will be enough to buy the drink"""
    if inserted >= cost:
        resources["money"] += cost
        change = inserted - cost
        change = round(change,2)
        return f"The cost was ${cost}. You have ${change} change. Enjoy your drink"
    elif inserted < cost:
        return f"The cost was ${cost}. Sorry that's not enough money. Money refunded."


def coffee_machine():
    """this functions as a coffee machine"""
    resources["money"] = 0
    should_continue = True
    while should_continue:
        # print(print_resources())
        choice = input("What would you like? (espresso/ latte/ cappuccino): ").lower()

        if choice == "off":
            # Clearing the Screen
            print("Coffee Machine turning off")
            should_continue = False
        elif choice == "report":
            print(print_resources())
        else:
            drink_ingr = get_drink(choice)["ingredients"]
            if suffecient_resources(drink_ingr):
                calc_resources(drink_ingr)
                coins = process_coin()
                print(f"You have inserted ${coins}")
                drink_price = get_drink(choice)["cost"]
                print(process_payment(coins,drink_price))
            else:
                should_continue =False
            # print(print_resources())


coffee_machine()