from flask import Flask

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')

@app.route('/')
def index():
    return "<h1>Inventory App</h1>"

@app.route('/config')
def config():
    return (f'<h1>Configuration</h1>'
            f'<ul>'
                f'<li>DEBUG: {app.config["DEBUG"]}</li>'
                f'<li>TESTING: {app.config["TESTING"]}</li>'
                f'<li>SECRET_KEY: {app.config["SECRET_KEY"]}</li>'
            f'</ul>'
    )

if __name__ == '__main__':
    app.run()