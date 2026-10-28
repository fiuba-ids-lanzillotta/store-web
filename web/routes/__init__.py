from flask import Blueprint
from web.routes.site import site_bp
from web.routes.admin import admin_bp

web_bp = Blueprint('web', __name__)

web_bp.register_blueprint(site_bp)
web_bp.register_blueprint(admin_bp, url_prefix='/admin')
