"""Envío de emails (Flask-Mail / SMTP).

Env-gated: si no hay credenciales (`MAIL_USERNAME`/`MAIL_PASSWORD`) o
`MAIL_SUPPRESS_SEND=true`, no se envía nada: se loguea el mensaje (modo dev).
"""
import logging
from flask import current_app, render_template
from flask_mail import Mail, Message

from web.constants import (
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_SUPPRESS_SEND,
    CONTACTO_EMAIL,
)

logger = logging.getLogger(__name__)


def _mail_configurado() -> bool:
    return bool(MAIL_USERNAME and MAIL_PASSWORD) and not MAIL_SUPPRESS_SEND


def enviar_email_contacto(nombre: str, email: str, mensaje: str) -> dict:
    """
    Envía el mensaje del formulario de contacto a la casilla del admin
    (CONTACTO_EMAIL). Devuelve {'ok': True} o {'ok': False, 'error': ...}.
    """
    if not _mail_configurado():
        logger.warning(f'[contacto] Email deshabilitado; mensaje de {nombre} <{email}>:\n{mensaje}')

        return {'ok': True}

    try:
        correo = Message(
            subject=f'Contacto desde el sitio - {nombre}',
            recipients=[CONTACTO_EMAIL],
            reply_to=email,
            html=render_template('emails/contacto.html', nombre=nombre, email=email, mensaje=mensaje),
        )

        Mail(current_app).send(correo)

        return {'ok': True}

    except Exception as error:
        logger.error(f'Error al enviar el email de contacto: {error}')

        return {'ok': False, 'error': 'No se pudo enviar el mensaje. Intenta mas tarde.'}
