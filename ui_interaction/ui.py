from estructure.model_data import *
from crud.service import (
    add_product_list,
    find_product,
    get_inventory,
    update_product_inventory,
    delete_product_inventory,
    calculate_statistic,
)


def show_menu():
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
    try:
        option = int(input())
        return option
    except ValueError:
        return None


def update_product(product_wait: Product) -> Optional[dict]:
    product_local: Product = {
        "name": product_wait["name"],
        "price": None,
        "stock": None,
    }
    iterator = 0
    while iterator != 1:
        print("")
        process = (
            str(
                input(
                    f"este es tu producto elegido para actualizar: \n"
                    f"---------------PRODUCT------------ \n"
                    f"{product_wait} \n"
                    f"------------------------------------ \n\n"
                    f"-si deseas editarlo digita la plabra EDIT \n"
                    f"-si deseas guardarlo digita la plabra SAVE \n\n"
                )
            )
            .strip()
            .upper()
        )

        if process == "SAVE":
            return product_local

        elif process == "EDIT":
            edit = ""
            while True:
                print("")
                edit = (
                    str(
                        input(
                            f"este es tu inventario actual: \n"
                            f"---------------INVENTARIO------------ \n"
                            f"{product_wait} \n"
                            f"------------------------------------ \n\n"
                            f"si quieres editar el precio, ingresa PRECIO \n"
                            f"si quieres editar la cantidad, CANTIDAD \n"
                            f"si quieres salir de la seccion de editar ingresa EXIT \n\n"
                        )
                    )
                    .strip()
                    .upper()
                )
                try:
                    if edit == "PRECIO":
                        product_local["price"] = float(
                            input(
                                f"\n Nuevo valor del producto {product_wait["name"]}: "
                            )
                        )
                        product_wait["price"] = product_local["price"]

                    elif edit == "CANTIDAD":
                        product_local["stock"] = int(
                            input(
                                f"\n Nueva cantidad asignable para el producto {product_wait['name']}: "
                            )
                        )
                        product_wait["stock"] = product_local["stock"]

                    elif edit == "EXIT":
                        break
                except ValueError:
                    print()
                    print("--Ingresa un valor valido--")


def logic_find_product(text: str):
    name: str = (
        input(f"Dame el nombre del producto que deseas {text.upper()}: \n")
        .strip()
        .lower()
    )
    i_name = find_product(name)
    if not i_name:
        print(
            f"el producto bajo el nombre de {name.upper()} que deseas {text}, no se encuentra en el inventario"
        )
    else:
        if text == "buscar":
            print("------PRODUCTO ENCONTRADO------")
            print(
                f"Producto: {i_name['name']} | Precio: {i_name['price']:.2f} | Cantidad: {i_name['stock']}"
            )
            print("-" * 40)

        if text == "actualizar":
            product_up = update_product(i_name)
            update_product_inventory(product_up)

        if text == "eliminar":
            delete_product_inventory(name)


def show_statistics():
    statistics = calculate_statistic()
    if statistics is None:
        print("El inventario está vacío")
    else:
        print("\n--- ESTADÍSTICAS ---")
        print(f"{'Unidades totales:':30} {statistics['total_units']}")
        print(f"{'Valor total:':30} ${statistics['total_value']:.2f}")

        most_expensive = statistics["most_expensive_product"]
        print(f"{'Producto más caro:':30} {most_expensive.get('name', 'N/A')}")
        print(f"{'Precio:':30} ${most_expensive.get('price', 0):.2f}")

        highest_stock = statistics["highest_stock_product"]
        print(f"{'Producto mayor stock:':30} {highest_stock.get('name', 'N/A')}")
        print(f"{'Stock:':30} {highest_stock.get('stock', 0)}")
