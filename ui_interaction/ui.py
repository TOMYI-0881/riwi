"""Console UI helpers: menu display, user input, product find/update/statistics."""

from estructure.model_data import *
from crud.service import service as inventory_service


def show_menu():
    """Display static application menu options."""
    print(
        "-----------MENU----------- \n"
        "1) Add product \n"
        "2) Show products \n"
        "3) Search product \n"
        "4) Update product \n"
        "5) Delete product \n"
        "6) Statistics \n"
        "7) Save CSV \n"
        "8) Load CSV \n"
        "9) Exit \n"
        "--------------------------\n"
    )


def request_options() -> int | None:
    """Read integer option from user input; return None on invalid input."""
    try:
        option = int(input())
        return option
    except ValueError:
        return None


def update_product(product_wait: Product) -> Optional[dict]:
    """Interactively update a product price and/or stock.

    Returns a partial product dict with updated values. If no field is changed,
    values remain None and the caller can skip the update.
    """

    product_local: Product = {
        "name": product_wait["name"],
        "price": None,
        "stock": None,
    }

    while True:
        print("")
        print("Selected product to update:")
        print("-" * 40)
        print(f"Name: {product_wait['name']}")
        print(f"Price: ${product_wait['price']:.2f}")
        print(f"Stock: {product_wait['stock']}")
        print("-" * 40)
        process = input("Enter 'EDIT' to edit or 'SAVE' to save: ").strip().upper()

        if process == "SAVE":
            return product_local

        elif process == "EDIT":
            edit = ""
            while True:
                print("")
                print("Edit options:")
                print("1. Edit price")
                print("2. Edit stock")
                print("3. Exit editing")
                edit = input("Select an option (1-3): ").strip()

                try:
                    if edit == "1":
                        new_price = float(
                            input(f"New price for '{product_wait['name']}': ")
                        )
                        if new_price >= 0:
                            product_local["price"] = new_price
                            product_wait["price"] = new_price
                            print("Price updated.")
                        else:
                            print("Price must be greater than or equal to 0.")

                    elif edit == "2":
                        new_stock = int(
                            input(f"New stock for '{product_wait['name']}': ")
                        )
                        if new_stock >= 0:
                            product_local["stock"] = new_stock
                            product_wait["stock"] = new_stock
                            print("Stock updated.")
                        else:
                            print("Stock must be greater than or equal to 0.")

                    elif edit == "3":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Enter a valid value.")


def logic_find_product(text: str):
    """Handle product search, update, or delete operations based on text action."""
    name: str = input(f"Enter the product name you want to {text}: ").strip().lower()
    i_name = inventory_service.find_product(name)
    if not i_name:
        print(f"Product '{name}' not found in inventory.")
    else:
        if text == "search":
            print("Product found:")
            print("-" * 40)
            print(f"Name: {i_name['name']}")
            print(f"Price: ${i_name['price']:.2f}")
            print(f"Stock: {i_name['stock']}")
            print("-" * 40)

        if text == "update":
            product_up = update_product(i_name)
            inventory_service.update_product_inventory(product_up)

        if text == "delete":
            inventory_service.delete_product_inventory(name)


def show_statistics():
    """Display computed inventory statistics clearly.

    Uses calculate_statistic() to gather values and prints totals and best values.
    """
    statistics = inventory_service.calculate_statistic()
    if statistics is None:
        print("Inventory is empty.")
    else:
        print("\nInventory statistics:")
        print("-" * 40)
        print(f"{'Total units:':<25} {statistics['total_units']}")
        print(f"{'Total value:':<25} ${statistics['total_value']:.2f}")
        print()

        most_expensive = statistics["most_expensive_product"]
        print("Most expensive product:")
        print(f"{'Name:':<25} {most_expensive.get('name', 'N/A')}")
        print(f"{'Price:':<25} ${most_expensive.get('price', 0):.2f}")
        print()

        highest_stock = statistics["highest_stock_product"]
        print("Highest stock product:")
        print(f"{'Name:':<25} {highest_stock.get('name', 'N/A')}")
        print(f"{'Stock:':<25} {highest_stock.get('stock', 0)}")
        print("-" * 40)
