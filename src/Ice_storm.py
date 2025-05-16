
# This class is used to create a dessert menu for the Cinos restaurant.
class CinosDessertMenu:

    """
    This is the main list of icecreams and toppings offered at Cinos.
    """
    icecream_flavors = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }
    
    toppings = {
        "Chocolate Sauce": 0.50,
        "Caramel Sauce": 0.50,
        "Whipped Cream": 0.00,
        "Cherry": 0.00,
        "Storios": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50,
    }

class IceCream:
    """
    This class builds a single icecream item for the order.
    It checks if the item is on the menu and provides access to the name, toppings, and price.
    """
    def __init__(self, name):
        if name not in CinosDessertMenu.icecream_flavors:
            raise ValueError(f"'{name}' is not on the dessert menu.")
        self.__name = name
        self.__price = CinosDessertMenu.icecream_flavors[name]
        self.__toppings = []

    def get_icecream_name(self):
        """Return the name of the ice cream item."""
        return self.__name
    
    def get_toppings(self):
        """Return a list of all toppings added to the ice cream item."""
        return list(self.__toppings)
    
    def get_topping_price(self):
        """Calculate the total price for all toppings added."""
        return sum(CinosDessertMenu.toppings[t] for t in self.__toppings)
    
    def add_topping(self, topping):
        """Add a topping if it's valid and not already added."""
        if topping not in CinosDessertMenu.toppings:
            raise ValueError(f"'{topping}' is not a valid topping.")
        if topping not in self.__toppings:
            self.__toppings.append(topping)

    def get_total(self):
        """Calculate and return the total price of the ice cream including toppings."""
        return self.__price + self.get_topping_price()
    
    def __str__(self):
        """Return a string representation of the ice cream item."""
        toppings_str = ', '.join(self.__toppings) if self.__toppings else "No toppings"
        return f"{self.__name} with {toppings_str} - ${self.get_total():.2f}"
    
    
