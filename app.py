from estructure.model_data import Product
from crud.service import show_products, find_product
from ui_interaction.ui import *


def menu_base():
    while True:
        print("")
        show_menu()
        option = request_options()

        if option == 1:
            name_product = ""
            price = 0.0
            stock = 0
            product_wait: Product = {}

            while True:
                try:
                    if not name_product:
                        name_product = input("Nombre del producto: ")
                        product_wait["name"] = name_product.strip().lower()
                    if not price:
                        price = float(input(f"Precio del producto {name_product}: "))
                        product_wait["price"] = price
                    if not stock:
                        stock = int(
                            input(f"cantida de {name_product} que deseas agregar: ")
                        )
                        product_wait["stock"] = stock
                    break
                except ValueError:
                    print()
                    print("--Ingresa un valor valido--")

            add_product_list(product_wait)

        elif option == 2:
            show_products()

        elif option == 3:
            logic_find_product("buscar")

        elif option == 4:
            logic_find_product("actualizar")

        elif option == 5:
            print("Eliminar Producto - Opción no implementada aún")

        elif option == 6:
            print("Estadistica - Opción no implementada aún")

        elif option == 7:
            print("Guardar CSV - Opción no implementada aún")

        elif option == 8:
            print("Cargar CSV - Opción no implementada aún")

        elif option == 9:
            print("Saliendo...")
            break
        elif not option:
            print("ingresa un valor valido")
        else:
            print("ingresa un numero de 1 - 9")


menu_base()
