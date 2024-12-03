import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest 
from src.product import *
from src.inventory import * 

@pytest.fixture 
def sample_inventory():
    """
    Creates and returns a sample inventory that will be usable in all our tests. 
    It's the starting inventory.
    """
    inventory = Inventory()
    inventory.add_product(Product(name="Iphone 16", price=969.00, quantity=5))
    inventory.add_product(Product(name="Iphone 16 Plus", price=1119.00, quantity=7))
    return inventory 

def test_add_product(sample_inventory):
    """
    Tests the functionality of adding a product to the inventory.
    """
    product = Product(name="Iphone 16 Pro", price=1229.00, quantity=10)
    sample_inventory.add_product(product)
    assert sample_inventory.get_product("Iphone 16 Pro") == product

def test_remove_product(sample_inventory):
    """
    Tests the functionality of removing a product from the inventory.
    """
    sample_inventory.remove_product("Iphone 16")
    assert sample_inventory.get_product("Iphone 16") is None

def test_get_product(sample_inventory):
    """
    Tests the functionality of retrieving a product from the inventory.
    """
    assert sample_inventory.get_product("Iphone 16 Pro") is None
    assert sample_inventory.get_product("Iphone 16") is not None
    assert sample_inventory.get_product("Iphone 16").price == 969.00

def test_total_inventory_value(sample_inventory):
    """
    Tests the calculation of the total value of the sample inventory.
    """
    assert sample_inventory.total_inventory_value() == ((969 * 5) + (1119 * 7))
