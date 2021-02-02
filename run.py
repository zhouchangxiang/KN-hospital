import datetime
import json
import socket

from flask import Flask, abort, request, render_template
# from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
from flask_mail import Mail, Message

from common.KN_model import RunError
from database.db_operate import DB_URL
from common.asd import db_session
from repair import repair
from energy import energy
from energy_api import electric
from system_backend.SystemManagement import account_auth
from system_backend.SystemManagement.account_auth import login_auth
from common.common_cuid import select, update, delete, insert
from tools.MyEncode import MyEncoder
from tools.handle import my_log

app = Flask(__name__)
# bootstrap = Bootstrap(app)
# app.config['MAIL_SERVER'] = 'smtp.qq.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USERNAME'] = '448144775@qq.com'
# app.config['MAIL_PASSWORD'] = 'keofaicqcoqzcaaj'
# app.config['MAIL_PASSWORD'] = 'kvoedqjfwbdsjife'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ruiiiecemxbaebgh'
account_auth.login_manager.init_app(app)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='448144775@qq.com',
    MAIL_PASSWORD='keofaicqcoqzcaaj',
    MAIL_DEBUG=True
)

api = Api(app)
mail = Mail(app)

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


# def send_async_email(app1, msg):
#     with app1.app_context():
#         mail.send(msg)
#
#
# send_async_email(app, 'Hello, Mr.Huang')


def main():
    app.run(port=5000)


@app.route('/')
def hello_world():
    return 'hello world!'


@app.errorhandler(Exception)
def error_handler(e):
    """全局捕获异常"""
    db_session.rollback()
    re_path = request.path
    re_func = request.url_rule.endpoint.split('.')[1]
    re_method = request.method
    # root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # file_path = os.path.join(root_path, 'logs\\logs.txt')
    ip = socket.gethostbyname(socket.gethostname())
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    result = f"{now_time} -- {ip} -- {re_path} -- {re_func} -- {re_method} -- {e}"
    print(result)
    db_session.add(RunError(Time=now_time, IP=ip, Path=re_path, Func=re_func, Method=re_method, Error=e))
    db_session.commit()
    db_session.close()
    my_log(e)
    return json.dumps({'code': '2000', 'msg': result}, cls=MyEncoder, ensure_ascii=False)


@app.route('/send_mail', methods=['POST'])
def email_send_charactor():
    recipients = json.loads(request.values.get("mail"))
    message = Message("康宁医院运维任务", sender="448144775@qq.com", recipients=recipients)
    message.body = '您有一份新的运维任务，详情登录系统查看'
    try:
        mail.send(message)
        return json.dumps({"code": "200", "message": "发送成功，请注意查收~"})
    except Exception as e:
        print(e)
        return json.dumps({"code": "201", "message": "发送失败，请检查邮箱格式是否正确"})


if __name__ == '__main__':
    main()
