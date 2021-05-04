from flask import Flask
from inventory.device.views import device
from inventory.admin.views import admin

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('configuration.DevelopmentConfig')
app.config.from_pyfile('development.cfg', silent=True)
app.register_blueprint(device)
app.register_blueprint(admin)
