import logging
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from web.routes import web_bp
from web.constants import (
    MAIL_SERVER,
    MAIL_PORT,
    MAIL_USE_TLS,
    MAIL_USE_SSL,
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER,
    MAIL_SUPPRESS_SEND,
)

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(name)s - %(message)s'
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

app.json.sort_keys = False

# Necesaria para los mensajes flash (feedback de los formularios del admin)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Email (Flask-Mail): si no hay credenciales, el mailer loguea en vez de enviar
app.config.update(
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_USE_TLS=MAIL_USE_TLS,
    MAIL_USE_SSL=MAIL_USE_SSL,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER=MAIL_DEFAULT_SENDER,
    MAIL_SUPPRESS_SEND=MAIL_SUPPRESS_SEND,
)

app.register_blueprint(web_bp)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


if __name__ == '__main__':
    app.run(port=5001, debug=True)
