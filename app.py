from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return "<h1>Inventory App</h1>"

if __name__ == '__main__':
    app.run()