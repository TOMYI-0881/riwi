"""Definición del modelo de datos del sistema de estudiantes."""

from typing import TypedDict, Optional, Dict


class Student(TypedDict):
    """
    Representa un estudiante en el sistema.

    Atributos:
        id      (int): Identificador único del estudiante.
        name    (str): Nombre completo del estudiante.
        age     (int): Edad del estudiante.
        course  (str): Curso o programa en el que está matriculado.
        status  (str): Estado — 'active' o 'inactive'.
    """
    id:     int
    name:   str
    age:    int
    course: str
    status: str


class Statistics(TypedDict):
    """
    Representa las estadísticas del registro de estudiantes.

    Atributos:
        total_students (int)          : Total de estudiantes registrados.
        total_active   (int)          : Estudiantes activos.
        total_inactive (int)          : Estudiantes inactivos.
        average_age    (float)        : Promedio de edad.
        courses        (Dict[str,int]): Cantidad de estudiantes por curso.
    """
    total_students: int
    total_active:   int
    total_inactive: int
    average_age:    float
    courses:        Dict[str, int]
