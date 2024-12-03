import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest 
from src.product import *


def test_product_initialization():
    """
    Test initialization of a product with valid data.
    """
    product = Product(name="Iphone 16", price=969.00, quantity = 5)
    assert product.name == "Iphone 16"
    assert product.price == 969.00
    assert product.quantity == 5


def test_product_value():
    """
    Test the calculation of the total value of a product with its quantity.
    """
    product = Product(name="Iphone 16", price=969.00, quantity = 5)
    assert product.value() == (969.00 * 5)

def test_product_equality():
    """
    Test the equality between two products that have the same attributes.
    """
    product1 = Product(name="Iphone 16", price=969.00, quantity = 5)
    product2 = Product(name="Iphone 16", price=969.00, quantity = 5)
    assert product1 == product2