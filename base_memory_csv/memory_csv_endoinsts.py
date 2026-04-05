"""Utilidades de persistencia CSV para los datos de estudiantes."""

from estructure.model_data import *
import csv
import os
from typing import List

# Configuración de ruta del archivo CSV
BASE_DIR  = os.path.dirname(__file__)
FOLDER    = os.path.join(BASE_DIR, "data_base")
FILE_PATH = os.path.join(FOLDER, "students.csv")

# Columnas del CSV (tupla — inmutable)
FIELD_NAMES: tuple = ("id", "name", "age", "course", "status")


def read_students_csv() -> List[dict]:
    """Lee los estudiantes del CSV y los retorna como lista de diccionarios."""

    if not os.path.isfile(FILE_PATH):
        print("File does not exist.")
        return []

    students: List[dict] = []

    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    students.append({
                        "id":     int(row["id"]),
                        "name":   row["name"],
                        "age":    int(row["age"]),
                        "course": row["course"],
                        "status": row["status"],
                    })
                except (ValueError, KeyError) as e:
                    print(f"CSV row format error: {row} -> {e}")
                    continue

    except FileNotFoundError:
        print(f"File not found: {FILE_PATH}")
        return []
    except UnicodeDecodeError as e:
        print(f"CSV decode error: {e}")
        return []
    except Exception as e:
        print(f"Unknown error reading CSV: {e}")
        return []

    return students


def save_students_csv(students: List[dict]):
    """Sobreescribe el CSV con la lista actual de estudiantes en memoria.

    Se llama automáticamente después de cada registro, actualización o eliminación.

    Args:
        students (List[dict]): Lista completa de estudiantes a guardar.
    """
    try:
        os.makedirs(FOLDER, exist_ok=True)

        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()

            for student in students:
                writer.writerow({
                    "id":     student["id"],
                    "name":   student["name"],
                    "age":    student["age"],
                    "course": student["course"],
                    "status": student["status"],
                })

    except Exception as e:
        print(f"Unknown error while saving CSV: {e}")
