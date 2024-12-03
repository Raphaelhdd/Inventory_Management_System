from src.product import *

class Inventory:
    def __init__(self):
        """
        Initialize an empty Inventory instance.
        """
        self.products = []
    
    def add_product(self, product : Product):
        """
        Add a product to the inventory.
        Args:
            product (Product): product to add to the inventory  
        """
        self.products.append(product)
    
    def remove_product(self, product_name : str):
        """
        Remove a product from the inventory by its name
        Args:
            product_name (str): The product's name to remove from the inventory
        """
        self.products = [product for product in self.products if product.name != product_name]

    def get_product(self, product_name : str) -> Product:
        """
        Get a product by its name.
        Args:
            product_name (str): product's name to find in the inventory

        Returns:
            Product: the product if it's in the inventory, else None
        """
        for product in self.products:
            if product.name == product_name:
                return product
        return None
    
    def total_inventory_value(self) -> float:
        """
        Calculate the total inventory value of the inventory
        Returns:
            float: total value of the inventory
        """
        return sum(product.price * product.quantity for product in self.products)