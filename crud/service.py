"""Capa de servicio de inventario: operaciones CRUD y cálculo de estadísticas.

Este módulo contiene la clase InventoryService que gestiona todas las operaciones
sobre los productos del inventario: agregar, leer, actualizar, eliminar y calcular
estadísticas. Mantiene el estado del inventario en memoria y proporciona una
interfaz para la persistencia en CSV.
"""

from estructure.model_data import *
from base_memory_csv.memory_csv_endoinsts import read_products_csv


class InventoryService:
    """
    Servicio de inventario con estado: mantiene una lista de productos en memoria
    y proporciona operaciones CRUD, cálculo de estadísticas e integración con CSV.

    La instancia es un singleton compartido entre la aplicación y la interfaz de usuario.
    """

    def __init__(self):
        self._inventory: list[Product] = []

    def add_product_list(self, product: dict):
        """Agrega un producto al inventario o actualiza uno existente.

        Si el producto ya existe por nombre, incrementa el stock y actualiza el precio.
        Si no existe, lo agrega como nuevo producto.

        Args:
            product (dict): Diccionario con las claves 'name', 'price' y 'stock'.
        """
        for i in self._inventory:
            if i["name"] == product["name"]:
                i["stock"] += product["stock"]
                i["price"] = product["price"]
                return

        self._inventory.append(product)

    def get_inventory(self):
        """
        Retorna la referencia directa a la lista del inventario actual.

        Returns:
            list[Product]: La lista de productos en inventario.
        """
        return self._inventory

    def show_products(self):
        """
        Muestra los productos del inventario en una tabla formateada.

        Si el inventario está vacío, muestra un mensaje informativo.
        La tabla incluye número de orden, nombre, precio y cantidad disponible.
        """
        if not self._inventory:
            print("Sin productos en el inventario.")
            return

        print("Productos en el inventario:")
        print("-" * 50)
        print(
            "{:<3} | {:<15} | {:<10} | {:<8}".format("No", "NOMBRE", "PRECIO", "STOCK")
        )
        print("-" * 50)

        for idx, product in enumerate(self._inventory, start=1):
            price = float(product["price"]) if product["price"] is not None else 0.0
            stock = int(product["stock"]) if product["stock"] is not None else 0
            print(
                "{:<3} | {:<15} | ${:<9.2f} | {:<8}".format(
                    idx, product["name"], price, stock
                )
            )

        print("-" * 50)

    def find_product(self, name: str) -> Optional[Product]:
        """
        Busca un producto por nombre en el inventario.

        Args:
            name (str): El nombre del producto a buscar (en minúsculas).

        Returns:
            Optional[Product]: El diccionario del producto si se encuentra, None en caso contrario.
        """
        if not self._inventory:
            print("No hay productos en el inventario.")
            return None

        for i in self._inventory:
            if i["name"] == name:
                return i

        return None

    def update_product_inventory(self, up_product: Product):
        """
        Actualiza los campos de un producto en el inventario por nombre.

        Solo actualiza los valores que no sean None en el producto proporcionado.
        Muestra mensajes informativos sobre el resultado de la operación.

        Args:
            up_product (Product): Diccionario con el nombre del producto y los campos a actualizar.
        """
        change = 0
        for i, v in enumerate(self._inventory):
            if v["name"] == up_product["name"]:
                if up_product.get("price") is not None:
                    self._inventory[i]["price"] = up_product["price"]
                    change += 1
                if up_product.get("stock") is not None:
                    self._inventory[i]["stock"] = up_product["stock"]
                    change += 1

                if change == 0:
                    print("No se realizaron cambios en el producto.")
                else:
                    print("Producto actualizado exitosamente.")
                return

        print(
            f"El producto '{up_product.get('name', '')}' no se encontró en el inventario."
        )

    def delete_product_inventory(self, name: str):
        """
        Elimina un producto del inventario por nombre.

        Muestra un mensaje de confirmación si el producto se eliminó correctamente,
        o un mensaje de error si el producto no fue encontrado.

        Args:
            name (str): El nombre del producto a eliminar.
        """
        if not self._inventory:
            print("Sin productos en el inventario.")
            return

        for item in self._inventory:
            if item["name"] == name:
                self._inventory.remove(item)
                print(f"Producto '{name}' eliminado exitosamente.")
                return

        print(f"El producto '{name}' no se encontró en el inventario.")

    def calculate_statistic(self) -> Optional[Statistics]:
        """
        Calcula métricas resumidas del inventario.

        Computa:
        - Total de unidades en stock
        - Valor total del inventario (precio * cantidad)
        - Producto más costoso
        - Producto con mayor cantidad en stock

        Returns:
            Optional[Statistics]: Diccionario con las estadísticas si hay productos, None si el inventario está vacío.
        """
        if not self._inventory:
            return None

        total_units = 0
        total_value = 0.0
        most_expensive_product = self._inventory[0]
        highest_stock_product = self._inventory[0]

        for i in self._inventory:
            total_units += i["stock"]
            total_value += i["price"] * i["stock"]

            if i["price"] > most_expensive_product["price"]:
                most_expensive_product = i
            if i["stock"] > highest_stock_product["stock"]:
                highest_stock_product = i

        return {
            "total_units": total_units,
            "total_value": total_value,
            "most_expensive_product": {
                "name": most_expensive_product["name"],
                "price": most_expensive_product["price"],
            },
            "highest_stock_product": {
                "name": highest_stock_product["name"],
                "stock": highest_stock_product["stock"],
            },
        }

    def clear_inventory(self):
        """
        Limpia la lista del inventario en memoria eliminando todos los productos.
        """
        self._inventory.clear()

    def read_product_memory_csv(self):
        """
        Carga los productos desde un archivo CSV al inventario.

        Limpia el inventario actual antes de cargar los datos del archivo CSV,
        asegurando que no haya duplicados o datos inconsistentes.
        """
        self.clear_inventory()
        self._inventory.extend(read_products_csv())


# Instancia singleton compartida para uso de la aplicación e interfaz de usuario
service = InventoryService()
