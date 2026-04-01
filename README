# Product Inventory System

## Description

This project is a **product inventory management system** developed in Python. It allows you to add, display, search, update, and delete products, as well as calculate statistics and save/load data in CSV files. The interface is entirely console-based, making it simple and efficient for basic use.

The system is **modularized** to facilitate maintenance and expansion, with clear separation between business logic, user interface, and data persistence.

## Features

- **Complete Product Management**: Add, list, search, update, and delete products.
- **Data Validation**: Inputs validated for non-negative prices and stock.
- **Inventory Statistics**: Calculation of total units, total value, most expensive product, and highest stock product.
- **CSV Persistence**: Save and load inventory from CSV files, with overwrite or merge options.
- **Console Interface**: Easy-to-use interactive menu.
- **Modularity**: Code organized in independent modules (structure, CRUD, UI, persistence).

## Requirements

- Python 3.8 or higher.
- No additional external libraries required (uses only standard modules like `csv`, `os`, `typing`).

## Installation

1. Clone or download the repository to your local machine.
2. Ensure Python is installed.
3. Run the main file `app.py` from the project root:

   ```bash
   python app.py
   ```

No additional dependencies need to be installed, as the project uses only Python's standard libraries.

## Usage

When running `app.py`, you'll see a menu with the following options:

1. **Add Product**: Enter name, price, and stock. If the product already exists, stock is updated.
2. **Show Products**: List all products in a formatted table.
3. **Search Product**: Find a product by name and display its details.
4. **Update Product**: Modify price or stock of an existing product.
5. **Delete Product**: Remove a product from inventory.
6. **Statistics**: Display general inventory metrics.
7. **Save CSV**: Export current inventory to a CSV file (choose overwrite or merge).
8. **Load CSV**: Import products from a CSV file into inventory.
9. **Exit**: Close the application.

### Usage Example

- Add a product: Select option 1, enter "apple", price 2.50, stock 10.
- Show products: Select option 2 to view the table.
- Search: Select option 3, enter "apple" to view details.
- Statistics: Select option 6 to view totals and highlighted products.

## Project Structure

```
riwi2/
├── app.py                          # Main file that runs the menu
├── estructure/
│   └── model_data.py               # Type definitions (Product, Statistics)
├── crud/
│   └── service.py                  # CRUD operations and statistics logic
├── ui_interaction/
│   └── ui.py                       # Console user interface
├── base_memory_csv/
│   ├── memory_csv_endoinsts.py     # Functions to save/load CSV
│   └── data_base/
│       └── inventory.csv           # CSV file for persistence (auto-created)
└── README.md                       # This file
```

### Module Descriptions

- **app.py**: Entry point. Handles the menu loop and calls functions from other modules.
- **estructure/model_data.py**: Defines TypedDict classes for Product and Statistics, ensuring strong typing.
- **crud/service.py**: Contains functions to add, search, update, delete products, and calculate statistics. Manages the global inventory list.
- **ui_interaction/ui.py**: Handles user interaction: displays menus, requests inputs, and validates data.
- **base_memory_csv/memory_csv_endoinsts.py**: Responsible for persistence. Reads and writes CSV files, with logic to merge or overwrite data.

## Detailed Features

### Product Management

- Products are stored in a global in-memory list.
- Each product has name (string), price (float), and stock (int).
- Full CRUD operations with validations.

### Statistics

- Calculates total units, total value (accumulated price \* stock).
- Identifies the most expensive product and the one with highest stock.

### Persistence

- Data is saved to `base_memory_csv/data_base/inventory.csv`.
- When saving, choose to overwrite everything or merge by name (adds stock if exists).
- When loading, replaces the current inventory.

## Contributing

If you want to contribute:

1. Fork the project.
2. Create a branch for your feature (e.g., `git checkout -b new-feature`).
3. Make changes and test.
4. Send a pull request with a clear description.

Make sure to follow best practices: English docstrings, strong typing, and manual testing.

## License

This project is open-source. Use it freely for learning or personal projects. It comes with no warranty of any kind.

## Final Notes

This system is ideal for small businesses or as a base for more complex applications. If you find bugs or have ideas for improvements (like a graphical interface or database), let me know!

Developed with pure Python for simplicity and portability.
