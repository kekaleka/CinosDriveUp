import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from drink import Drink
from order import Order

# this test checks if the Order class is working as expected
def test_add_item():
    o = Order()
    d = Drink("sprite")
    o.add_item(d)
    assert o.get_num_items() == 1
#
def test_remove_item():
    o = Order()
    d = Drink("fanta")
    o.add_item(d)
    item_id = list(o.get_items().keys())[0]
    o.remove_item(item_id)
    assert o.get_num_items() == 0

def test_get_receipt_base():
    o = Order()
    d = Drink("soda")
    d.add_flavor("mint")
    o.add_item(d)
    receipt = o.get_receipt()
    assert "soda" in receipt