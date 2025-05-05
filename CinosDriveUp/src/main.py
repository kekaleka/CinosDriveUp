from order import Order
from drink import Drink, CinosDrinkMenu

# Interactive terminal-based order system
if __name__ == "__main__":
    order = Order()
    print("Welcome to Cinos Drive-Up! Let's start your drink order.\n")

    while True:
        print("Available drinks:")
        for i, drink in enumerate(CinosDrinkMenu.drink_options, 1):
            print(f"  {i}. {drink}")
        base_index = input("Choose a drink by number (or type 'done' to finish): ").lower()
        if base_index == 'done':
            break
        if not base_index.isdigit() or not 1 <= int(base_index) <= len(CinosDrinkMenu.drink_options):
            print("Invalid drink choice. Please enter a valid number.")
            continue
        base = CinosDrinkMenu.drink_options[int(base_index) - 1]

        print("Available sizes:")
        size_keys = list(Drink.size_prices.keys())
        for i, size in enumerate(size_keys, 1):
            print(f"  {i}. {size}")
        size_index = input("Choose a size by number: ").lower()
        if not size_index.isdigit() or not 1 <= int(size_index) <= len(size_keys):
            print("Invalid size choice. Please enter a valid number.")
            continue
        size = size_keys[int(size_index) - 1]

        try:
            drink = Drink(base, size)
        except ValueError as e:
            print(e)
            continue

        print("Available flavors:")
        for i, flavor in enumerate(CinosDrinkMenu.drink_flavors, 1):
            print(f"  {i}. {flavor}")
        while True:
            flavor_index = input("Add a flavor by number (or type 'done' when finished): ").lower()
            if flavor_index == 'done':
                break
            if not flavor_index.isdigit() or not 1 <= int(flavor_index) <= len(CinosDrinkMenu.drink_flavors):
                print("Invalid flavor choice. Please enter a valid number.")
                continue
            flavor = CinosDrinkMenu.drink_flavors[int(flavor_index) - 1]
            try:
                drink.add_flavor(flavor)
            except ValueError as e:
                print(e)

        order.add_item(drink)
        print("Drink added to your order!\n")

    print(order.get_receipt())