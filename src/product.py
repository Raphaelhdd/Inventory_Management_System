class Product:
    def __init__(self, name : str, price : float, quantity : int) -> None:
        """
        Initialize a new Product instance.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product.
        """
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