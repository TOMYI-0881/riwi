from estructure.model_data import *

import csv
import os


# Configuración de ruta
BASE_DIR = os.path.dirname(__file__)
FOLDER = os.path.join(BASE_DIR, "data_base")
FILE_PATH = os.path.join(FOLDER, "inventory.csv")


def add_product_csv(products: List[Product]):
    fieldnames = ["name", "price", "stock"]

    # Crear carpeta si no existe
    os.makedirs(FOLDER, exist_ok=True)

    with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products:
            writer.writerow(product)


def read_products_csv() -> List[Product]:

    #  Validar si el archivo existe
    if not os.path.isfile(FILE_PATH):
        print("El archivo no existe.")
        return []

    products: List[Product] = []

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
