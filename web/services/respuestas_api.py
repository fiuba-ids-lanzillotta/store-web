"""Helpers compartidos para interpretar las respuestas de la API (store-api)."""


def mensaje_error_api(response) -> str:
    """Extrae un mensaje legible del cuerpo de error de la API, o uno generico."""
    try:
        datos = response.json()
        errores = datos.get('errors') or []

        if errores:
            textos = [
                error.get('description') or error.get('message') or ''
                for error in errores
            ]

            return ' '.join(texto for texto in textos if texto) or 'Error de validacion.'
    except Exception:
        pass

    return f'Error del servidor (HTTP {response.status_code}).'
