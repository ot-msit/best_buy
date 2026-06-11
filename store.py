from products import Product

class Store:
    """
    The Store class will contain one variable - a list of products that exist in the store.
    """

    def __init__(self, products: list[Product] | None = None):
        self.products: list[Product] = list(products) if products is not None else []

    def add_product(self, product: Product):
        """Adds a product from store."""
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.get_name()} is not sold in this store")
            total += product.buy(quantity)
        return total
