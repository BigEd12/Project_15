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
            "milk": 200,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}
game = True

def report():
    """Prints a statement of remaining resources in the machine"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def sufficient_resources(drink):
    """Checks if there are enough resources to make the drink"""
    if drink == "espresso":
        if not resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        elif not resources["water"] >= MENU[drink]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        else:
            return True
    elif drink == "latte" or "capuccino":
        if not resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        elif not resources["water"] >= MENU[drink]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif not resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        else:
            return True



def process_coins(amount, coin):
    if coin == "quarters":
        cash = amount * 0.25
        return cash
    elif coin == "dimes":
        cash = amount * 0.10
        return cash
    elif coin == "nickels":
        cash = amount * 0.05
        return cash
    elif coin == "pennies":
        cash = amount * 0.01
        return cash


def total_amount_entered(q, d, n, p, drink):
    cash = q + d + n + p
    if cash < MENU[drink]["cost"]:
        print("You haven't got enough money. Go away.")
    else:
        change = cash - MENU[drink]["cost"]
        print(f"Here is your change: ${change}.\nHere is your {drink}. Enjoy!")


def affect_resources(drink):
    if drink == "espresso":
        change_in_cash = MENU[drink]["cost"]
        change_in_coffee = MENU[drink]["ingredients"]["coffee"]
        change_in_water = MENU[drink]["ingredients"]["water"]
        resources["money"] = resources["money"] + change_in_cash
        resources["coffee"] = resources["coffee"] - change_in_coffee
        resources["water"] = resources["water"] - change_in_water
    else:
        change_in_cash = MENU[drink]["cost"]
        change_in_coffee = MENU[drink]["ingredients"]["coffee"]
        change_in_water = MENU[drink]["ingredients"]["water"]
        change_in_milk = MENU[drink]["ingredients"]["milk"]
        resources["money"] = resources["money"] + change_in_cash
        resources["coffee"] = resources["coffee"] - change_in_coffee
        resources["water"] = resources["water"] - change_in_water
        resources["milk"] = resources["milk"] - change_in_milk


while game:
    question = input("What would you like? (espresso/latte/cappuccino): ")
    if question == "off":
        game = False
    elif question == "report":
        report()
    else:
        if sufficient_resources(question):
            quarters = int(input("Please insert coins.\nHow many quarters: "))
            first_coin = process_coins(quarters, "quarters")
            dimes = int(input("How many dimes: "))
            second_coin = process_coins(dimes, "dimes")
            nickels = int(input("How many nickels: "))
            third_coin = process_coins(nickels, "nickels")
            pennies = int(input("How many pennies: "))
            fourth_coin = process_coins(pennies, "pennies")
            total_amount_entered(first_coin, second_coin, third_coin, fourth_coin, question)
            affect_resources(question)


# TODO 1 insert a while loop

# TODO 2 Insert an off command



