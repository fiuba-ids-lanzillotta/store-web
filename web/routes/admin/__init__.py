"""Blueprint padre para la zona de administracion (sin login, a proposito)."""
from flask import Blueprint, redirect, url_for

from web.routes.admin.productos import productos_bp
from web.routes.admin.categorias import categorias_bp

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def index():
    return redirect(url_for('web.admin.productos.index'))


admin_bp.register_blueprint(productos_bp, url_prefix='/productos')
admin_bp.register_blueprint(categorias_bp, url_prefix='/categorias')
