from estructure.model_data import *
import csv
import os
from typing import List

# Configuración de ruta
BASE_DIR = os.path.dirname(__file__)
FOLDER = os.path.join(BASE_DIR, "data_base")
FILE_PATH = os.path.join(FOLDER, "inventory.csv")


def read_products_csv() -> List[dict]:
    """Lee los productos del CSV y los retorna como lista de diccionarios"""

    if not os.path.isfile(FILE_PATH):
        print("El archivo no existe.")
        return []

    products: List[dict] = []

    with open(FILE_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for fila in reader:
            products.append(
                {
                    "name": fila["name"],
                    "price": float(fila["price"]),
                    "stock": int(fila["stock"]),
                }
            )

    return products


def add_product_csv(products: List[dict]):
    """
    Guarda productos en CSV.

    Pregunta al usuario si desea sobrescribir o fusionar:
    - yes: sobrescribe completamente
    - No: fusiona por nombre
    """

    fieldnames = ["name", "price", "stock"]

    os.makedirs(FOLDER, exist_ok=True)

    file_exists = os.path.isfile(FILE_PATH)

    # Leer datos actuales
    existing_products = read_products_csv()

    # Convertir a diccionario por nombre para fácil acceso
    existing_dict = {p["name"]: p for p in existing_products}

    # Preguntar al usuario
    opcion = (
        input(
            f"¿Sobrescribir inventario actual? ( YES / NO): \n"
            f"Digita YES si quieres sobrescribir \n"
            f"Digita NO si no quieres sobrescribir \n\n"
        )
        .strip()
        .lower()
    )

    # CASO 1: SOBRESCRIBIR
    if opcion == "yes":
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for product in products:
                writer.writerow(
                    {
                        "name": product["name"],
                        "price": product["price"],
                        "stock": product["stock"],
                    }
                )

        print("Inventario sobrescrito correctamente.")
        return

    # CASO 2: FUSIONAR
    elif opcion == "no":
        merged = existing_dict.copy()

        for product in products:
            name = product["name"]

            if name in merged:
                merged[name]["stock"] += product["stock"]
                merged[name]["price"] = product["price"]
            else:
                merged[name] = product

        # Guardar resultado fusionado
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for product in merged.values():
                writer.writerow(
                    {
                        "name": product["name"],
                        "price": product["price"],
                        "stock": product["stock"],
                    }
                )

        print("Inventario fusionado correctamente.")
        return

    else:
        print("Opción no válida.")
