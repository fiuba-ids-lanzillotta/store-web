"""Consumo de la API (store-api) para los datos de categorias."""
import logging
import requests

from web.constants import API_BASE_URL, CATEGORIAS_EJEMPLO
from web.services.respuestas_api import mensaje_error_api

logger = logging.getLogger(__name__)

_ERROR_CONEXION = 'No se pudo conectar con el servidor. Intenta mas tarde.'


def obtener_categorias() -> list[dict]:
    """
    Consume la API para obtener la lista de categorias.
    Si la API no responde, devuelve los datos de ejemplo de constants.
    """
    try:
        response = requests.get(f'{API_BASE_URL}/categorias', timeout=10)

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')
    except Exception as error:
        logger.error(f'Error al obtener categorias: {error}')

    return CATEGORIAS_EJEMPLO


def obtener_categoria(categoria_id: int) -> dict:
    """Devuelve la categoria; si la API no responde, busca en los datos de ejemplo."""
    try:
        response = requests.get(f'{API_BASE_URL}/categorias/{categoria_id}', timeout=10)

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')
    except Exception as error:
        logger.error(f'Error al obtener la categoria {categoria_id}: {error}')

    coincidencias = [categoria for categoria in CATEGORIAS_EJEMPLO if categoria['id'] == categoria_id]

    return coincidencias[0] if coincidencias else {}


def crear_categoria(datos: dict) -> dict:
    """Crea una categoria via POST /categorias."""
    try:
        response = requests.post(f'{API_BASE_URL}/categorias', json=datos, timeout=15)

        if response.status_code == 201:
            return {'ok': True}

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')

        return {'ok': False, 'error': _ERROR_CONEXION}

    except Exception as error:
        logger.error(f'Error al crear categoria: {error}')

        return {'ok': False, 'error': 'Ocurrio un error al agregar la categoria.'}


def actualizar_categoria(categoria_id: int, datos: dict) -> dict:
    """Actualiza una categoria via PUT /categorias/<id>."""
    try:
        response = requests.put(f'{API_BASE_URL}/categorias/{categoria_id}', json=datos, timeout=15)

        if response.status_code == 200:
            return {'ok': True}

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')

        return {'ok': False, 'error': _ERROR_CONEXION}

    except Exception as error:
        logger.error(f'Error al actualizar categoria: {error}')

        return {'ok': False, 'error': 'Ocurrio un error al guardar la categoria.'}


def eliminar_categoria(categoria_id: int) -> dict:
    """Elimina una categoria via DELETE /categorias/<id> (409 si tiene productos)."""
    try:
        response = requests.delete(f'{API_BASE_URL}/categorias/{categoria_id}', timeout=10)

        if response.status_code == 204:
            return {'ok': True}

        return {'ok': False, 'error': mensaje_error_api(response)}

    except requests.exceptions.ConnectionError:
        logger.error(f'No se pudo conectar con la API en {API_BASE_URL}')

        return {'ok': False, 'error': _ERROR_CONEXION}

    except Exception as error:
        logger.error(f'Error al eliminar categoria: {error}')

        return {'ok': False, 'error': 'Ocurrio un error al eliminar la categoria.'}
