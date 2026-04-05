"""Módulo de interfaz de usuario de consola: menú, entrada de usuario, búsqueda y estadísticas.

Este módulo contiene funciones auxiliares para mostrar el menú, solicitar opciones
del usuario, buscar productos, actualizar productos y mostrar estadísticas del inventario.
Toda la interacción con el usuario ocurre a través de la consola terminal.
"""

from estructure.model_data import *
from crud.service import service as inventory_service


def show_menu():
    """
    Muestra el menú estático de opciones de la aplicación.

    Las opciones incluyen añadir, mostrar, buscar, actualizar y eliminar productos,
    ver estadísticas, guardar y cargar desde CSV, y salir de la aplicación.
    """
    print(
        "-----------MENÚ----------- \n"
        "1) Añadir producto \n"
        "2) Mostrar productos \n"
        "3) Buscar producto \n"
        "4) Actualizar producto \n"
        "5) Eliminar producto \n"
        "6) Estadísticas \n"
        "7) Guardar en CSV \n"
        "8) Cargar de CSV \n"
        "9) Salir \n"
        "--------------------------\n"
    )


def request_options() -> int | None:
    """
    Lee una opción numérica desde la entrada del usuario.

    Intenta convertir la entrada a un entero. Si la entrada es inválida,
    retorna None para indicar un error de conversión.

    Returns:
        int | None: La opción numérica si es válida, None en caso contrario.
    """
    try:
        option = int(input())
        return option
    except ValueError:
        return None


def update_product(product_wait: Product) -> Optional[dict]:
    """
    Interfaz interactiva para actualizar el precio y/o cantidad de un producto.

    Muestra un menú donde el usuario puede editar el precio o la cantidad del producto.
    Retorna un diccionario parcial con solo los valores que fueron modificados (None si no hay cambios).

    Args:
        product_wait (Product): El producto a actualizar.

    Returns:
        Optional[dict]: Diccionario con el nombre y los campos actualizados del producto.
    """

    product_local: Product = {
        "name": product_wait["name"],
        "price": None,
        "stock": None,
    }

    while True:
        print("")
        print("Producto seleccionado para actualizar:")
        print("-" * 40)
        print(f"Nombre: {product_wait['name']}")
        print(f"Precio: ${product_wait['price']:.2f}")
        print(f"Stock: {product_wait['stock']}")
        print("-" * 40)
        process = (
            input("Ingresa 'EDITAR' para editar o 'GUARDAR' para guardar: ")
            .strip()
            .upper()
        )

        if process == "GUARDAR":
            return product_local

        elif process == "EDITAR":
            edit = ""
            while True:
                print("")
                print("Opciones de edición:")
                print("1. Editar precio")
                print("2. Editar stock")
                print("3. Salir de edición")
                edit = input("Selecciona una opción (1-3): ").strip()

                try:
                    if edit == "1":
                        new_price = float(
                            input(f"Nuevo precio para '{product_wait['name']}': ")
                        )
                        if new_price >= 0:
                            product_local["price"] = new_price
                            product_wait["price"] = new_price
                            print("Precio actualizado.")
                        else:
                            print("El precio debe ser mayor o igual a 0.")

                    elif edit == "2":
                        new_stock = int(
                            input(f"Nuevo stock para '{product_wait['name']}': ")
                        )
                        if new_stock >= 0:
                            product_local["stock"] = new_stock
                            product_wait["stock"] = new_stock
                            print("Stock actualizado.")
                        else:
                            print("El stock debe ser mayor o igual a 0.")

                    elif edit == "3":
                        break

                    else:
                        print("Opción inválida.")

                except ValueError:
                    print("Por favor, ingresa un valor válido.")


def logic_find_product(text: str):
    """
    Maneja las operaciones de búsqueda, actualización o eliminación de productos.

    Según el parámetro 'text', realiza:
    - "buscar": Muestra la información del producto encontrado.
    - "actualizar": Abre el editor interactivo para modificar el producto.
    - "eliminar": Elimina el producto del inventario.

    Args:
        text (str): La acción a realizar: "buscar", "actualizar" o "eliminar".
    """
    name: str = (
        input(f"Ingresa el nombre del producto que deseas {text}: ").strip().lower()
    )
    i_name = inventory_service.find_product(name)
    if not i_name:
        print(f"El producto '{name}' no se encontró en el inventario.")
    else:
        if text == "buscar":
            print("Producto encontrado:")
            print("-" * 40)
            print(f"Nombre: {i_name['name']}")
            print(f"Precio: ${i_name['price']:.2f}")
            print(f"Stock: {i_name['stock']}")
            print("-" * 40)

        if text == "actualizar":
            product_up = update_product(i_name)
            inventory_service.update_product_inventory(product_up)

        if text == "eliminar":
            inventory_service.delete_product_inventory(name)


def show_statistics():
    """
    Muestra las estadísticas agregadas del inventario de forma clara y formateada.

    Utiliza calculate_statistic() para obtener los valores y muestra:
    - Total de unidades y valor total del inventario
    - Producto más costoso
    - Producto con mayor cantidad en stock
    """
    statistics = inventory_service.calculate_statistic()
    if statistics is None:
        print("El inventario está vacío.")
    else:
        print("\nEstadísticas del inventario:")
        print("-" * 40)
        print(f"{'Total de unidades:':<25} {statistics['total_units']}")
        print(f"{'Valor total:':<25} ${statistics['total_value']:.2f}")
        print()

        most_expensive = statistics["most_expensive_product"]
        print("Producto más costoso:")
        print(f"{'Nombre:':<25} {most_expensive.get('name', 'N/A')}")
        print(f"{'Precio:':<25} ${most_expensive.get('price', 0):.2f}")
        print()

        highest_stock = statistics["highest_stock_product"]
        print("Producto con mayor stock:")
        print(f"{'Nombre:':<25} {highest_stock.get('name', 'N/A')}")
        print(f"{'Stock:':<25} {highest_stock.get('stock', 0)}")
        print("-" * 40)
