from inventory.device import models
from inventory import app
from inventory.device.models import DEVICES

@app.route('/')
@app.route('/device')
def show_all_devices():
    return DEVICES