"""Capa de servicio del sistema de estudiantes: operaciones CRUD y estadísticas."""

from estructure.model_data import *
from base_memory_csv.memory_csv_endoinsts import read_students_csv, save_students_csv


def normalize_name(name: str) -> str:
    """Elimina espacios sobrantes de un nombre y aplica Title Case.

    Ejemplo: '  john   doe  ' -> 'John Doe'
    """
    return " ".join(name.split()).title()


class StudentService:
    """Servicio de gestión de estudiantes con persistencia automática en CSV."""

    def __init__(self):
        self._students: list[Student] = []

    def add_student(self, student: dict):
        """Registra un estudiante. Valida ID y nombre duplicados.
        Guarda automáticamente en CSV.
        """
        # Verificar ID duplicado
        for s in self._students:
            if s["id"] == student["id"]:
                print(f"Error: ID {student['id']} is already in use.")
                return

        # Normalizar nombre y verificar duplicado
        student["name"] = normalize_name(student["name"])
        for s in self._students:
            if normalize_name(s["name"]) == student["name"]:
                print(f"Error: A student named '{student['name']}' already exists.")
                return

        self._students.append(student)
        save_students_csv(self._students)
        print(f"Student '{student['name']}' registered successfully with ID {student['id']}.")

    def get_students(self) -> list[Student]:
        """Retorna la lista de estudiantes en memoria."""
        return self._students

    def show_students(self):
        """Imprime todos los estudiantes en formato de tabla."""
        if not self._students:
            print("No students registered.")
            return

        print("Registered students:")
        print("-" * 66)
        print("{:<5} | {:<22} | {:<4} | {:<18} | {:<8}".format(
            "ID", "NAME", "AGE", "COURSE", "STATUS"
        ))
        print("-" * 66)

        for s in self._students:
            print("{:<5} | {:<22} | {:<4} | {:<18} | {:<8}".format(
                s["id"], s["name"], s["age"], s["course"], s["status"].upper()
            ))

        print("-" * 66)

    def find_student(self, value: str) -> Optional[Student]:
        """Busca un estudiante por ID (si es numérico) o por nombre.

        Retorna el estudiante encontrado o None.
        """
        if not self._students:
            print("No students registered.")
            return None

        if value.isdigit():
            for s in self._students:
                if s["id"] == int(value):
                    return s
        else:
            for s in self._students:
                if normalize_name(s["name"]) == normalize_name(value):
                    return s

        return None

    def update_student_service(self, up_student: Student):
        """Actualiza los campos no nulos de un estudiante existente.
        Guarda automáticamente en CSV.
        """
        change = 0

        for i, s in enumerate(self._students):
            if s["id"] == up_student["id"]:

                if up_student.get("name") is not None:
                    new_name = normalize_name(up_student["name"])
                    # Verificar duplicado solo si el nombre cambia
                    if normalize_name(s["name"]) != new_name:
                        for other in self._students:
                            if normalize_name(other["name"]) == new_name:
                                print(f"Error: A student named '{new_name}' already exists.")
                                return
                    self._students[i]["name"] = new_name
                    change += 1

                if up_student.get("age") is not None:
                    self._students[i]["age"] = up_student["age"]
                    change += 1

                if up_student.get("course") is not None:
                    self._students[i]["course"] = up_student["course"]
                    change += 1

                if up_student.get("status") is not None:
                    self._students[i]["status"] = up_student["status"]
                    change += 1

                if change == 0:
                    print("No changes were made to the student.")
                else:
                    save_students_csv(self._students)
                    print("Student updated successfully.")
                return

        print(f"Student with ID {up_student.get('id')} not found.")

    def delete_student(self, value: str):
        """Elimina un estudiante por ID o nombre.
        Guarda automáticamente en CSV.
        """
        if not self._students:
            print("No students registered.")
            return

        student = self.find_student(value)

        if student:
            self._students.remove(student)
            save_students_csv(self._students)
            print(f"Student '{student['name']}' (ID {student['id']}) deleted successfully.")
        else:
            print(f"Student '{value}' not found.")

    def calculate_statistic(self) -> Optional[Statistics]:
        """Calcula las estadísticas generales del registro de estudiantes."""
        if not self._students:
            return None

        total_active   = 0
        total_inactive = 0
        total_age      = 0
        courses        = {}

        for s in self._students:
            if s["status"] == "active":
                total_active += 1
            else:
                total_inactive += 1

            total_age += s["age"]

            if s["course"] in courses:
                courses[s["course"]] += 1
            else:
                courses[s["course"]] = 1

        return {
            "total_students": len(self._students),
            "total_active":   total_active,
            "total_inactive": total_inactive,
            "average_age":    round(total_age / len(self._students), 1),
            "courses":        courses,
        }

    def read_student_memory_csv(self):
        """Carga los estudiantes desde el CSV a memoria (limpia el registro primero)."""
        self._students.clear()
        self._students.extend(read_students_csv())


# Instancia compartida (singleton) para uso en app y ui
service = StudentService()
