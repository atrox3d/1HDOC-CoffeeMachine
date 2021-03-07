# renamed github repo to 1hdoc-CoffeeMachine
import data


def is_resource_sufficient(order_ingredients):
    """return True when order can be made, False if ingredients are insufficient"""
    # print(type(data.resources))
    # print(data.resources)
    for resource_name, drink_quantity in order_ingredients.items():
        if drink_quantity >= data.resources[resource_name]:
            print(f"Sorry, there is not enough {resource_name}.")
            return False
        return True


def process_coins():
    """return the total calculated from the coins inserted"""
    print("Please insert coins.")
    total = int(input("How manu quarters?: ")) * 0.25
    total += int(input("How manu dimes?: ")) * 0.1
    total += int(input("How manu nickels?: ")) * 0.05
    total += int(input("How manu pennies?: ")) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """returns true if payment is accepted or false if not sufficient"""
    global profit

    if money_received >= drink_cost:
        change = round(money_received- drink_cost, 2)
        print(f"Here is ${change} in change")
        profit += payment
        return True
    else:
        print("Sorry that's not enough money, money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    print(type(order_ingredients), order_ingredients)
    for ingredient, quantity in order_ingredients.items():
        data.resources[ingredient] -= quantity
    print(f"Here's your {drink_name}, enjoy")


profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("shutting down...")
        is_on = False
    elif choice == "report":
        print(f"Water:  {data.resources['water']}ml")
        print(f"Milk:   {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money:  ${profit}")
    else:
        drink = data.MENU[choice]
        print(drink)
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            print(f"${payment}")
            if is_transaction_succesful(payment, data.MENU[choice]["cost"]):
                print("ok")
                make_coffee(choice, data.MENU[choice]['ingredients'])
            else:
                print("poor")


