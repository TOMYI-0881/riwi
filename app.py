"""Punto de entrada principal del sistema de gestión de estudiantes."""

from estructure.model_data import Student
from crud.service import service as student_service
from ui_interaction.ui import *
from base_memory_csv.memory_csv_endoinsts import read_students_csv


def menu_base():
    """Muestra el menú y ejecuta las acciones del usuario.

    Itera hasta que el usuario selecciona salir. Maneja el registro,
    búsqueda, actualización, eliminación y estadísticas de estudiantes.
    """
    student_service.read_student_memory_csv()

    while True:
        print("")
        show_menu()
        option = request_options()

        if option == 1:
            student_id     = -1
            student_name   = ""
            student_age    = -1
            student_course = ""
            student_status = ""
            student_wait: Student = {}

            while True:
                try:
                    if student_id < 0:
                        student_id = int(input("Student ID: "))
                        if student_id >= 0:
                            student_wait["id"] = student_id
                        else:
                            print("ID must be 0 or greater.")
                            student_id = -1
                            continue

                    if not student_name:
                        student_name = input("Full name: ").strip()
                        if student_name:
                            student_wait["name"] = student_name
                        else:
                            print("Name cannot be empty.")
                            continue

                    if student_age < 0:
                        student_age = int(input(f"Age of '{student_name}': "))
                        if 1 <= student_age <= 120:
                            student_wait["age"] = student_age
                        else:
                            print("Age must be between 1 and 120.")
                            student_age = -1
                            continue

                    if not student_course:
                        student_course = input(f"Course for '{student_name}': ").strip()
                        if student_course:
                            student_wait["course"] = student_course
                        else:
                            print("Course cannot be empty.")
                            continue

                    if not student_status:
                        student_status = input(f"Status for '{student_name}' (active / inactive): ").strip().lower()
                        if student_status in ("active", "inactive"):
                            student_wait["status"] = student_status
                        else:
                            print("Invalid status. Enter 'active' or 'inactive'.")
                            student_status = ""
                            continue

                    break

                except ValueError:
                    print("Enter a valid value.")

            student_service.add_student(student_wait)

        elif option == 2:
            student_service.show_students()

        elif option == 3:
            logic_find_student("search")

        elif option == 4:
            logic_find_student("update")

        elif option == 5:
            logic_find_student("delete")

        elif option == 6:
            show_statistics()

        elif option == 7:
            print("Exiting...")
            break

        elif not option:
            print("Enter a valid value.")

        else:
            print("Enter a number from 1 to 7.")


if __name__ == "__main__":
    menu_base()
