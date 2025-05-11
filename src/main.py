from drink import Drink, CinosDrinkMenu
from hungry_hungry_students import Food, CinosFoodMenu
from order import Order

if __name__ == "__main__":
    order = Order()
    print("Welcome to Cinos Drive-Up! Let's start your drink order.")

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
        print("Drink added to your order!")
        print(order.get_receipt())

    # Food ordering section
    while True:
        print("Available food items:")
        for i, item in enumerate(CinosFoodMenu.food_options, 1):
            print(f"  {i}. {item} - ${CinosFoodMenu.food_options[item]:.2f}")
        food_index = input("Choose a food by number (or type 'done' to finish): ").lower()
        if food_index == 'done':
            break
        if not food_index.isdigit() or not 1 <= int(food_index) <= len(CinosFoodMenu.food_options):
            print("Invalid food choice. Please enter a valid number.")
            continue
        food_name = list(CinosFoodMenu.food_options.keys())[int(food_index) - 1]

        try:
            food_item = Food(food_name)
        except ValueError as e:
            print(e)
            continue

        print("Available toppings:")
        for i, topping in enumerate(CinosFoodMenu.toppings, 1):
            print(f"  {i}. {topping} - ${CinosFoodMenu.toppings[topping]:.2f}")
        while True:
            topping_index = input("Add a topping by number (or type 'done' when finished): ").lower()
            if topping_index == 'done':
                break
            if not topping_index.isdigit() or not 1 <= int(topping_index) <= len(CinosFoodMenu.toppings):
                print("Invalid topping choice. Please enter a valid number.")
                continue
            topping = list(CinosFoodMenu.toppings.keys())[int(topping_index) - 1]
            try:
                food_item.add_topping(topping)
            except ValueError as e:
                print(e)

        order.add_item(food_item)
        print("Food item added to your order!")
        print(order.get_receipt())