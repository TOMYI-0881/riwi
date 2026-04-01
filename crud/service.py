"""
Módulo que maneja las operaciones CRUD del inventario.
"""

from estructure.model_data import *
from base_memory_csv.memory_csv_endoinsts import read_products_csv

inventory: list[Product] = []


def add_product_list(product: dict):
    """
    Agrega un producto al inventario. Si ya existe, actualiza stock y precio.

    Args:
        product (dict): Diccionario con 'name', 'price', 'stock'.
    """
    for i in inventory:
        if i["name"] == product["name"]:
            i["stock"] += product["stock"]
            i["price"] = product["price"]
            return

    inventory.append(product)


def get_inventory():
    """
    Retorna la lista del inventario actual.

    Returns:
        list[Product]: Lista de productos.
    """
    return inventory


def show_products():
    """
    Muestra los productos del inventario en formato tabular.
    """
    if not inventory:
        print("No hay productos en el inventario.")
    else:
        print("Productos en el inventario:")
        print("-" * 50)
        print(
            "{:<3} | {:<15} | {:<10} | {:<8}".format("No", "NOMBRE", "PRECIO", "STOCK")
        )
        print("-" * 50)
        for i, product in enumerate(inventory, start=1):
            price = float(product["price"]) if product["price"] is not None else 0.0
            stock = int(product["stock"]) if product["stock"] is not None else 0

            print(
                "{:<3} | {:<15} | ${:<9.2f} | {:<8}".format(
                    i, product["name"], price, stock
                )
            )
        print("-" * 50)


def find_product(name: str) -> Optional[Product]:
    """
    Busca un producto por nombre en el inventario.

    Args:
        name (str): Nombre del producto.

    Returns:
        Optional[Product]: Producto encontrado o None.
    """
    if not inventory:
        print("No hay productos en el inventario.")
        return None

    else:
        for i in inventory:
            if i["name"] == name:
                return i


def update_product_inventory(up_product: Product):
    """
    Actualiza un producto en el inventario con nuevos valores.

    Args:
        up_product (Product): Producto con valores actualizados.
    """
    change: int = 0
    for i, v in enumerate(inventory):
        if v["name"] == up_product["name"]:
            if up_product["price"] is not None:
                inventory[i]["price"] = up_product["price"]
                change += 1
            if up_product["stock"] is not None:
                inventory[i]["stock"] = up_product["stock"]
                change += 1
            if change == 0:
                print("No se realizaron cambios en el producto.")
            else:
                print("Producto actualizado correctamente.")
            return


def delete_product_inventory(name: str):
    """
    Elimina un producto del inventario por nombre.

    Args:
        name (str): Nombre del producto a eliminar.
    """
    if not inventory:
        print("No hay productos en el inventario.")
        return None

    else:
        for i in inventory:
            if i["name"] == name:
                inventory.remove(i)
                print(f"Producto '{name}' eliminado exitosamente.")
                return
        print(f"El producto '{name}' no se encontró en el inventario.")


def calculate_statistic() -> Optional[Statistics]:
    """
    Calcula estadísticas del inventario.

    Returns:
        Optional[Statistics]: Estadísticas o None si inventario vacío.
    """
    if inventory is None:
        return None

    total_units: int = 0
    total_value: float = 0.0

    most_expensive_product: Product = inventory[0]
    highest_stock_product: Product = inventory[0]

    for i in inventory:
        total_units += i["stock"]
        total_value += i["price"] * i["stock"]

        if i["price"] > most_expensive_product["price"]:
            most_expensive_product = i

        if i["stock"] > highest_stock_product["stock"]:
            highest_stock_product = i

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive_product": {
            "name": most_expensive_product["name"],
            "price": most_expensive_product["price"],
        },
        "highest_stock_product": {
            "name": highest_stock_product["name"],
            "stock": highest_stock_product["stock"],
        },
    }


def clear_inventory():
    """
    Limpia el inventario actual.
    """
    inventory.clear()


def read_product_memory_csv():
    """
    Carga productos desde CSV al inventario.
    """
    clear_inventory()
    inventory.extend(read_products_csv())
