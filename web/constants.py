# ---------------------------------------------------------------
# Datos de ejemplo
# ---------------------------------------------------------------
# Datos hardcodeados que el sitio muestra en su version standalone
# (sin backend). Tienen la misma forma que los DTOs que devuelve
# store-api, para que la integracion no cambie los templates.

CATEGORIAS_EJEMPLO = [
    {'id': 1, 'nombre': 'Electronica',  'descripcion': 'Dispositivos y accesorios electronicos', 'cantidad_productos': 2},
    {'id': 2, 'nombre': 'Hogar',        'descripcion': 'Articulos para el hogar',                'cantidad_productos': 1},
    {'id': 3, 'nombre': 'Indumentaria', 'descripcion': 'Ropa y accesorios',                      'cantidad_productos': 1},
]

PRODUCTOS_EJEMPLO = [
    {'id': 1, 'nombre': 'Auriculares Bluetooth', 'descripcion': 'Auriculares inalambricos con estuche de carga',
     'precio': 25999.99, 'stock': 15, 'imagen_url': '', 'categoria': {'id': 1, 'nombre': 'Electronica'}},
    {'id': 2, 'nombre': 'Teclado Mecanico', 'descripcion': 'Teclado mecanico RGB switches rojos',
     'precio': 45999.0, 'stock': 8, 'imagen_url': '', 'categoria': {'id': 1, 'nombre': 'Electronica'}},
    {'id': 3, 'nombre': 'Lampara de Escritorio', 'descripcion': 'Lampara LED con intensidad regulable',
     'precio': 18500.5, 'stock': 20, 'imagen_url': '', 'categoria': {'id': 2, 'nombre': 'Hogar'}},
    {'id': 4, 'nombre': 'Remera Basica', 'descripcion': 'Remera de algodon unisex',
     'precio': 9999.99, 'stock': 50, 'imagen_url': '', 'categoria': {'id': 3, 'nombre': 'Indumentaria'}},
]
