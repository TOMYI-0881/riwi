"""
Módulo que define los tipos de datos para productos y estadísticas.
"""

from typing import TypedDict, List, Optional, Dict


class Product(TypedDict):
    """
    Representa un producto en el inventario.

    Atributos:
        name (str): Nombre del producto.
        price (float | None): Precio del producto.
        stock (int | None): Cantidad en stock.
    """

    name: str
    price: float | None
    stock: int | None


class Statistics(TypedDict):
    """
    Representa las estadísticas del inventario.

    Atributos:
        total_units (int): Total de unidades en stock.
        total_value (float): Valor total del inventario.
        most_expensive_product (Dict[str, object]): Producto más caro.
        highest_stock_product (Dict[str, object]): Producto con mayor stock.
    """

    total_units: int
    total_value: float
    most_expensive_product: Dict[str, object]
    highest_stock_product: Dict[str, object]
