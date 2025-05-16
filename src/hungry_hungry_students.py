class CinosFoodMenu:
    """
    This is the main list of food items and prices offered at Cinos.

    """
    food_options = {
        "Hotdog": 2.30,
        "Corndog": 2.00,
        "Ice Cream": 3.00,
        "Onion Rings": 1.75,
        "French Fries": 1.50,
        "Tater Tots": 1.70,
        "Nacho Chips": 1.90
    }

    food_toppings = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Nacho Cheese": 0.30,
        "Chili": 0.60,
        "Bacon Bits": 0.30,
        "Ketchup": 0.00,
        "Mustard": 0.00
    }

class Food:
    """
    This class builds a single food item for the order.
    It checks if the item is on the menu and provides access to the name, toppings, and price.
    """
    def __init__(self, name):
        if name not in CinosFoodMenu.food_options:
            raise ValueError(f"'{name}' is not on the food menu.")
        self.__name = name
        self.__price = CinosFoodMenu.food_options[name]
        self.__toppings = []

    
    def get_food_name(self):
        """Return the name of the food item."""
        return self.__name
    
    def get_toppings(self):
        """Return a list of all toppings added to the food item."""
        return list(self.__toppings)

    def get_topping_price(self):
        """Calculate the total price for all toppings added."""
        return sum(CinosFoodMenu.toppings[t] for t in self.__toppings)

    def add_topping(self, topping):
        """Add a topping if it's valid and not already added."""
        if topping not in CinosFoodMenu.toppings:
            raise ValueError(f"'{topping}' is not a valid topping.")
        if topping not in self.__toppings:
            self.__toppings.append(topping)

    def get_total(self):
        return self.__price + self.get_topping_price()
    
    def __str__(self):
        """Return a string representation of the food item with toppings and total price."""
        toppings_str = ', '.join(self.__toppings) if self.__toppings else "No toppings"
        return f"{self.__name} with {toppings_str} - ${self.get_total():.2f}"