"""Utilidades de persistencia CSV para datos de inventario.

Este módulo proporciona funciones para leer y guardar datos de productos
desde y hacia archivos CSV. Permite cargar un inventario existente o guardar
el inventario actual con opciones de sobrescribir o fusionar datos existentes.

Funciones principales:
  - read_products_csv(): Lee productos del archivo CSV
  - add_product_csv(): Guarda productos en archivo CSV con dos opciones (sobrescribir o fusionar)

Estructura de archivos:
  - Ubicación: base_memory_csv/data_base/inventory.csv
  - Formato: CSV con columnas name, price, stock
"""

# ============================================================================
# IMPORTACIONES: Módulos necesarios para manipular archivos y datos
# ============================================================================

from estructure.model_data import *  # Importa tipos Product y Statistics
import csv  # Módulo para leer y escribir archivos CSV
import os  # Módulo para trabajar con rutas de archivos y directorios
from typing import List  # Importa anotación de tipo List para especificar retornos

# ============================================================================
# CONFIGURACIÓN DE RUTAS: Define dónde se guarda el archivo de inventario
# ============================================================================

# BASE_DIR: Obtiene la carpeta donde se encuentra este archivo de Python
# __file__ contiene la ruta completa del archivo actual
BASE_DIR = os.path.dirname(__file__)

# FOLDER: Construye la ruta a la carpeta "data_base" dentro de la carpeta actual
# Resultado: ...\base_memory_csv\data_base
FOLDER = os.path.join(BASE_DIR, "data_base")

# FILE_PATH: Construye la ruta completa al archivo CSV de inventario
# Resultado: ...\base_memory_csv\data_base\inventory.csv
FILE_PATH = os.path.join(FOLDER, "inventory.csv")


# ============================================================================
# FUNCIÓN: read_products_csv()
# Propósito: Leer datos de productos desde un archivo CSV y cargarlos en memoria
# ============================================================================


def read_products_csv() -> List[dict]:
    """
    Lee productos desde un archivo CSV y retorna una lista de diccionarios de productos.

    Valida los tipos de datos de cada fila del CSV. Si ocurre un error al procesar
    una fila, la salta y continúa con la siguiente.

    Returns:
        List[dict]: Lista de diccionarios con las claves 'name', 'price' y 'stock'.
                    Retorna una lista vacía si el archivo no existe o hay errores.
    """

    # PASO 1: Verificar si el archivo CSV existe en el sistema de archivos
    # Si no existe, no hay datos que cargar, por lo que retornamos una lista vacía
    if not os.path.isfile(FILE_PATH):
        print("El archivo no existe.")
        return []  # Retorna lista vacía si no hay archivo

    # PASO 2: Crear una lista vacía donde se almacenarán los productos cargados
    # Esta lista se irá llenando mientras leemos el archivo CSV
    products: List[dict] = []

    # PASO 3: Bloque principal de lectura del CSV con manejo de errores
    try:
        # Abre el archivo CSV en modo lectura ("r")
        # encoding="utf-8" permite leer caracteres especiales y acentos correctamente
        # with asegura que el archivo se cierre automáticamente al terminar
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            # csv.DictReader convierte cada fila en un diccionario
            # Las columnas del CSV se convierten en claves del diccionario
            reader = csv.DictReader(file)

            # PASO 3.1: Iterar sobre cada fila del archivo CSV
            for fila in reader:
                # PASO 3.2: Intentar procesar y agregar cada fila a la lista
                try:
                    # Crear un diccionario con los datos de la fila
                    # Convertir tipos de datos: price a float, stock a int
                    products.append(
                        {
                            "name": fila[
                                "name"
                            ],  # El nombre se mantiene como texto (str)
                            "price": float(
                                fila["price"]
                            ),  # Convertir precio a número decimal
                            "stock": int(
                                fila["stock"]
                            ),  # Convertir cantidad a número entero
                        }
                    )
                # PASO 3.3: Si la conversión de tipos falla, ignorar esa fila y continuar
                except (ValueError, TypeError) as e:
                    # ValueError: Si no se puede convertir a float/int (ej: "abc" a float)
                    # TypeError: Si el tipo de dato es completamente incompatible
                    print(f"Error de formato en fila del CSV: {fila} -> {e}")
                    continue  # Salta a la siguiente fila sin agregar esta

    # PASO 4: Manejo de errores específicos al abrir el archivo
    except FileNotFoundError:
        # Este error ocurre si el archivo se elimina después de verificarlo
        print(f"Archivo no encontrado: {FILE_PATH}")
        return []  # Retorna lista vacía
    except UnicodeDecodeError as e:
        # Este error ocurre si el encoding del archivo no es UTF-8
        print(f"Error de decodificación del CSV: {e}")
        return []  # Retorna lista vacía
    except Exception as e:
        # Captura cualquier otro error no previsto
        print(f"Error desconocido al leer CSV: {e}")
        return []  # Retorna lista vacía

    # PASO 5: Retornar la lista de productos cargados exitosamente
    return products


# ============================================================================
# FUNCIÓN: add_product_csv(products)
# Propósito: Guardar productos en el archivo CSV con dos opciones:
#           1. SOBRESCRIBIR (SI): Reemplaza todo el contenido del archivo
#           2. FUSIONAR (NO): Combina productos nuevos con existentes
# ============================================================================


def add_product_csv(products: List[dict]):
    """
    Guarda una lista de productos en un archivo CSV con opción de sobrescribir o fusionar.

    El usuario puede elegir entre dos opciones:
    - SI: Sobrescribe el archivo de inventario actual con los nuevos productos
    - NO: Fusiona los nuevos productos con los existentes, sumando el stock
           por nombre de producto y actualizando el precio

    Args:
        products (List[dict]): Lista de productos a guardar.
    """

    # PASO 1: Definir la estructura del archivo CSV
    # Estos serán los nombres de las columnas en el archivo
    # El orden define cómo aparecerán los datos en el CSV
    fieldnames = ["name", "price", "stock"]

    # PASO 2: Crear la carpeta "data_base" si no existe
    # exist_ok=True evita error si la carpeta ya existe
    os.makedirs(FOLDER, exist_ok=True)

    # PASO 3: Cargar los productos que ya existen en el archivo CSV
    # Necesitamos esto para poder fusionar datos cuando el usuario elige esa opción
    existing_products = read_products_csv()

    # PASO 4: Convertir la lista de productos existentes en un diccionario
    # Clave = nombre del producto
    # Valor = datos completos del producto (name, price, stock)
    # Esto permite buscar productos por nombre en O(1) en lugar de O(n)
    existing_dict = {p["name"]: p for p in existing_products}

    # PASO 5: Solicitar al usuario que elija entre sobrescribir o fusionar
    # La opción se convierte a minúsculas para comparación consistente
    opcion = (
        input(
            f"¿Sobrescribir el inventario actual? (SI / NO): \n"
            f"Escribe SI para sobrescribir \n"
            f"Escribe NO para fusionar \n\n"
        )
        .strip()  # Elimina espacios al inicio y final
        .lower()  # Convierte a minúsculas (ej: "SI" -> "si")
    )

    # PASO 6: Bloque principal con manejo de errores para guardar el archivo
    try:
        # ====================================================================
        # OPCIÓN 1: SOBRESCRIBIR - Reemplazar todo el contenido del CSV
        # ====================================================================
        if opcion == "si":
            # Abre el archivo en modo escritura ("w")
            # Si el archivo existe, se elimina su contenido
            # Si no existe, se crea uno nuevo
            # encoding="utf-8" permite guardar caracteres especiales
            # newline="" previene saltos de línea extras en Windows
            with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
                # Crear un escritor de CSV que usa diccionarios
                # Especificar fieldnames asegura que las columnas se escriban en el orden correcto
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Escribir la fila de encabezados (name, price, stock)
                writer.writeheader()

                # Escribir cada producto de la lista en una fila del CSV
                for product in products:
                    writer.writerow(
                        {
                            "name": product["name"],
                            "price": product["price"],
                            "stock": product["stock"],
                        }
                    )

            print("Inventario sobrescrito exitosamente.")
            return  # Terminar la función

        # ====================================================================
        # OPCIÓN 2: FUSIONAR - Combinar productos nuevos con existentes
        # ====================================================================
        elif opcion == "no":
            # Crear una copia del diccionario de productos existentes
            # Trabajar con una copia para no modificar el original
            merged = existing_dict.copy()

            # Procesar cada producto nuevo
            for product in products:
                name = product["name"]

                # Si el producto ya existe en el inventario
                if name in merged:
                    # Sumar el stock: cantidad existente + cantidad nueva
                    merged[name]["stock"] += product["stock"]
                    # Actualizar el precio al nuevo valor
                    merged[name]["price"] = product["price"]
                # Si el producto es nuevo (no existe en el inventario)
                else:
                    # Agregarlo como producto nuevo en el diccionario fusionado
                    merged[name] = product

            # Guardar el diccionario fusionado en el archivo CSV
            with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                # merged.values() obtiene solo los productos (valores), no las claves
                for product in merged.values():
                    writer.writerow(
                        {
                            "name": product["name"],
                            "price": product["price"],
                            "stock": product["stock"],
                        }
                    )

            print("Inventario fusionado exitosamente.")
            return  # Terminar la función

        # ====================================================================
        # OPCIÓN 3: ENTRADA INVÁLIDA - El usuario escribió algo que no es SI o NO
        # ====================================================================
        else:
            print("Opción inválida.")

    # PASO 7: Manejo de errores específicos
    except FileNotFoundError as e:
        # Error si no se puede encontrar o crear el archivo
        print(f"Error: Archivo no encontrado al guardar CSV: {e}")
    except UnicodeDecodeError as e:
        # Error si hay problemas con caracteres especiales o encoding
        print(f"Error de decodificación del CSV al guardar: {e}")
    except ValueError as e:
        # Error al intentar convertir tipos de datos
        print(f"Error de conversión de datos al guardar CSV: {e}")
    except Exception as e:
        # Captura cualquier otro error no anticipado
        print(f"Error desconocido al guardar CSV: {e}")
