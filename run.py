from flask import Flask, abort, request, render_template
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource

from database.db_operate import DB_URL
from repair import repair
# from database.db_operate import DB_URL
from energy import energy
from energy_api import electric
from system_backend.SystemManagement import account_auth
from system_backend.SystemManagement.account_auth import login_auth
from common.common_cuid import select, update, delete, insert

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'qeqhdasdqiqd131'
account_auth.login_manager.init_app(app)
api = Api(app)


CORS(app, supports_credentials=True)
app.register_blueprint(energy)
app.register_blueprint(electric)
app.register_blueprint(repair)
app.register_blueprint(login_auth)


class CUIDList(Resource):
    def get(self):
        return select(request.values)

    def post(self):
        return insert(request.values)

    def put(self):
        return update(request.values)

    def delete(self):
        return delete(request.values)


api.add_resource(CUIDList, '/CUID')


def main():
    app.run(port=5000)


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    main()
