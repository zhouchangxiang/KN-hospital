from flask import Blueprint, render_template, request
from sqlalchemy import desc, create_engine
import json
import socket
import datetime
from flask_login import current_user, LoginManager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from common.MESLogger import logger,insertSyslog
from common.BSFramwork import AlchemyEncoder
from common.system import Organization, Factory, DepartmentManager, Role, SysLog, AuditTrace
from system_backend.SystemManagement.user_management import user_manage
from database.connect_db import CONNECT_DATABASE
login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)

systemlog = Blueprint('systemlog', __name__, template_folder='templates')

# 系统日志
@systemlog.route('/syslogs')
def syslogs():
    return render_template('./syslogs.html')


# 日志查询
@systemlog.route('/syslogs/findByDate')
def syslogsFindByDate():
    if request.method == 'GET':
        data = request.values  # 返回请求中的参数和form
        try:
            json_str = json.dumps(data.to_dict())
            if len(json_str) > 10:
                pages = int(data.get("offset"))  # 页数
                rowsnumber = int(data.get("limit"))  # 行数
                inipage = pages * rowsnumber + 0  # 起始页
                endpage = pages * rowsnumber + rowsnumber  # 截止页
                startTime = data.get('startTime')  # 开始时间
                endTime = data.get('endTime') # 结束时间
                if startTime == "" and endTime == "":
                    total = db_session.query(SysLog).count()
                    syslogs = db_session.query(SysLog).order_by(desc("OperationDate")).all()[inipage:endpage]
                elif startTime != "" and endTime == "":
                    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    total = db_session.query(SysLog).filter(SysLog.OperationDate.between(startTime, nowTime)).count()
                    syslogs = db_session.query(SysLog).filter(
                        SysLog.OperationDate.between(startTime, nowTime)).order_by(desc("OperationDate")).all()[
                              inipage:endpage]
                else:
                    total = db_session.query(SysLog).filter(SysLog.OperationDate.between(startTime, endTime)).count()
                    syslogs = db_session.query(SysLog).filter(
                        SysLog.OperationDate.between(startTime, endTime)).order_by(desc("OperationDate")).all()[
                              inipage:endpage]
                return {"code": "200", "message": "请求成功", "data": {"total": total, "rows": syslogs}}
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "查询日志报错Error：" + str(e), current_user.Name)
            return {"code": "500", "message": "请求错误", "data": "查询日志报错Error：" + str(e)}

# 插入日志OperationType OperationContent OperationDate UserName ComputerName IP
def insertSyslog(operationType, operationContent, userName):
    try:
        if operationType == None: operationType = ""
        if operationContent == None:
            operationContent = ""
        else:
            operationContent = str(operationContent)
        if userName == None: userName = ""
        ComputerName = socket.gethostname()
        db_session.add(
            SysLog(OperationType=operationType, OperationContent=operationContent,
                   OperationDate=datetime.datetime.now(), UserName=userName,
                   ComputerName=ComputerName, IP=socket.gethostbyname(ComputerName)))
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(e)
        logger.error(e)


# 审计追踪查询
@systemlog.route('/syslogs/AuditTraceSelecct')
def AuditTraceSelecct():
    if request.method == 'GET':
        data = request.values  # 返回请求中的参数和form
        try:
            json_str = json.dumps(data.to_dict())
            if len(json_str) > 10:
                pages = int(data.get("offset"))  # 页数
                rowsnumber = int(data.get("limit"))  # 行数
                inipage = pages * rowsnumber + 0  # 起始页
                endpage = pages * rowsnumber + rowsnumber  # 截止页
                startTime = data['startTime']  # 开始时间
                endTime = data['endTime']  # 结束时间
                if startTime == "" and endTime == "":
                    total = db_session.query(AuditTrace).count()
                    syslogs = db_session.query(AuditTrace).order_by(desc("ReviseDate")).all()[inipage:endpage]
                elif startTime != "" and endTime == "":
                    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    total = db_session.query(AuditTrace).filter(AuditTrace.ReviseDate.between(startTime, nowTime)).count()
                    syslogs = db_session.query(AuditTrace).filter(
                        SysLog.OperationDate.between(startTime, nowTime)).order_by(desc("ReviseDate")).all()[
                              inipage:endpage]
                else:
                    total = db_session.query(AuditTrace).filter(AuditTrace.ReviseDate.between(startTime, endTime)).count()
                    syslogs = db_session.query(AuditTrace).filter(
                        AuditTrace.ReviseDate.between(startTime, endTime)).order_by(desc("OperationDate")).all()[
                              inipage:endpage]
                return {"code": "200", "message": "请求成功", "data": {"total": total, "rows": syslogs}}
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "审计追踪查询报错Error：" + str(e), current_user.Name)
            return {"code": "500", "message": "请求错误", "data": "审计追踪查询报错Error：" + str(e)}