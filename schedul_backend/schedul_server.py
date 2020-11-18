from flask import Flask, abort, request, render_template
from flask_bootstrap import Bootstrap
from flask_restful import reqparse, abort, Api, Resource
from flask_login import login_required
from flask_login import current_user
import datetime
from system_backend.SystemManagement import auth_lib, user_management, Role_management, system_manage, \
    PermissionAssignment, account_auth
from system_backend.SystemManagement.account_auth import login_auth
from system_backend.SystemManagement.organization_model import organiza
from schedul_backend.ERP_Schedul import erp_schedul

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'qeqhdasdqiqd131'
account_auth.login_manager.init_app(app)

# 将后台函数传到前端
app.add_template_global(auth_lib.isIn, 'isIn')

# 排产
app.register_blueprint(erp_schedul)

@app.route('/')
@login_required
def index():
    return render_template("./main/index.html")


@app.route('/home')
@login_required
def home():
    return render_template("./main/home.html")


@app.route('/config')
@login_required
def config():
    if current_user.WorkNumber == "201900":
        return render_template("./main/config.html")
    else:
        return "没有此权限！"

api = Api(app)
from common.common_cuid import select, update, delete, insert
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
if __name__ == '__main__':
    from livereload import Server

    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve()
    # app.run()
