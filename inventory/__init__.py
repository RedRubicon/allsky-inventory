from flask import Flask
from inventory.device.views import device

app = Flask(__name__)
app.register_blueprint(device)
