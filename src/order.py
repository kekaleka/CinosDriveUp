from drink import Drink
from hungry_hungry_students import Food


class Order:
    """
    This class helps keep track of all the items (drinks or food) someone adds to their order — kind of like a shopping cart.
    Each item gets an ID so we can manage it easily. The class also calculates subtotal, tax, and total.
    """
    def __init__(self):
        self.__items = {}
        self.__order_counter_id = 1

    def add_item(self, item):
        """Add a Drink or Food object to the order. Each item gets a unique ID."""
        if isinstance(item, (Drink, Food)):
            self.__items[self.__order_counter_id] = item
            self.__order_counter_id += 1
        else:
            raise TypeError("Only Drink or Food objects can be added to the order.")

    def remove_item(self, item_id):
        """Remove an item from the order using its ID number."""
        if item_id in self.__items:
            del self.__items[item_id]
        else:
            raise KeyError("That item ID does not exist in the order.")

    def get_items(self):
        """Return a dictionary of all items in the order."""
        return dict(self.__items)

    def get_num_items(self):
        """Return the number of items currently in the order."""
        return len(self.__items)

    def get_total(self):
        """Calculate and return the subtotal for all items before tax."""
        return sum(item.get_total() for item in self.__items.values())

    def get_receipt(self):
        """Return a formatted string receipt with each item's details, subtotal, tax, and final total."""
        receipt = "- Cinos Receipt ---"
        subtotal = 0
        for item_id, item in self.__items.items():
            item_total = item.get_total()
            subtotal += item_total

        if isinstance(item, Drink):
                receipt += f"Drink #{item_id}: {item.get_drink_base()} ({item.get_size()}) with {', '.join(item.get_drink_flavors())} - ${item_total:.2f}"
        elif isinstance(item, Food):
            receipt += f"Food #{item_id}: {item.get_food_name()} with {', '.join(item.get_toppings())} - ${item_total:.2f}"
            tax = subtotal * 0.0725
            total = subtotal + tax
            receipt += f"""Subtotal: ${subtotal:.2f}Tax (7.25%): ${tax:.2f}Total: ${total:.2f}"""
            return receipt