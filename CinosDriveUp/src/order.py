from drink import Drink

class Order:
    """
    This class is like a shopping cart. It keeps track of all the drinks someone orders.
    Each drink has an ID number so we can add or remove them easily and print a full receipt.
    """
    def __init__(self):
        # We start with no drinks, and the first ID will be 1
        self.__items = {}
        self.__next_id = 1

    def get_items(self):
        """Returns all the drinks currently in the order."""
        return dict(self.__items)

    def get_total(self):
        """Each drink is $3.50 — this tells us the total price for all of them."""
        return len(self.__items) * 3.50

    def get_num_items(self):
        """Tells us how many total drinks are in this order."""
        return len(self.__items)

    def get_receipt(self):
        """
        Builds a little receipt showing each drink and its flavors, and the total cost at the bottom.
        """
        receipt = "--- Cinos Receipt ---"
        for drink_id, drink in self.__items.items():
            # List each drink’s base and flavors
            receipt += f"Drink #{drink_id}: {drink.get_drink_base()} with {', '.join(drink.get_drink_flavors())}"

        receipt += f"Total: ${self.get_total():.2f}"
        return receipt

    def add_item(self, drink):
        """
        Adds a drink to the order. Only works if what you're adding is actually a Drink.
        """
        if isinstance(drink, Drink):
            self.__items[self.__next_id] = drink
            self.__next_id += 1
        else:
            raise TypeError("Sorry, you can only add drinks to your order!")

    def remove_item(self, drink_id):
        """
        Lets us delete a drink by its ID number. If you use an ID that doesn’t exist, we’ll get an error.
        """
        if drink_id in self.__items:
            del self.__items[drink_id]
        else:
            raise KeyError("Oops! That drink ID doesn't exist in your order.")