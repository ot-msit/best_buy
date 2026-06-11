class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.
        """
        if name == "":
            raise ValueError("Product should not be empty")
        self.name = name
        if price < 0:
            raise ValueError("Price should not be negative!")
        self.price = price
        if quantity < 0:
            raise ValueError("Quantity should not be negative!")
        self.quantity = quantity
        self.active = quantity > 0

    def set_quantity(self, quantity: int):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        Assumption: active product if quantity > 0
        """
        if quantity < 0:
            raise ValueError("Quantity should not be negative!")
        self.quantity = quantity
        if quantity == 0 and self.is_active():
            self.deactivate()
        elif quantity > 0 and not self.is_active():
            self.activate()

    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity(int)."""
        return self.quantity

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def show(self):
        """Prints a string that represents the product"""
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def get_price(self) -> float:
        """getter and setter should be used, so also a getter for price"""
        return self.price

    def get_name(self) -> str:
        """getter and setter should be used, so also a getter for name"""
        return self.name

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        if quantity < 0:
            raise ValueError("Quantity should not be negative!")
        current_quantity = self.get_quantity()
        if quantity > current_quantity:
            raise ValueError("Amount not available!")
        self.set_quantity(current_quantity - quantity)
        total = quantity * self.get_price()
        return total