"""Datos de categorias (version standalone, sin backend).

En la rama `integracion-api` estos mismos services consumen la API
store-api via HTTP; aca devuelven los datos de ejemplo de
web/constants.py con la misma forma que los DTOs de la API.
"""
from web.constants import CATEGORIAS_EJEMPLO

_ERROR_SIN_BACKEND = 'Sin backend: esta accion necesita la API corriendo.'


def obtener_categorias() -> list[dict]:
    """Devuelve las categorias de ejemplo."""
    return CATEGORIAS_EJEMPLO


def obtener_categoria(categoria_id: int) -> dict:
    """Devuelve la categoria de ejemplo con ese id, o {} si no existe."""
    coincidencias = [categoria for categoria in CATEGORIAS_EJEMPLO if categoria['id'] == categoria_id]

    return coincidencias[0] if coincidencias else {}


def crear_categoria(datos: dict) -> dict:
    return {'ok': False, 'error': _ERROR_SIN_BACKEND}


def actualizar_categoria(categoria_id: int, datos: dict) -> dict:
    return {'ok': False, 'error': _ERROR_SIN_BACKEND}


def eliminar_categoria(categoria_id: int) -> dict:
    return {'ok': False, 'error': _ERROR_SIN_BACKEND}
