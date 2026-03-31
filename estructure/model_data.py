from typing import TypedDict


class Product(TypedDict):
    name: str
    price: float | None
    stock: int | None
