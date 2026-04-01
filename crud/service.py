from estructure.model_data import Product

inventory: list[Product] = []


def add_product_list(product: Product):
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
            print("-" * 50)
            print(
                "{:<3} | {:<15} | {:<10.2f} | {:<8}".format(
                    i, product["name"], product["price"], product["stock"]
                )
            )


def find_product(name: str) -> Product | None:
    if not inventory:
        print("no hay productos en el inventario")
        return None

    else:
        for i in inventory:
            if i["name"] == name:
                return i


def update_product_inventory(up_product: Product):
    for i, v in enumerate(inventory):
        print("entro a la funcion update_product_inventory")
        print(up_product)
        if v["name"] == up_product["name"]:
            if up_product["price"] is not None:
                inventory[i]["price"] = up_product["price"]
            if up_product["stock"] is not None:
                inventory[i]["stock"] = up_product["stock"]
