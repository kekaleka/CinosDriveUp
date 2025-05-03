from drink import Drink
# Cinos Drive-Up Beverage Service
# This class manages the order of drinks, allowing items to be added or removed.
class Order:
    def __init__(self):
        # Start with an empty order
        self.__items = {}
        self.__next_id = 1

    def get_items(self):
        return dict(self.__items)

    def get_total(self):
        return len(self.__items) * 3.50

    def get_num_items(self):
        return len(self.__items)
    
        # Get the total number of items in the order
    def get_receipt(self):
        receipt = "\n--- Cinos Receipt ---\n"
        for drink_id, drink in self.__items.items():
            receipt += f"Drink #{drink_id}: {drink.get_drink_base()} with {', '.join(drink.get_drink_flavors())}\n"
        receipt += f"Total: ${self.get_total():.2f}\n"
        return receipt

    def add_item(self, drink):
        # Only Drink objects can be added to an order
        if isinstance(drink, Drink):
            self.__items[self.__next_id] = drink
            self.__next_id += 1
        else:
            raise TypeError("Sorry, you can only add drinks to your order!")

    def remove_item(self, drink_id):
        # Removes a drink by its ID
        if drink_id in self.__items:
            del self.__items[drink_id]
        else:
            raise KeyError("Oops! That drink ID doesn't exist in your order.")