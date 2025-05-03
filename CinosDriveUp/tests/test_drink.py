import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from drink import Drink
from order import Order
# this is a test for the Drink class
#this test checks if the drink class is working as expected
def test_add_flavor():
    d = Drink("water")
    d.add_flavor("lemon")
    assert "lemon" in d.get_drink_flavors()

def test_invalid_base():
    try:
        Drink("invalid")
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True