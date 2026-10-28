from flask import Blueprint, render_template, request, redirect, url_for, flash, abort

from web.services.categorias import (
    obtener_categorias,
    obtener_categoria,
    crear_categoria,
    actualizar_categoria,
    eliminar_categoria,
)

categorias_bp = Blueprint('categorias', __name__)


def _datos_del_formulario() -> dict:
    formulario = request.form

    return {
        'nombre':      formulario.get('nombre', '').strip(),
        'descripcion': formulario.get('descripcion', '').strip(),
    }


@categorias_bp.route('/')
def index():
    return render_template('admin/categorias.html', categorias=obtener_categorias())


@categorias_bp.route('/nueva', methods=['GET', 'POST'])
def nueva():
    if request.method == 'POST':
        resultado = crear_categoria(_datos_del_formulario())

        if resultado['ok']:
            flash('Categoria creada correctamente.', 'exito')

            return redirect(url_for('web.admin.categorias.index'))

        flash(resultado['error'], 'error')

    return render_template('admin/categoria_form.html', categoria=None)


@categorias_bp.route('/<int:categoria_id>/editar', methods=['GET', 'POST'])
def editar(categoria_id):
    categoria = obtener_categoria(categoria_id)

    if not categoria:
        abort(404)

    if request.method == 'POST':
        resultado = actualizar_categoria(categoria_id, _datos_del_formulario())

        if resultado['ok']:
            flash('Categoria actualizada correctamente.', 'exito')

            return redirect(url_for('web.admin.categorias.index'))

        flash(resultado['error'], 'error')

    return render_template('admin/categoria_form.html', categoria=categoria)


@categorias_bp.route('/<int:categoria_id>/eliminar', methods=['POST'])
def eliminar(categoria_id):
    resultado = eliminar_categoria(categoria_id)

    if resultado['ok']:
        flash('Categoria eliminada.', 'exito')
    else:
        flash(resultado['error'], 'error')

    return redirect(url_for('web.admin.categorias.index'))
