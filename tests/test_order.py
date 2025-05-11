import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from drink import Drink
from order import Order


def test_add_item():
    order = Order()
    custom_drink = Drink("sprite", "small")
    order.add_item(custom_drink)
    assert order.get_num_items() == 1

def test_remove_item():
    order = Order()
    custom_drink = Drink("fanta", "small")
    order.add_item(custom_drink)
    item_id = list(order.get_items().keys())[0]
    order.remove_item(item_id)
    assert order.get_num_items() == 0

def test_get_receipt_base():
    order = Order()
    custom_drink = Drink("soda", "small")
    custom_drink.add_flavor("mint")
    order.add_item(custom_drink)
    receipt = order.get_receipt()
    assert all(word in receipt for word in ["soda", "mint", "small", "Subtotal", "Tax (7.25%)", "Total"])