from collections import namedtuple

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio',       # tipo float
    'fecha_compra'  # tipo date
])

def categoria_mayor_gasto(productos: list[Producto]) -> tuple[str, float] | None:
    """
    Determina la categoría con el mayor gasto total. Devuelve el nombre de la categoría
    junto con el gasto total en esa categoría.

    Si la lista de productos está vacía, devuelve None.

    Parámetros:
    productos (list[Producto]): Lista de productos.

    Devuelve:
    tuple[str, float] | None: La categoría con el mayor gasto total y el gasto total, o None si la lista de productos está vacía.
    """
    # TODO: Borra este comentario y la instrucción pass, e implementa la función
    pass