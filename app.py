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
                        name_product = input("Nombre del producto: ")
                        product_wait["name"] = name_product.strip().lower()
                    if price < 0.0:
                        price = float(input(f"Precio del producto '{name_product}': "))
                        if price >= 0:
                            product_wait["price"] = price
                        else:
                            price = -0.1
                            continue
                    if stock < 0:
                        stock = int(
                            input(f"Cantidad de '{name_product}' que deseas agregar: ")
                        )
                        if stock >= 0:
                            product_wait["stock"] = stock
                        else:
                            stock = -1
                            continue

                    break
                except ValueError:
                    print("Ingresa un valor válido.")

            inventory_service.add_product_list(product_wait)

        elif option == 2:
            inventory_service.show_products()

        elif option == 3:
            logic_find_product("buscar".lower())

        elif option == 4:
            logic_find_product("actualizar".lower())

        elif option == 5:
            logic_find_product("eliminar".lower())

        elif option == 6:
            show_statistics()

        elif option == 7:
            if inventory_service.get_inventory() != []:
                add_product_csv(inventory_service.get_inventory())
                inventory_service.clear_inventory()

            else:
                print("Error: El inventario está vacío.")

        elif option == 8:
            try:
                inventory_service.read_product_memory_csv()
            except FileNotFoundError:
                print("No se encontró el archivo CSV de inventario pendiente.")
            except UnicodeDecodeError:
                print("No se pudo decodificar el archivo CSV al cargar inventario.")
            except ValueError as e:
                print(f"Error de formato al cargar inventario CSV: {e}")
            except Exception as e:
                print(f"Error inesperado al cargar inventario CSV: {e}")

        elif option == 9:
            print("Saliendo...")
            break
        elif not option:
            print("Ingresa un valor válido.")
        else:
            print("Ingresa un número del 1 al 9.")


if __name__ == "__main__":
    menu_base()
