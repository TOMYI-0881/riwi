"""Console UI helpers: menu display, user input, product find/update/statistics."""

from estructure.model_data import *
from crud.service import service as inventory_service


def show_menu():
    """Display static application menu options."""
    print(
        "-----------MENU----------- \n"
        "1) Agregar producto \n"
        "2) Mostrar Producto \n"
        "3) Buscar Producto \n"
        "4) Actualizar Producto \n"
        "5) Eliminar Producto \n"
        "6) Estadistica \n"
        "7) Guardar CSV \n"
        "8) Cargar CSV \n"
        "9) Salir \n"
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
        print("Producto seleccionado para actualizar:")
        print("-" * 40)
        print(f"Nombre: {product_wait['name']}")
        print(f"Precio: ${product_wait['price']:.2f}")
        print(f"Stock: {product_wait['stock']}")
        print("-" * 40)
        process = (
            input("Ingresa 'EDIT' para editar o 'SAVE' para guardar: ").strip().upper()
        )

        if process == "SAVE":
            return product_local

        elif process == "EDIT":
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
                    print("Ingresa un valor válido.")


def logic_find_product(text: str):
    """Handle product search, update, or delete operations based on text action."""
    name: str = (
        input(f"Ingresa el nombre del producto que deseas {text}: ").strip().lower()
    )
    i_name = inventory_service.find_product(name)
    if not i_name:
        print(f"El producto '{name}' no se encuentra en el inventario.")
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
    """Display computed inventory statistics clearly.

    Uses calculate_statistic() to gather values and prints totals and best values.
    """
    statistics = inventory_service.calculate_statistic()
    if statistics is None:
        print("El inventario está vacío.")
    else:
        print("\nEstadísticas del inventario:")
        print("-" * 40)
        print(f"{'Unidades totales:':<25} {statistics['total_units']}")
        print(f"{'Valor total:':<25} ${statistics['total_value']:.2f}")
        print()

        most_expensive = statistics["most_expensive_product"]
        print("Producto más caro:")
        print(f"{'Nombre:':<25} {most_expensive.get('name', 'N/A')}")
        print(f"{'Precio:':<25} ${most_expensive.get('price', 0):.2f}")
        print()

        highest_stock = statistics["highest_stock_product"]
        print("Producto con mayor stock:")
        print(f"{'Nombre:':<25} {highest_stock.get('name', 'N/A')}")
        print(f"{'Stock:':<25} {highest_stock.get('stock', 0)}")
        print("-" * 40)
