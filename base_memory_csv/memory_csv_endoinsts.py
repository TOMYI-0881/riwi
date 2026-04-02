"""CSV persistence utilities for inventory data."""

from estructure.model_data import *
import csv
import os
from typing import List

# Path configuration for inventory file
BASE_DIR = os.path.dirname(__file__)
FOLDER = os.path.join(BASE_DIR, "data_base")
FILE_PATH = os.path.join(FOLDER, "inventory.csv")


def read_products_csv() -> List[dict]:
    """Read products from CSV and return a list of product dictionaries."""

    if not os.path.isfile(FILE_PATH):
        print("El archivo no existe.")
        return []

    products: List[dict] = []

    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for fila in reader:
                try:
                    products.append(
                        {
                            "name": fila["name"],
                            "price": float(fila["price"]),
                            "stock": int(fila["stock"]),
                        }
                    )
                except (ValueError, TypeError) as e:
                    print(f"Error de formato en fila CSV: {fila} -> {e}")
                    continue

    except FileNotFoundError:
        print(f"Archivo no encontrado: {FILE_PATH}")
        return []
    except UnicodeDecodeError as e:
        print(f"Error de decodificación al leer CSV: {e}")
        return []
    except Exception as e:
        print(f"Error desconocido al leer CSV: {e}")
        return []

    return products


def add_product_csv(products: List[dict]):
    """Save product list to CSV file with optional overwrite or merge.

    User chooses:
    - YES: overwrite inventory file
    - NO: merge stock by product name and update price
    """

    fieldnames = ["name", "price", "stock"]

    os.makedirs(FOLDER, exist_ok=True)

    # Check that the file exists; if it does not, create it using the current products
    # file_exists = os.path.isfile(FILE_PATH)

    # Read current data
    existing_products = read_products_csv()

    # Convert to a dictionary by name for easy access
    existing_dict = {p["name"]: p for p in existing_products}

    # Ask the user
    opcion = (
        input(
            f"¿Sobrescribir inventario actual? ( YES / NO): \n"
            f"Digita YES si quieres sobrescribir \n"
            f"Digita NO si no quieres sobrescribir \n\n"
        )
        .strip()
        .lower()
    )

    try:
        # CASE 1: OVERWRITE
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

        # CASE 2: MERGE
        elif opcion == "no":
            merged = existing_dict.copy()

            for product in products:
                name = product["name"]

                if name in merged:
                    merged[name]["stock"] += product["stock"]
                    merged[name]["price"] = product["price"]
                else:
                    merged[name] = product

            # Save merged result
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

    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado al guardar CSV: {e}")
    except UnicodeDecodeError as e:
        print(f"Error de decodificación al guardar CSV: {e}")
    except ValueError as e:
        print(f"Error de conversión de datos al guardar CSV: {e}")
    except Exception as e:
        print(f"Error desconocido al guardar CSV: {e}")
