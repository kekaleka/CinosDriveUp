from drink import Drink, CinosDrinkMenu
from order import Order
# Cinos Drive-Up Beverage Service
# This script simulates a simple beverage ordering system.
# It allows users to choose drinks and flavors, place an order, and receive a receipt.
def main():
    print("Welcome to Cinos Drive-Up Beverage Service!")
    print("Available Drinks:")
    print(", ".join(CinosDrinkMenu.drink_options))

    print("\nAvailable Flavors:")
    print(", ".join(CinosDrinkMenu.drink_flavors))

    print("\nLet's place a sample order for you...\n")

    drink1 = Drink("water")
    drink1.add_flavor("lemon")

    drink2 = Drink("iced coffee")
    drink2.add_flavor("cherry")

    order = Order()
    order.add_item(drink1)
    order.add_item(drink2)

    print("\nYour order has been placed! Here is your receipt:\n")
    print(order.get_receipt())

if __name__ == "__main__":
    main()