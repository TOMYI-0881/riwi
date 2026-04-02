"""Inventory service layer: product CRUD and statistics operations."""

from estructure.model_data import *
from base_memory_csv.memory_csv_endoinsts import read_products_csv


class InventoryService:
    """Stateful inventory service with in-memory list and CSV operations."""

    def __init__(self):
        self._inventory: list[Product] = []

    def add_product_list(self, product: dict):
        """Add product to inventory or update existing product stock and price."""
        for i in self._inventory:
            if i["name"] == product["name"]:
                i["stock"] += product["stock"]
                i["price"] = product["price"]
                return

        self._inventory.append(product)

    def get_inventory(self):
        """Return live inventory list reference."""
        return self._inventory

    def show_products(self):
        """Print inventory products in a formatted table."""
        if not self._inventory:
            print("No hay productos en el inventario.")
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
        """Find a product by name in inventory; returns product dict or None."""
        if not self._inventory:
            print("No hay productos en el inventario.")
            return None

        for i in self._inventory:
            if i["name"] == name:
                return i

        return None

    def update_product_inventory(self, up_product: Product):
        """Update inventory product fields by name with non-None values."""
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
                    print("Producto actualizado correctamente.")
                return

        print(
            f"El producto '{up_product.get('name', '')}' no se encontró en el inventario."
        )

    def delete_product_inventory(self, name: str):
        """Delete a product by name from inventory."""
        if not self._inventory:
            print("No hay productos en el inventario.")
            return

        for item in self._inventory:
            if item["name"] == name:
                self._inventory.remove(item)
                print(f"Producto '{name}' eliminado exitosamente.")
                return

        print(f"El producto '{name}' no se encontró en el inventario.")

    def calculate_statistic(self) -> Optional[Statistics]:
        """Compute summary metrics from inventory products."""
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
        """Clear in-memory inventory list."""
        self._inventory.clear()

    def read_product_memory_csv(self):
        """Load products from CSV file into inventory (clears existing data first)."""
        self.clear_inventory()
        self._inventory.extend(read_products_csv())
        print("Inventario cargado desde CSV correctamente.")


# Shared singleton instance for app/ui usage
service = InventoryService()
