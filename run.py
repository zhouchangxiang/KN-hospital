from flask import Flask, abort, request, render_template
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource

from database.db_operate import DB_URL
from repair import repair
# from database.db_operate import DB_URL
from energy import energy
from energy_api import electric
from system_backend.SystemManagement.account_auth import login_auth
from common.common_cuid import select, update, delete, insert

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, supports_credentials=True)
app.register_blueprint(energy)
app.register_blueprint(electric)
app.register_blueprint(repair)
app.register_blueprint(login_auth)


api = Api(app)


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
