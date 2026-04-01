# Sistema de Inventario de Productos

## Descripción

Este proyecto es un sistema de gestión de inventario de productos desarrollado en Python. Permite agregar, mostrar, buscar, actualizar y eliminar productos, además de calcular estadísticas y guardar/cargar datos en archivos CSV. La interfaz es completamente en consola, lo que lo hace simple y eficiente para uso básico.

El sistema está modularizado para facilitar el mantenimiento y la expansión, con separación clara entre lógica de negocio, interfaz de usuario y persistencia de datos.

## Características

- **Gestión completa de productos**: Agregar, listar, buscar, actualizar y eliminar productos.
- **Validación de datos**: Entradas validadas para precios y stock no negativos.
- **Estadísticas del inventario**: Cálculo de unidades totales, valor total, producto más caro y producto con mayor stock.
- **Persistencia en CSV**: Guardar y cargar inventario desde archivos CSV, con opciones de sobrescribir o fusionar.
- **Interfaz en consola**: Menú interactivo fácil de usar.
- **Modularidad**: Código organizado en módulos independientes (estructura, CRUD, UI, persistencia).

## Requisitos

- Python 3.8 o superior.
- No se requieren bibliotecas externas adicionales (usa solo módulos estándar como `csv`, `os`, `typing`).

## Instalación

1. Clona o descarga el repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. Ejecuta el archivo principal `app.py` desde la raíz del proyecto:

   ```bash
   python app.py
   ```

No es necesario instalar dependencias adicionales, ya que el proyecto usa solo bibliotecas estándar de Python.

## Uso

Al ejecutar `app.py`, verás un menú con las siguientes opciones:

1. **Agregar producto**: Ingresa nombre, precio y stock. Si el producto ya existe, se actualiza el stock.
2. **Mostrar productos**: Lista todos los productos en una tabla formateada.
3. **Buscar producto**: Encuentra un producto por nombre y muestra sus detalles.
4. **Actualizar producto**: Modifica precio o stock de un producto existente.
5. **Eliminar producto**: Remueve un producto del inventario.
6. **Estadísticas**: Muestra métricas generales del inventario.
7. **Guardar CSV**: Exporta el inventario actual a un archivo CSV (elige sobrescribir o fusionar).
8. **Cargar CSV**: Importa productos desde un archivo CSV al inventario.
9. **Salir**: Cierra la aplicación.

### Ejemplo de uso

- Agregar un producto: Selecciona opción 1, ingresa "manzana", precio 2.50, stock 10.
- Mostrar productos: Selecciona opción 2 para ver la tabla.
- Buscar: Selecciona opción 3, ingresa "manzana" para ver detalles.
- Estadísticas: Selecciona opción 6 para ver totales y productos destacados.

## Estructura del Proyecto

```
riwi2/
├── app.py                          # Archivo principal que ejecuta el menú
├── estructure/
│   └── model_data.py               # Definición de tipos (Product, Statistics)
├── crud/
│   └── service.py                  # Lógica de operaciones CRUD y estadísticas
├── ui_interaction/
│   └── ui.py                       # Interfaz de usuario en consola
├── base_memory_csv/
│   ├── memory_csv_endoinsts.py     # Funciones para guardar/cargar CSV
│   └── data_base/
│       └── inventory.csv           # Archivo CSV para persistencia (creado automáticamente)
└── README.md                       # Este archivo
```

### Descripción de Módulos

- **app.py**: Punto de entrada. Maneja el bucle del menú y llama a funciones de otros módulos.
- **estructure/model_data.py**: Define las clases TypedDict para Product y Statistics, asegurando tipado fuerte.
- **crud/service.py**: Contiene funciones para agregar, buscar, actualizar, eliminar productos y calcular estadísticas. Gestiona la lista global de inventario.
- **ui_interaction/ui.py**: Maneja la interacción con el usuario: muestra menús, solicita inputs y valida datos.
- **base_memory_csv/memory_csv_endoinsts.py**: Encargado de la persistencia. Lee y escribe archivos CSV, con lógica para fusionar o sobrescribir datos.

## Funcionalidades Detalladas

### Gestión de Productos

- Los productos se almacenan en una lista global en memoria.
- Cada producto tiene nombre (string), precio (float) y stock (int).
- Operaciones CRUD completas con validaciones.

### Estadísticas

- Calcula unidades totales, valor total (precio \* stock acumulado).
- Identifica el producto más caro y el de mayor stock.

### Persistencia

- Los datos se guardan en `base_memory_csv/data_base/inventory.csv`.
- Al guardar, elige entre sobrescribir todo o fusionar por nombre (suma stock si existe).
- Al cargar, reemplaza el inventario actual.

## Contribución

Si deseas contribuir:

1. Haz un fork del proyecto.
2. Crea una rama para tu feature (ej. `git checkout -b nueva-funcionalidad`).
3. Realiza cambios y prueba.
4. Envía un pull request con descripción clara.

Asegúrate de seguir buenas prácticas: docstrings en español, tipado fuerte y pruebas manuales.

## Licencia

Este proyecto es de código abierto. Úsalo libremente para aprendizaje o proyectos personales. No incluye garantía de ningún tipo.

## Notas Finales

Este sistema es ideal para pequeños negocios o como base para aplicaciones más complejas. Si encuentras bugs o tienes ideas para mejoras (como interfaz gráfica o base de datos), ¡házmelo saber!

Desarrollado con Python puro para simplicidad y portabilidad.
