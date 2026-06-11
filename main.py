from store import Store
from products import Product

MENU = """
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""

def main():
    """Initialize the shop with its products and start the menu."""
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", 1450, 100),
                    Product("Bose QuietComfort Earbuds", 250, 500),
                    Product("Google Pixel 7", 500, 250)
                   ]
    best_buy = Store(product_list)
    start(best_buy)

def start(store: Store):
    """Run the main menu loop and dispatch the user's choice."""
    product_list = store.get_all_products()
    shopping_list = []
    while True:
        print(MENU)
        menu_answer = input("Please choose a number: ")
        match menu_answer:
            case "1":
                show_product_list(product_list)
            case "2":
                print(f"\nTotal of {store.get_total_quantity()} items in store")
            case "3":
                show_product_list(product_list)
                print("\nWhen you want to finish order, enter empty text.")
                while True:
                    product_answer = input("Which product # do you want? ")
                    if product_answer == "":
                        if shopping_list:
                            try:
                                total = store.order(shopping_list)
                                print(f"\nOrder made! Total payment: ${total}")
                                shopping_list = []
                                product_list = store.get_all_products()
                            except ValueError as e:
                                print(e)
                        break
                    try:
                        product_number = validate_product_answer(product_answer, product_list)
                        product = product_list[product_number]
                    except ValueError as e:
                        print(e)
                        continue
                    while True:
                        product_amount = input("\nWhat amount do you want? ")
                        if product_amount == "":
                            continue
                        try:
                            quantity = validate_product_amount(product_amount, product)
                            shopping_list.append((product, quantity))
                        except ValueError as e:
                            print(e)
                            continue
                        print("\nProduct added to list!\n")
                        break
            case "4":
                break
            case _:
                pass

def show_product_list(product_list: list[Product]):
    """show the product list with an index"""
    print("---------------------------------------------")
    if not product_list:
        print("No products available")
    else:
        for index, product in enumerate(product_list, start=1):
            print(f"{index}. {product.show()}")
    print("---------------------------------------------")

def validate_product_answer(product_answer: str, product_list: list[Product]) -> int:
    """Validate that the input is a number within the available product range."""
    if not product_answer.isdigit():
        raise ValueError("\nPlease enter a number")
    product_answer_int = int(product_answer)
    if not 0 < product_answer_int <= len(product_list):
        raise ValueError("\nProduct not available")
    return product_answer_int - 1 # reduce by 1 for index (starts counting at 0)

def validate_product_amount(product_amount: str, product: Product) -> int:
    """Validate that the input is a number within the available quantity range."""
    if not product_amount.isdigit():
        raise ValueError("\nPlease enter a number")
    product_amount_int = int(product_amount)
    if not 0 < product_amount_int <= product.get_quantity():
        raise ValueError("\nNot available in this quantity")
    return product_amount_int

if __name__ == "__main__":
      main()
