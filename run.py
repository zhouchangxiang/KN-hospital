from flask import Flask
from flask_cors import CORS

from database.connect_db import CONNECT_DATABASE
from energy import energy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, supports_credentials=True)
app.register_blueprint(energy, url_prefix='/work')


def main():
    app.run(port=5000)


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    main()
