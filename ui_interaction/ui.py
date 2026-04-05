"""Helpers de interfaz de usuario en consola para el sistema de estudiantes."""

from estructure.model_data import *
from crud.service import service as student_service


def show_menu():
    """Muestra las opciones del menú principal."""
    print(
        "-----------MENU----------- \n"
        "1) Register student \n"
        "2) Show students \n"
        "3) Search student \n"
        "4) Update student \n"
        "5) Delete student \n"
        "6) Statistics \n"
        "7) Exit \n"
        "--------------------------\n"
    )


def request_options() -> int | None:
    """Lee una opción del menú. Retorna None si el valor es inválido."""
    try:
        option = int(input())
        return option
    except ValueError:
        return None


def update_student(student_wait: Student) -> Optional[dict]:
    """Interfaz interactiva para actualizar los datos de un estudiante.

    Sigue el mismo patrón EDIT/SAVE del proyecto base.
    Retorna un diccionario con los campos a actualizar (None en los que no cambian).
    """
    student_local: Student = {
        "id":     student_wait["id"],
        "name":   None,
        "age":    None,
        "course": None,
        "status": None,
    }

    while True:
        print("")
        print("Selected student to update:")
        print("-" * 50)
        print(f"ID     : {student_wait['id']}")
        print(f"Name   : {student_wait['name']}")
        print(f"Age    : {student_wait['age']}")
        print(f"Course : {student_wait['course']}")
        print(f"Status : {student_wait['status'].upper()}")
        print("-" * 50)
        process = input("Enter 'EDIT' to edit or 'SAVE' to save: ").strip().upper()

        if process == "SAVE":
            return student_local

        elif process == "EDIT":
            while True:
                print("")
                print("Edit options:")
                print("1. Edit name")
                print("2. Edit age")
                print("3. Edit course")
                print("4. Edit status")
                print("5. Exit editing")
                edit = input("Select an option (1-5): ").strip()

                try:
                    if edit == "1":
                        new_name = input(f"New name for ID {student_wait['id']}: ").strip()
                        if new_name:
                            student_local["name"] = new_name
                            student_wait["name"]  = new_name
                            print("Name updated.")
                        else:
                            print("Name cannot be empty.")

                    elif edit == "2":
                        new_age = int(input(f"New age for '{student_wait['name']}': "))
                        if 1 <= new_age <= 120:
                            student_local["age"] = new_age
                            student_wait["age"]  = new_age
                            print("Age updated.")
                        else:
                            print("Age must be between 1 and 120.")

                    elif edit == "3":
                        new_course = input(f"New course for '{student_wait['name']}': ").strip()
                        if new_course:
                            student_local["course"] = new_course
                            student_wait["course"]  = new_course
                            print("Course updated.")
                        else:
                            print("Course cannot be empty.")

                    elif edit == "4":
                        new_status = input(f"New status for '{student_wait['name']}' (active / inactive): ").strip().lower()
                        if new_status in ("active", "inactive"):
                            student_local["status"] = new_status
                            student_wait["status"]  = new_status
                            print("Status updated.")
                        else:
                            print("Invalid status. Enter 'active' or 'inactive'.")

                    elif edit == "5":
                        break

                    else:
                        print("Invalid option.")

                except ValueError:
                    print("Enter a valid value.")

        else:
            print("Enter 'EDIT' or 'SAVE'.")


def logic_find_student(text: str):
    """Maneja búsqueda, actualización y eliminación de estudiantes por ID o nombre."""
    value: str = input(f"Enter the student ID or name to {text}: ").strip()
    student = student_service.find_student(value)

    if not student:
        print(f"Student '{value}' not found.")
    else:
        if text == "search":
            print("Student found:")
            print("-" * 50)
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Status : {student['status'].upper()}")
            print("-" * 50)

        if text == "update":
            student_up = update_student(student)
            student_service.update_student_service(student_up)

        if text == "delete":
            student_service.delete_student(str(student["id"]))


def show_statistics():
    """Muestra las estadísticas generales del registro de estudiantes."""
    statistics = student_service.calculate_statistic()

    if statistics is None:
        print("Registry is empty.")
    else:
        print("\nStudent registry statistics:")
        print("-" * 44)
        print(f"{'Total students:':<28} {statistics['total_students']}")
        print(f"{'Active:':<28} {statistics['total_active']}")
        print(f"{'Inactive:':<28} {statistics['total_inactive']}")
        print(f"{'Average age:':<28} {statistics['average_age']}")
        print()
        print("Students per course:")
        print("-" * 44)
        for course, count in statistics["courses"].items():
            print(f"  {course:<30} {count}")
        print("-" * 44)
