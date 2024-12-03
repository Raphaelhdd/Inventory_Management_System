class Product:
    def __init__(self, name : str, price : float, quantity : int) -> None:
        """
        Initialize a new Product instance.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product.
        """
        if price < 0:
            raise ValueError("Price of a product can't be negative.")
        if quantity < 0:
            raise ValueError("Quantity of a product can't be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def value(self) -> float:
        """
        Calculate the total value of the product
        Returns:
            float: Total value
        """
        return self.price * self.quantity

    def __repr__(self) -> str:
        """
        String representation of the Product instance
        Returns:
            str: a string that show the products details
        """
        return f"Product (Name : {self.name} , Price : {self.price}, Quantity : {self.quantity}"
    
    def __eq__(self, other: object) -> bool:
        """
        Overrides the default equality operator to check the equality of two Products.
        Args:
            other (object): object to check for equality

        Returns:
            bool: True if it's the same Product, otherwise False
        """
        if not isinstance(other, Product):
            return False
        return (self.name == other.name and self.price == other.price and self.quantity == other.quantity)
        