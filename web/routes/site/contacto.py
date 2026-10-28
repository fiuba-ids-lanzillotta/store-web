from flask import Blueprint, render_template, request, redirect, url_for, flash

from web.mailer import enviar_email_contacto

contacto_bp = Blueprint('contacto', __name__)


@contacto_bp.route('/contacto', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        formulario = request.form
        nombre     = formulario.get('nombre', '').strip()
        email      = formulario.get('email', '').strip()
        mensaje    = formulario.get('mensaje', '').strip()

        if nombre and email and mensaje:
            resultado = enviar_email_contacto(nombre, email, mensaje)

            if resultado['ok']:
                flash('Mensaje enviado. Gracias por contactarte.', 'exito')

                return redirect(url_for('web.site.contacto.index'))

            flash(resultado['error'], 'error')
        else:
            flash('Completa todos los campos.', 'error')

    return render_template('site/contacto.html')
