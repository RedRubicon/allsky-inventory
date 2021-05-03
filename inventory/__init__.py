from flask import Flask
from inventory.device.views import device
from inventory.admin.views import admin

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
app.register_blueprint(device)
app.register_blueprint(admin)
