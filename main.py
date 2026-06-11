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
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                   ]
    best_buy = Store(product_list)
    start(best_buy)

def start(store: Store):
    while True:
        print(MENU)
        menu_answer = input("Please choose a number: ")
        match menu_answer:
            case "1":
                show_product_list(store)
            case "2":
                print(store.get_total_quantity())
            case "3":
                pass
            case "4":
                break
            case _:
                print("Please enter a number")

def show_product_list(store: Store):
    print("---------------------------------------------")
    for product in store.get_all_products():
        product.show()
    print("---------------------------------------------")

if __name__ == "__main__":
      main()