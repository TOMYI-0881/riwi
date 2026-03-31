from estructure.model_data import Product
from crud.service import (
    add_product_list,
    find_product,
    get_inventory,
    update_product_inventory,
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


def update_product(product_wait: Product) -> Product:
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
            return product_wait

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
                            f"si quieres editar el producto, ingresa PRODUCTO \n"
                            f"si quieres editar el precio, ingresa PRECIO \n"
                            f"si quieres editar la cantidad, CANTIDAD \n"
                            f"si quieres salir de la seccion de editar ingresa EXIT \n\n"
                        )
                    )
                    .strip()
                    .upper()
                )

                if edit == "PRODUCTO":
                    product_wait["name"] = str(input(f"\n Nuevo nombre de producto: "))

                elif edit == "PRECIO":
                    product_wait["price"] = float(
                        input(f"\n Nuevo valor del producto {product_wait["name"]}: ")
                    )

                elif edit == "CANTIDAD":
                    product_wait["stock"] = int(
                        input(
                            f"\n Nueva cantidad asignable para el producto {product_wait['name']}: "
                        )
                    )

                elif edit == "EXIT":
                    break


def logic_find_product(text: str):
    name: str = (
        input(f"Dame el nombre del producto que deseas {text}: \n").strip().lower()
    )
    i_name = find_product(name)
    if not i_name:
        print(
            f"el producto bajo el nombre de {name} que deseas {text}, no se encuentra en el inventario"
        )
    else:
        print("------PRODUCTO ENCONTRADO------")
        print(
            f"Producto: {i_name['name']} | Precio: {i_name['price']} | Cantidad: {i_name['stock']}"
        )
        print("-" * 40)

        if text == "actualizar":
            product_up = update_product(i_name)
            update_product_inventory(product_up)

        # elif(name == "eliminar")
