from src.product import *

class Inventory:
    def __init__(self):
        """
        Initializes an empty Inventory instance.
        """
        self.products = []
    
    def add_product(self, product : Product):
        """
        Adds a product to the inventory.
        Args:
            product (Product): product to add to the inventory  
        """
        if not isinstance(product, Product):
            raise ValueError("The product you want to add can't be added to the inventory.")
        self.products.append(product)
    
    def remove_product(self, product_name : str):
        """
        Removes a product from the inventory by its name.
        Args:
            product_name (str): The product's name to remove from the inventory.
        """
        initial_len = len(self.products)
        self.products = [product for product in self.products if product.name != product_name]
        if initial_len == len(self.products):
            raise ValueError(f"{product_name} is not found in the inventory")

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
        if not self.products:
            print("The inventory is empty.")
            return 0
        return sum(product.price * product.quantity for product in self.products)