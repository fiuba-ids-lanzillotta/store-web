from flask import Blueprint, render_template, request, redirect, url_for, flash, abort

from web.services.productos import (
    obtener_productos,
    obtener_producto,
    crear_producto,
    actualizar_producto,
    eliminar_producto,
    archivo_a_data_uri,
)
from web.services.categorias import obtener_categorias

productos_bp = Blueprint('productos', __name__)


def _datos_del_formulario(producto_actual: dict = None) -> dict:
    """
    Toma los campos del formulario HTML y los normaliza para la API.
    La imagen llega como archivo y se convierte a data URI base64; si no se
    sube una nueva en la edicion, se conserva la actual.
    """
    formulario = request.form
    imagen     = archivo_a_data_uri(request.files.get('imagen'))

    if imagen is None and producto_actual:
        imagen = producto_actual.get('imagen') or ''

    return {
        'nombre':       formulario.get('nombre', '').strip(),
        'descripcion':  formulario.get('descripcion', '').strip(),
        'precio':       formulario.get('precio', '').strip() or '0',
        'stock':        formulario.get('stock', '').strip() or '0',
        'imagen':       imagen or '',
        'categoria_id': formulario.get('categoria_id', '').strip() or '0',
    }


@productos_bp.route('/')
def index():
    return render_template('admin/productos.html', productos=obtener_productos())


@productos_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        resultado = crear_producto(_datos_del_formulario())

        if resultado['ok']:
            flash('Producto creado correctamente.', 'exito')

            return redirect(url_for('web.admin.productos.index'))

        flash(resultado['error'], 'error')

    return render_template(
        'admin/producto_form.html',
        producto=None,
        categorias=obtener_categorias(),
    )


@productos_bp.route('/<int:producto_id>/editar', methods=['GET', 'POST'])
def editar(producto_id):
    producto = obtener_producto(producto_id)

    if not producto:
        abort(404)

    if request.method == 'POST':
        resultado = actualizar_producto(producto_id, _datos_del_formulario(producto))

        if resultado['ok']:
            flash('Producto actualizado correctamente.', 'exito')

            return redirect(url_for('web.admin.productos.index'))

        flash(resultado['error'], 'error')

    return render_template(
        'admin/producto_form.html',
        producto=producto,
        categorias=obtener_categorias(),
    )


@productos_bp.route('/<int:producto_id>/eliminar', methods=['POST'])
def eliminar(producto_id):
    resultado = eliminar_producto(producto_id)

    if resultado['ok']:
        flash('Producto eliminado.', 'exito')
    else:
        flash(resultado['error'], 'error')

    return redirect(url_for('web.admin.productos.index'))
