import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ice_storm import IceCream

# Test creating an ice cream with a valid flavor
def test_valid_ice_cream():
    icecream_order = IceCream("Mint Chocolate Chip")
    assert icecream_order.get_icecream_name() == "Mint Chocolate Chip"
    assert icecream_order.get_total() == 4.00

# Test that an invalid flavor raises ValueError
def test_invalid_flavor():
    try:
        IceCream("Mango Madness")
        assert False, "Should raise ValueError for invalid flavor"
    except ValueError:
        assert True

# Test adding free toppings
def test_free_toppings():
    icecream_order = IceCream("Chocolate")
    icecream_order.add_topping("Cherry")
    icecream_order.add_topping("Whipped Cream")
    assert icecream_order.get_total() == 3.00

# Test adding paid toppings
def test_paid_toppings():
    icecream_order = IceCream("Vanilla Bean")
    icecream_order.add_topping("Caramel Sauce")
    icecream_order.add_topping("Chocolate Sauce")
    assert icecream_order.get_total() == 3.00 + 0.50 + 0.50

# Test adding mix-in toppings
def test_mixins():
    icecream_order = IceCream("Butter Pecan")
    icecream_order.add_topping("Storios")
    icecream_order.add_topping("Cookie Dough")
    assert icecream_order.get_total() == 3.50 + 1.00 + 1.00

# Test that duplicate toppings are not added
def test_no_duplicate_toppings():
    icecream_order = IceCream("Banana")
    icecream_order.add_topping("T&T's")
    icecream_order.add_topping("T&T's")  # Should not be added twice
    assert icecream_order.get_total() == 3.50 + 1.00
    assert icecream_order.get_toppings() == ["T&T's"]

# Test formatted string output for receipt
def test_str_representation():
    icecream_order = IceCream("S'more")
    icecream_order.add_topping("Pecans")
    icecream_order.add_topping("Cherry")
    receipt = str(icecream_order)
    assert "S'more" in receipt
    assert "Pecans" in receipt
    assert "Cherry" in receipt
    assert "$" in receipt

