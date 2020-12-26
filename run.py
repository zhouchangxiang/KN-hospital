from flask import Flask
from flask_cors import CORS

from database.db_operate import DB_URL
from repair import repair
# from database.db_operate import DB_URL
from energy import energy
from energy_api import electric

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, supports_credentials=True)
app.register_blueprint(energy)
app.register_blueprint(electric)
app.register_blueprint(repair)


def main():
    app.run(port=5000)


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    main()
