"""Consumo de la API (store-api) para los datos de productos."""
import base64
import logging
import requests

from web.constants import API_BASE_URL, PRODUCTOS_EJEMPLO
from web.services.respuestas_api import mensaje_error_api

logger = logging.getLogger(__name__)

_ERROR_CONEXION = 'No se pudo conectar con el servidor. Intenta mas tarde.'


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


def _productos_de_ejemplo(categoria_id: int = None, texto: str = None) -> list[dict]:
    """Aplica sobre los datos de ejemplo los mismos filtros que la API."""
    resultado = PRODUCTOS_EJEMPLO

    if categoria_id:
        resultado = [producto for producto in resultado if producto['categoria']['id'] == categoria_id]

    if texto:
        resultado = [producto for producto in resultado if texto.lower() in producto['nombre'].lower()]

    return resultado


def _producto_de_ejemplo(producto_id: int) -> dict:
    coincidencias = [producto for producto in PRODUCTOS_EJEMPLO if producto['id'] == producto_id]

    return coincidencias[0] if coincidencias else {}


def obtener_productos(categoria_id: int = None, texto: str = None) -> list[dict]:
    """
    Consume la API para obtener la lista de productos.
    Si la API no responde, devuelve los datos de ejemplo de constants.
    """
    try:
        parametros = {}

        if categoria_id:
            parametros['categoria_id'] = categoria_id

        if texto:
            parametros['q'] = texto

        response = requests.get(f'{API_BASE_URL}/productos', params=parametros, timeout=10)

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')
    except Exception as error:
        logger.error(f'Error al obtener productos: {error}')

    return _productos_de_ejemplo(categoria_id=categoria_id, texto=texto)


def obtener_producto(producto_id: int) -> dict:
    """Devuelve el producto; si la API no responde, busca en los datos de ejemplo."""
    try:
        response = requests.get(f'{API_BASE_URL}/productos/{producto_id}', timeout=10)

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')
    except Exception as error:
        logger.error(f'Error al obtener el producto {producto_id}: {error}')

    return _producto_de_ejemplo(producto_id)


def crear_producto(datos: dict) -> dict:
    """Crea un producto via POST /productos."""
    try:
        response = requests.post(f'{API_BASE_URL}/productos', json=datos, timeout=15)

        if response.status_code == 201:
            return {'ok': True}

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')

        return {'ok': False, 'error': _ERROR_CONEXION}

    except Exception as error:
        logger.error(f'Error al crear producto: {error}')

        return {'ok': False, 'error': 'Ocurrio un error al agregar el producto.'}


def actualizar_producto(producto_id: int, datos: dict) -> dict:
    """Actualiza un producto via PUT /productos/<id>."""
    try:
        response = requests.put(f'{API_BASE_URL}/productos/{producto_id}', json=datos, timeout=15)

        if response.status_code == 200:
            return {'ok': True}

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')

        return {'ok': False, 'error': _ERROR_CONEXION}

    except Exception as error:
        logger.error(f'Error al actualizar producto: {error}')

        return {'ok': False, 'error': 'Ocurrio un error al guardar el producto.'}


def eliminar_producto(producto_id: int) -> dict:
    """Elimina un producto via DELETE /productos/<id>."""
    try:
        response = requests.delete(f'{API_BASE_URL}/productos/{producto_id}', timeout=10)

        if response.status_code == 204:
            return {'ok': True}

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')

        return {'ok': False, 'error': _ERROR_CONEXION}

    except Exception as error:
        logger.error(f'Error al eliminar producto: {error}')

        return {'ok': False, 'error': 'Ocurrio un error al eliminar el producto.'}
