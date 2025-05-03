# Cinos Drink Menu
# This class contains the available drink options and flavors for the Cinos Drive-Up Beverage Service.
class CinosDrinkMenu:
    """
    This is the main list of drinks and flavors we offer at Cinos.
    We write it once here so we don’t have to keep repeating it everywhere else.
    """
    drink_options = ["water", "iced coffee", "iced tea", "juice", "soda", "sprite", "coke", "pepsi", "fanta", "redbull"]
    drink_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
    
    # This class contains the available drink options and flavors for the Cinos Drive-Up Beverage Service.
    # It also provides methods to validate and manage the drink options and flavors.
class Drink:
    """
    This class makes one drink. Every drink has a base (like juice or soda) and you can
    add flavors to customize it. We keep stuff private so it doesn’t get messed up by mistake.
    """
    def __init__(self, base):
        if base not in CinosDrinkMenu.drink_options:
            raise ValueError(f"Sorry, '{base}' is not on our menu. Please choose from {CinosDrinkMenu.drink_options}.")
        self.__base = base
        self.__flavors = []

    def get_drink_base(self):
        """Gives you the main drink (like soda, tea, etc.)."""
        return self.__base

    def get_drink_flavors(self):
        """Gives a list of all the flavors added to this drink."""
        return list(self.__flavors)

    def get_num_flavors(self):
        """Tells how many flavors were added in total."""
        return len(self.__flavors)

    def set_flavors(self, flavors):
        """
        Lets you set a whole new group of flavors, but only if they're valid
        and not repeated.
        """
        unique_flavors = []
        for flavor in flavors:
            if flavor in CinosDrinkMenu.drink_flavors and flavor not in unique_flavors:
                unique_flavors.append(flavor)
        self.__flavors = unique_flavors

    def add_flavor(self, flavor):
        """
        Adds one flavor to the drink if it’s on the menu and isn’t already added.
        """
        if flavor not in CinosDrinkMenu.drink_flavors:
            raise ValueError(f"Sorry, '{flavor}' is not an available flavor. Please choose from {CinosDrinkMenu.drink_flavors}.")
        if flavor not in self.__flavors:
            self.__flavors.append(flavor)