"""Datos de productos (version standalone, sin backend).

En la rama `integracion-api` estos mismos services consumen la API
store-api via HTTP; aca devuelven los datos de ejemplo de
web/constants.py con la misma forma que los DTOs de la API.
"""
import base64

from web.constants import PRODUCTOS_EJEMPLO

_ERROR_SIN_BACKEND = 'Sin backend: esta accion necesita la API corriendo.'


def archivo_a_data_uri(archivo) -> str | None:
    """Convierte un FileStorage de Flask en data URI base64, o None si esta vacio."""
    if not archivo or not archivo.filename:
        return None

    contenido = archivo.read()

    if not contenido:
        return None

    mime = archivo.mimetype or 'image/jpeg'

    if mime == 'image/jpg':
        mime = 'image/jpeg'

    codificado = base64.b64encode(contenido).decode('ascii')

    return f'data:{mime};base64,{codificado}'


def obtener_productos(categoria_id: int = None, texto: str = None) -> list[dict]:
    """Devuelve los productos de ejemplo, con los mismos filtros que la API."""
    resultado = PRODUCTOS_EJEMPLO

    if categoria_id:
        resultado = [producto for producto in resultado if producto['categoria']['id'] == categoria_id]

    if texto:
        resultado = [producto for producto in resultado if texto.lower() in producto['nombre'].lower()]

    return resultado


def obtener_producto(producto_id: int) -> dict:
    """Devuelve el producto de ejemplo con ese id, o {} si no existe."""
    coincidencias = [producto for producto in PRODUCTOS_EJEMPLO if producto['id'] == producto_id]

    return coincidencias[0] if coincidencias else {}


def crear_producto(datos: dict) -> dict:
    return {'ok': False, 'error': _ERROR_SIN_BACKEND}


def actualizar_producto(producto_id: int, datos: dict) -> dict:
    return {'ok': False, 'error': _ERROR_SIN_BACKEND}


def eliminar_producto(producto_id: int) -> dict:
    return {'ok': False, 'error': _ERROR_SIN_BACKEND}
