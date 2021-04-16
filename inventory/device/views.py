from flask import Blueprint
from inventory.device.models import DEVICES

device = Blueprint('device', __name__)

@device.route('/')
@device.route('/device')
def show_all_devices():
    return DEVICES