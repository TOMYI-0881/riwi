"""Módulo de definición de estructuras de datos para la gestión de inventario.

Este módulo define los tipos de datos TypedDict utilizados en toda la aplicación
para representar productos e información estadística del inventario.
"""

from typing import TypedDict, List, Optional, Dict


class Product(TypedDict):
    """
    Estructura de datos que representa un producto en el inventario.

    Atributos:
        name (str): El nombre único del producto en minúsculas.
        price (float | None): El precio unitario del producto. Puede ser None si no se ha asignado.
        stock (int | None): La cantidad disponible del producto. Puede ser None si no se ha asignado.
    """

    name: str
    price: float | None
    stock: int | None


class Statistics(TypedDict):
    """
    Estructura de datos que contiene estadísticas agregadas del inventario.

    Atributos:
        total_units (int): Cantidad total de unidades en el inventario.
        total_value (float): Valor total del inventario (suma de precio * cantidad para cada producto).
        most_expensive_product (Dict[str, object]): Producto con el precio más alto, contiene 'name' y 'price'.
        highest_stock_product (Dict[str, object]): Producto con mayor cantidad en stock, contiene 'name' y 'stock'.
    """
