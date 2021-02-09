import data

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



