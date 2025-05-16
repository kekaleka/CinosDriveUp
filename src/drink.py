# Cinos Drink Menu
# This class contains the available drink options and flavors for the Cinos Drive-Up Beverage Service.
class CinosDrinkMenu:
    """
    This is the main list of drinks and flavors we offer at Cinos.
    We write it once here so we don't have to keep repeating it everywhere else.
    """
    drink_options = ["water", "iced coffee", "iced tea", "juice", "soda", "sprite", "coke", "pepsi", "fanta", "redbull"]
    drink_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]

class Drink:
    """
    This class builds a single drink for the order.
    You have to choose a valid base (like soda or tea) and a size (like small or mega).
    The cost of the drink depends on the size and how many flavors you add to it.
    """
    size_prices = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }

    def __init__(self, base, size):
        if base not in CinosDrinkMenu.drink_options:
            raise ValueError(f"Sorry, '{base}' is not on our menu. Please choose from {CinosDrinkMenu.drink_options}.")
        if size.lower() not in Drink.size_prices:
            raise ValueError(f"Sorry, '{size}' is not a valid size. Please choose from {list(Drink.size_prices.keys())}.")
        self.__base = base
        self.__size = size.lower()  # Stores the size for pricing and display
        self.__flavors = []

    def get_drink_base(self):
            """Return the base (type) of the drink."""
            return self.__base
    
    def get_drink_flavors(self):
            """Return a list of all flavors added to the drink."""
            return list(self.__flavors)
    
    def get_num_flavors(self):
            """Return the number of flavors currently in the drink."""
            return len(self.__flavors)
    
    def get_size(self):
            """Return the current size of the drink."""
            return self.__size
    
    def set_size(self, size):
            """Update the size of the drink if it's a valid size."""
            size = size.lower()
            if size in Drink.size_prices:
                self.__size = size
            else:
                raise ValueError("That size isn't on the menu!")

    def get_flavor_price(self):
        """Returns the total cost of all added flavors."""
        return len(self.__flavors) * 0.15

    def get_total(self):
        """Return the total price of the drink including base and flavor costs."""
        """Calculate and return the subtotal of all drinks in the order."""
        base_price = Drink.size_prices[self.__size]
        return base_price + self.get_flavor_price()

    # Replaces the current list of flavors with a new list
    # Only keeps flavors that are on the menu and not already in the list
    def set_new_flavors(self, flavors):
        unique_flavors = []
        for flavor in flavors:
            if flavor in CinosDrinkMenu.drink_flavors and flavor not in unique_flavors:
                unique_flavors.append(flavor)
        self.__flavors = unique_flavors

    # Adds one new flavor if it’s on the menu and not already in the drink
    def add_flavor(self, flavor):
        if flavor not in CinosDrinkMenu.drink_flavors:
            raise ValueError(f"Sorry, '{flavor}' is not an available flavor. Please choose from {CinosDrinkMenu.drink_flavors}.")
        if flavor not in self.__flavors:
            self.__flavors.append(flavor)

    def __str__(self):
        """Return a string representation of the drink."""
        flavor_list = ', '.join(self.__flavors) if self.__flavors else "No flavors added"
        return f"Drink: {self.__base} ({self.__size}) with flavors: {flavor_list}"