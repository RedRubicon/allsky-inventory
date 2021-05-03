from flask import Blueprint
import inventory

admin = Blueprint('admin', __name__)

@admin.route('/config/show')
def show_config():
    return (f"DEBUG: {inventory.app.config['DEBUG']}</br>"
            f"SECRET_KEY: {inventory.app.config['SECRET_KEY']}</br>"
            f"TESTING: {inventory.app.config['TESTING']}")