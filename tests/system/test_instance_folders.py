import pytest
from inventory import app

def test_show_config():
    with app.test_client() as client:
        response = client.get('/config/show')
        
        assert response.status_code == 200
        # verify that the instance folder config is loaded through the SECRET_KEY unique string
        # assert response.get_data().decode() == 'DEBUG: True</br>SECRET_KEY: uOzeuzWuah7bFy0KPVC0</br>TESTING: True'
        assert 'uOzeuzWuah7bFy0KPVC0' in response.get_data().decode()
