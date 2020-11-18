from flask import Flask, abort, request, render_template
from flask_bootstrap import Bootstrap
from flask_restful import reqparse, abort, Api, Resource
from flask_login import login_required
from flask_login import current_user
import datetime
from schedul_backend.ERP_Schedul import erp_schedul
from schedul_backend.plan_manager import batch_plan
from schedul_backend.interface_manage import interface_manage
from system_backend.SystemManagement import auth_lib, user_management, Role_management, system_manage, \
    PermissionAssignment, account_auth
from system_backend.SystemManagement.account_auth import login_auth
from system_backend.SystemManagement.organization_model import organiza
from system_backend.SystemManagement.system_manage import selectRedisBykey, addUpdateRedisBykey, \
    deleteRedisBykey
from system_backend.SystemManagement.user_management import user_manager

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'qeqhdasdqiqd131'
account_auth.login_manager.init_app(app)

# 将后台函数传到前端
app.add_template_global(auth_lib.isIn, 'isIn')

# 登录
app.register_blueprint(login_auth)
# 用户管理
app.register_blueprint(user_management.user_manager)
# 角色管理
app.register_blueprint(Role_management.role_management)
# 主页
app.register_blueprint(system_manage.system_set)
# 权限分配
app.register_blueprint(PermissionAssignment.permission_distribution)
# 组织机构
app.register_blueprint(organiza)
# 过程连续数据
# app.register_blueprint(ProcessContinuousData.continuous_data)
# 组织架构
app.register_blueprint(user_manager)
# 排产
app.register_blueprint(erp_schedul)
#批次计划
app.register_blueprint(batch_plan)
#接口
app.register_blueprint(interface_manage)

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

class RedisCUIDList(Resource):
    def get(self):
        return selectRedisBykey(request.values)

    def post(self):
        return addUpdateRedisBykey(request.values)

    def put(self):
        return addUpdateRedisBykey(request.values)

    def delete(self):
        return deleteRedisBykey(request.values)

api.add_resource(RedisCUIDList, '/RedisCUID')
api.add_resource(CUIDList, '/CUID')
if __name__ == '__main__':
    from livereload import Server

    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve()
    # app.run()
