from estructure.model_data import *
from base_memory_csv.memory_csv_endoinsts import read_products_csv

inventory: list[Product] = []


def add_product_list(product: dict):

    for i in inventory:
        if i["name"] == product["name"]:
            i["stock"] += product["stock"]
            i["price"] = product["price"]
            return

    inventory.append(product)


def get_inventory():
    return inventory


def show_products():
    if not inventory:
        print("No hay productos en el inventario.")
    else:
        print("Productos en el inventario:")
        print(
            "\n{:<3} |{:<15} | {:<10} | {:<8}".format("No", "NOMBRE", "PRECIO", "STOCK")
        )
        for i, product in enumerate(inventory, start=1):
            price = float(product["price"]) if product["price"] is not None else 0.0
            stock = int(product["stock"]) if product["stock"] is not None else 0

            print("-" * 50)
            print(
                "{:<3} | {:<15} | {:<10.2f} | {:<8}".format(
                    i, product["name"], price, stock
                )
            )


def find_product(name: str) -> Optional[Product]:
    if not inventory:
        print("no hay productos en el inventario")
        return None

    else:
        for i in inventory:
            if i["name"] == name:
                return i


def update_product_inventory(up_product: Product):
    change: int = 0
    for i, v in enumerate(inventory):
        print("entro a la funcion update_product_inventory")
        print(up_product)
        if v["name"] == up_product["name"]:
            if up_product["price"] is not None:
                inventory[i]["price"] = up_product["price"]
                change += 1
            if up_product["stock"] is not None:
                inventory[i]["stock"] = up_product["stock"]
                change += 1
            if change == 0:
                print("no se realizaron cambios en el producto")
            else:
                print("producto actualizado correctamente")
            return


def delete_product_inventory(name: str):
    if not inventory:
        print("no hay productos en el inventario")
        return None

    else:
        for i in inventory:
            if i["name"] == name:
                inventory.remove(i)
                print("")
                print(
                    f"producto con el nombre {name.upper()} fue eliminado exitosamente"
                )
                return
        print(
            f"El producto con el nombre {name.upper()} no se encontro en el inventario "
        )


def calculate_statistic() -> Optional[Statistics]:
    if inventory is None:
        return None

    total_units: int = 0
    total_value: float = 0.0

    most_expensive_product: Product = inventory[0]
    highest_stock_product: Product = inventory[0]

    for p in inventory:
        total_units += p["stock"]
        total_value += p["price"] * p["stock"]

        if p["price"] > most_expensive_product["price"]:
            most_expensive_product = p

        if p["stock"] > highest_stock_product["stock"]:
            highest_stock_product = p

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
    inventory.clear()


def read_product_memory_csv():
    clear_inventory
    inventory.extend(read_products_csv())
