# Cinos Drink Menu
# This class contains the available drink options and flavors for the Cinos Drive-Up Beverage Service.
class CinosDrinkMenu:
    drink_options = ["water", "iced coffee", "iced tea", "juice", "soda", "sprite", "coke", "pepsi", "fanta", "redbull"]
    drink_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
    
    # This class contains the available drink options and flavors for the Cinos Drive-Up Beverage Service.
    # It also provides methods to validate and manage the drink options and flavors.
class Drink:
    def __init__(self, base):
        if base not in CinosDrinkMenu.drink_options:
            raise ValueError(f"Sorry, '{base}' is not on our menu. Please choose from {CinosDrinkMenu.drink_options}.")
        self.__base = base
        self.__flavors = []

    def get_drink_base(self):
        return self.__base

    def get_drink_flavors(self):
        return list(self.__flavors)

    def get_num_flavors(self):
        return len(self.__flavors)

    def set_flavors(self, flavors):
        unique_flavors = []
        for flavor in flavors:
            if flavor in CinosDrinkMenu.drink_flavors and flavor not in unique_flavors:
                unique_flavors.append(flavor)
        self.__flavors = unique_flavors

    def add_flavor(self, flavor):
        if flavor not in CinosDrinkMenu.drink_flavors:
            raise ValueError(f"Sorry, '{flavor}' is not an available flavor. Please choose from {CinosDrinkMenu.drink_flavors}.")
        if flavor not in self.__flavors:
            self.__flavors.append(flavor)