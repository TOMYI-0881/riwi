"""
Módulo principal de la aplicación - Punto de entrada y manejo del menú del usuario.

Este módulo contiene la lógica principal del programa de gestión de inventario.
Maneja la interacción con el usuario a través de un menú terminal y coordina
las operaciones de CRUD (Crear, Leer, Actualizar, Eliminar) del inventario.
"""

from estructure.model_data import Product
from crud.service import service as inventory_service
from ui_interaction.ui import *
from base_memory_csv.memory_csv_endoinsts import add_product_csv, read_products_csv


def menu_base():
    """
    Muestra el menú de opciones y ejecuta las acciones del usuario.

    La función mantiene un bucle infinito que se ejecuta hasta que el usuario
    selecciona la opción de salir (opción 9). Valida la entrada del usuario para
    cada acción y coordina las operaciones de:
    - Agregar productos al inventario
    - Mostrar todos los productos
    - Buscar productos por nombre
    - Actualizar información de productos
    - Eliminar productos del inventario
    - Ver estadísticas del inventario
    - Guardar el inventario en archivo CSV
    - Cargar inventario desde archivo CSV
    """
    while True:
        print("")
        show_menu()
        option = request_options()  # Solicita al usuario que seleccione una opción

        if option == 1:
            # OPCIÓN 1: Agregar un nuevo producto al inventario
            name_product = ""
            price = -0.1
            stock = -1
            product_wait: Product = (
                {}
            )  # Diccionario temporal para almacenar datos del producto

            while True:
                try:
                    # Solicita el nombre del producto si aún no se ha ingresado
                    if not name_product:
                        name_product = input("Nombre del producto: ")
                        product_wait["name"] = name_product.strip().lower()

                    # Solicita el precio si aún no se ha ingresado con validación
                    if price < 0.0:
                        price = float(input(f"Precio de '{name_product}': "))
                        if price >= 0:
                            product_wait["price"] = price
                        else:
                            print("El precio no puede ser negativo.")
                            price = -0.1
                            continue

                    # Solicita la cantidad a agregar con validación
                    if stock < 0:
                        stock = int(input(f"Cantidad de '{name_product}' a agregar: "))
                        if stock >= 0:
                            product_wait["stock"] = stock
                        else:
                            print("La cantidad no puede ser negativa.")
                            stock = -1
                            continue

                    break
                except ValueError:
                    print("Por favor, ingresa un valor válido.")

            inventory_service.add_product_list(product_wait)

        elif option == 2:
            # OPCIÓN 2: Mostrar todos los productos del inventario
            inventory_service.show_products()

        elif option == 3:
            # OPCIÓN 3: Buscar un producto por nombre
            logic_find_product("buscar")

        elif option == 4:
            # OPCIÓN 4: Actualizar información de un producto
            logic_find_product("actualizar")

        elif option == 5:
            # OPCIÓN 5: Eliminar un producto del inventario
            logic_find_product("eliminar")

        elif option == 6:
            # OPCIÓN 6: Mostrar estadísticas del inventario
            show_statistics()

        elif option == 7:
            # OPCIÓN 7: Guardar el inventario actual en un archivo CSV
            if inventory_service.get_inventory() != []:
                add_product_csv(inventory_service.get_inventory())
                inventory_service.clear_inventory()
            else:
                print("Error: El inventario está vacío.")

        elif option == 8:
            # OPCIÓN 8: Cargar el inventario desde un archivo CSV
            try:
                inventory_service.read_product_memory_csv()
                print("Inventario cargado exitosamente desde el archivo CSV.")
            except FileNotFoundError:
                print("Error: No se encontró el archivo CSV de inventario.")
            except UnicodeDecodeError:
                print(
                    "Error: No se pudo decodificar el archivo CSV al cargar el inventario."
                )
            except ValueError as e:
                print(f"Error de formato en CSV al cargar el inventario: {e}")
            except Exception as e:
                print(f"Error inesperado al cargar el inventario desde CSV: {e}")

        elif option == 9:
            # OPCIÓN 9: Salir de la aplicación
            print("Saliendo...")
            break
        elif not option:
            print("Por favor, ingresa un valor válido.")
        else:
            print("Por favor, ingresa un número del 1 al 9.")


if __name__ == "__main__":
    menu_base()
