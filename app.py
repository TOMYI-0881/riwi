"""Main application entry point and user menu handling."""

from estructure.model_data import Product
from crud.service import service as inventory_service
from ui_interaction.ui import *
from base_memory_csv.memory_csv_endoinsts import add_product_csv, read_products_csv


def menu_base():
    """Show menu options and execute user actions.

    Loops until the user selects exit. Validates user input for actions
    and handles product add/show/search/update/delete/statistics/CSV operations.
    """
    while True:
        print("")
        show_menu()
        option = request_options()

        if option == 1:
            name_product = ""
            price = -0.1
            stock = -1
            product_wait: Product = {}

            while True:
                try:
                    if not name_product:
                        name_product = input("Product name: ")
                        product_wait["name"] = name_product.strip().lower()
                    if price < 0.0:
                        price = float(input(f"Price of '{name_product}': "))
                        if price >= 0:
                            product_wait["price"] = price
                        else:
                            price = -0.1
                            continue
                    if stock < 0:
                        stock = int(input(f"Quantity of '{name_product}' to add: "))
                        if stock >= 0:
                            product_wait["stock"] = stock
                        else:
                            stock = -1
                            continue

                    break
                except ValueError:
                    print("Enter a valid value.")

            inventory_service.add_product_list(product_wait)

        elif option == 2:
            inventory_service.show_products()

        elif option == 3:
            logic_find_product("search")

        elif option == 4:
            logic_find_product("update")

        elif option == 5:
            logic_find_product("delete")

        elif option == 6:
            show_statistics()

        elif option == 7:
            if inventory_service.get_inventory() != []:
                add_product_csv(inventory_service.get_inventory())
                inventory_service.clear_inventory()

            else:
                print("Error: Inventory is empty.")

        elif option == 8:
            try:
                inventory_service.read_product_memory_csv()
                print("Inventory successfully uploaded from CSV.")
            except FileNotFoundError:
                print("CSV inventory file not found.")
            except UnicodeDecodeError:
                print("Could not decode CSV when loading inventory.")
            except ValueError as e:
                print(f"CSV format error when loading inventory: {e}")
            except Exception as e:
                print(f"Unexpected error loading CSV inventory: {e}")

        elif option == 9:
            print("Exiting...")
            break
        elif not option:
            print("Enter a valid value.")
        else:
            print("Enter a number from 1 to 9.")


if __name__ == "__main__":
    menu_base()
