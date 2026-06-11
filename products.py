class Product:
    """
    Initiator (constructor) method.
    Creates the instance variables (active is set to True).
    If something is invalid (empty name / negative price or quantity),
    raises an exception.
    """
    def __init__(self, name: str, price: float, quantity: int):
        if name == "":
            raise ValueError("Product should not be empty")
        self.name = name
        if price < 0:
            raise ValueError("Price should not be negative!")
        self.price = price
        if quantity < 0:
            raise ValueError("Quantity should not be negative!")
        self.quantity = quantity
        self.active = False
        if not quantity == 0:
            self.active = True

    """
    Setter function for quantity.
    If quantity reaches 0, deactivates the product.
    Assumption: active product if quantity > 0
    """
    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity should not be negative!")
        self.quantity = quantity
        if quantity == 0 and self.is_active():
            self.deactivate()
        elif quantity > 0 and not self.is_active():
            self.activate()

    """
    Getter function for quantity.
    Returns the quantity(int).
    """
    def get_quantity(self) -> int:
        return self.quantity

    """Activates the product."""
    def activate(self):
        self.active = True

    """Deactivates the product."""
    def deactivate(self):
        self.active = False

    """
    Getter function for active.
    Returns True if the product is active, otherwise False.
    """
    def is_active(self) -> bool:
        return self.active

    """Prints a string that represents the product"""
    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    """getter and setter for quantity, so also a getter for price"""
    def get_price(self) -> float:
        return self.price

    """
    Buys a given quantity of the product.
    Returns the total price (float) of the purchase.
    Updates the quantity of the product.
    In case of a problem (when? think about it), raises an Exception.
    """
    def buy(self, quantity: int) -> float:
        if quantity < 0:
            raise ValueError("Quantity should not be negative!")
        current_quantity = self.get_quantity()
        if quantity > current_quantity:
            raise ValueError("Amount not available!")
        self.set_quantity(current_quantity - quantity)
        total = quantity * self.get_price()
        return total