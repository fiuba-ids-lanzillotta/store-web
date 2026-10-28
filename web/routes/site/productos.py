from flask import Blueprint, render_template, request, abort

from web.services.productos import obtener_productos, obtener_producto
from web.services.categorias import obtener_categorias

productos_bp = Blueprint('productos', __name__)


@productos_bp.route('/productos')
def index():
    """Catalogo publico, con filtro por categoria y busqueda por texto."""
    categoria_id = request.args.get('categoria_id', type=int)
    texto        = request.args.get('q', '').strip() or None

    return render_template(
        'site/catalogo.html',
        productos=obtener_productos(categoria_id=categoria_id, texto=texto),
        categorias=obtener_categorias(),
        categoria_actual=categoria_id,
        texto_actual=texto or '',
    )


@productos_bp.route('/productos/<int:producto_id>')
def detalle(producto_id):
    producto = obtener_producto(producto_id)

    if not producto:
        abort(404)

    return render_template('site/producto.html', producto=producto)
