import os
from dotenv import load_dotenv

load_dotenv()

# URL base de la API del backend (store-api). Configurable por variable de entorno.
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:5000/store_api')


# ---------------------------------------------------------------
# Datos de ejemplo (fallback sin backend)
# ---------------------------------------------------------------
# Cuando la API no esta disponible, los services devuelven estos
# datos para que el sitio se pueda ver y navegar igual. Tienen la
# misma forma que los DTOs que devuelve store-api.

CATEGORIAS_EJEMPLO = [
    {'id': 1, 'nombre': 'Electronica',  'descripcion': 'Dispositivos y accesorios electronicos', 'cantidad_productos': 2},
    {'id': 2, 'nombre': 'Hogar',        'descripcion': 'Articulos para el hogar',                'cantidad_productos': 1},
    {'id': 3, 'nombre': 'Indumentaria', 'descripcion': 'Ropa y accesorios',                      'cantidad_productos': 1},
]

# Las imagenes son data URIs (como las guarda la API); aca se usan SVGs
# minimos para no inflar el archivo con fotos en base64.

PRODUCTOS_EJEMPLO = [
    {'id': 1, 'nombre': 'Auriculares Bluetooth', 'descripcion': 'Auriculares inalambricos con estuche de carga',
     'precio': 25999.99, 'stock': 15,
     'imagen': 'data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22400%22%20height%3D%22300%22%3E%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%233155d4%22%2F%3E%3Ctext%20x%3D%22200%22%20y%3D%22155%22%20font-family%3D%22sans-serif%22%20font-size%3D%2222%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3EAuriculares%3C%2Ftext%3E%3C%2Fsvg%3E',
     'categoria': {'id': 1, 'nombre': 'Electronica'}},
    {'id': 2, 'nombre': 'Teclado Mecanico', 'descripcion': 'Teclado mecanico RGB switches rojos',
     'precio': 45999.0, 'stock': 8,
     'imagen': 'data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22400%22%20height%3D%22300%22%3E%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%235a32b8%22%2F%3E%3Ctext%20x%3D%22200%22%20y%3D%22155%22%20font-family%3D%22sans-serif%22%20font-size%3D%2222%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3ETeclado%3C%2Ftext%3E%3C%2Fsvg%3E',
     'categoria': {'id': 1, 'nombre': 'Electronica'}},
    {'id': 3, 'nombre': 'Lampara de Escritorio', 'descripcion': 'Lampara LED con intensidad regulable',
     'precio': 18500.5, 'stock': 20,
     'imagen': 'data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22400%22%20height%3D%22300%22%3E%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%23b8892a%22%2F%3E%3Ctext%20x%3D%22200%22%20y%3D%22155%22%20font-family%3D%22sans-serif%22%20font-size%3D%2222%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3ELampara%3C%2Ftext%3E%3C%2Fsvg%3E',
     'categoria': {'id': 2, 'nombre': 'Hogar'}},
    {'id': 4, 'nombre': 'Remera Basica', 'descripcion': 'Remera de algodon unisex',
     'precio': 9999.99, 'stock': 50,
     'imagen': 'data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22400%22%20height%3D%22300%22%3E%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%232a8f5f%22%2F%3E%3Ctext%20x%3D%22200%22%20y%3D%22155%22%20font-family%3D%22sans-serif%22%20font-size%3D%2222%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3ERemera%3C%2Ftext%3E%3C%2Fsvg%3E',
     'categoria': {'id': 3, 'nombre': 'Indumentaria'}},
]
