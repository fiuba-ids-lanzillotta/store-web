"""Blueprint padre para la zona publica del sitio."""
from flask import Blueprint

from web.routes.site.home import home_bp
from web.routes.site.productos import productos_bp

site_bp = Blueprint('site', __name__)
site_bp.register_blueprint(home_bp)
site_bp.register_blueprint(productos_bp)
