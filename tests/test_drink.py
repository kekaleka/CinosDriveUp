import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from drink import Drink
from order import Order

# This tests if the add flavor section works
def test_add_flavor():
    custom_drink = Drink("water", "small")
    custom_drink.add_flavor("lemon")
    assert "lemon" in custom_drink.get_drink_flavors()

#tests if invalid base makes  sure it will return an error
def test_invalid_base():
    try:
        Drink("invalid", "small")
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True

# Tests that the prices add properly after adding a flavor
def test_flavor_price():
    custom_drink = Drink("juice", "medium")
    custom_drink.add_flavor("lime")
    custom_drink.add_flavor("mint")
    assert custom_drink.get_flavor_price() == 0.30

#Tests that the total price funtion works
def test_total_price():
    custom_drink = Drink("juice", "medium")
    custom_drink.add_flavor("lime")
    custom_drink.add_flavor("mint")
    expected_total = 1.75 + 0.30
    assert custom_drink.get_total() == expected_total

#tests that multiple flavors can be added
def test_add_multiple_flavors():
    custom_drink = Drink("soda", "large")
    custom_drink.add_flavor("lemon")
    custom_drink.add_flavor("cherry")
    custom_drink.add_flavor("mint")
    flavors = custom_drink.get_drink_flavors()
    assert len(flavors) == 3
    assert set(flavors) == {"lemon", "cherry", "mint"}

#tests that the list can be amended for future updates
def test_set_new_flavors():
    custom_drink = Drink("iced coffee", "medium")
    custom_drink.set_new_flavors(["lemon", "mint", "lemon", "banana"])
    flavors = custom_drink.get_drink_flavors()
    assert flavors == ["lemon", "mint"]