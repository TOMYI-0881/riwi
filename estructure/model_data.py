from typing import TypedDict, List, Optional, Dict


class Product(TypedDict):
    name: str
    price: float | None
    stock: int | None


class Statistics(TypedDict):
    total_units: int
    total_value: float
    most_expensive_product: Dict[str, object]
    highest_stock_product: Dict[str, object]
