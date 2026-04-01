from estructure.model_data import Product
from crud.service import (
    show_products,
    find_product,
    read_product_memory_csv,
    get_inventory,
)
from ui_interaction.ui import *
from base_memory_csv.memory_csv_endoinsts import add_product_csv, read_products_csv


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
            logic_find_product("buscar".lower())

        elif option == 4:
            logic_find_product("actualizar".lower())

        elif option == 5:
            logic_find_product("eliminar".lower())

        elif option == 6:
            show_statistics()

        elif option == 7:
            if get_inventory() != []:
                while True:
                    answer = (
                        input(
                            f"\nEstas seguro que quieres sobrescribir los datos actuales en la base de datos?\n"
                            f"digita la palabra yes si quieres continuar \n"
                            f"digita la palabra no si quieres cancelar \n"
                        )
                        .strip()
                        .lower()
                    )
                    if answer == "yes":
                        add_product_csv(get_inventory())
                        break
                    elif answer == "no":
                        print("")
                        print("se cancelo la operacion")
                        break
                    else:
                        print("")
                        print("la opcion digitada no es correcta")
            else:
                print("ERROR el inventario que quieres subir esta vacio")

        elif option == 8:
            read_product_memory_csv()

        elif option == 9:
            print("Saliendo...")
            break
        elif not option:
            print("ingresa un valor valido")
        else:
            print("ingresa un numero de 1 - 9")


menu_base()
