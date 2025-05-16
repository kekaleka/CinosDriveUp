import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
assert os.path.exists(os.path.join(os.path.dirname(__file__), '../src/hungry_hungry_students.py')), "Module not found: hungry_hungry_students"

from hungry_hungry_students import Food

# Test creating a valid food item and checking its name and price
def test_create_food():
    food = Food("Hotdog")
    assert food.get_food_name() == "Hotdog"
    assert food.get_total() == 2.30

# Test creating an invalid food item 
def test_invalid_food():
    try:
        Food("Pizza")
        assert False, "Should have raised ValueError for invalid food"
    except ValueError:
        assert True

# Test adding valid toppings to a food item
def test_add_toppings():
    food = Food("French Fries")
    food.add_topping("Ketchup")
    food.add_topping("Chili")
    toppings = food.get_toppings()
    assert "Ketchup" in toppings
    assert "Chili" in toppings
    assert food.get_total() == 1.50 + 0.60  # base + chili (ketchup is $0.00)

# Test ignoring duplicate toppings
def test_no_duplicate_toppings():
    food = Food("Tater Tots")
    food.add_topping("Bacon Bits")
    food.add_topping("Bacon Bits")
    toppings = food.get_toppings()
    assert toppings.count("Bacon Bits") == 1

# Test that total updates with multiple toppings
def test_food_total_with_toppings():
    food = Food("Nacho Chips")
    food.add_topping("Nacho Cheese")
    food.add_topping("Chili")
    food.add_topping("Bacon Bits")
    expected_total = 1.90 + 0.30 + 0.60 + 0.30
    assert abs(food.get_total() - expected_total) < 0.01
