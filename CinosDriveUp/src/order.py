from drink import Drink

class Order:
    """
    This class helps keep track of all the drinks someone adds to their order — kind of like a shopping cart.
    Each drink has its own ID number so we can easily manage it. We also calculate a full receipt with subtotal,
    tax, and the total amount owed.
    """
    def __init__(self):
        self.__items = {}
        # This keeps track of the ID number for the next drink added to the order
        self.__order_counter_id = 1

    def get_items(self):
        """Return a dictionary of all drinks added to the order."""
        return dict(self.__items)

    def get_total(self):
        return sum(drink.get_total() for drink in self.__items.values())

    def get_num_items(self):
        """Return the total number of drinks in the order."""
        return len(self.__items)

    def get_receipt(self):
        """Generate and return a formatted receipt with drink details, subtotal, tax, and total."""
        receipt = "\n--- Cinos Receipt ---\n"
        subtotal = 0
        for drink_id, drink in self.__items.items():
            drink_total = drink.get_total()
            subtotal += drink_total
            receipt += f"Drink #{drink_id}: {drink.get_drink_base()} ({drink.get_size()}) with {', '.join(drink.get_drink_flavors())} - ${drink_total:.2f}\n"
            tax = subtotal * 0.0725
            total = subtotal + tax
            receipt += f"\nSubtotal: ${subtotal:.2f}"
            receipt += f"\nTax (7.25%): ${tax:.2f}"
            receipt += f"\nTotal: ${total:.2f}\n"
            return receipt

    def add_item(self, drink):
            """Add a Drink object to the order. Each added drink gets a unique ID."""
            if isinstance(drink, Drink):
                self.__items[self.__order_counter_id] = drink
                self.__order_counter_id += 1
            else:
                raise TypeError("Sorry, you can only add drinks to your order!")

    def remove_item(self, drink_id):
        """Remove a drink from the order by its ID number."""
        if drink_id in self.__items:
                del self.__items[drink_id]
        else:
            raise KeyError("Oops! That drink ID doesn't exist in your order.")