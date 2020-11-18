import redis
from flask import Blueprint, render_template, request, make_response, send_from_directory
from sqlalchemy.ext.automap import automap_base
import json
import arrow
import calendar
import datetime
from common.MESLogger import logger,insertSyslog
from flask import render_template,request,Blueprint,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from common import MESLogger, autocode
from flask_login import current_user, LoginManager
from common.BSFramwork import AlchemyEncoder
from common.system import Organization, Factory, DepartmentManager, Role
from database import connect_db

from database.connect_db import CONNECT_DATABASE
login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()

from sqlalchemy import MetaData, desc
from io import BytesIO

metadata = MetaData()
Base = automap_base()
Base.prepare(engine, reflect=True)

system_set = Blueprint('system_set', __name__, template_folder='templates')


# 加载工作台
@system_set.route('/home/workbench')
def workbenck():
    return render_template('./main/workbench.html')

# 加载工作台
@system_set.route('/system_set/make_model', methods=['POST', 'GET'])
def make_model():
    if request.method == 'POST':
        data = request.values
        try:
            jsonstr = json.dumps(data.to_dict())
            return autocode.make_model_main(data)
        except Exception as e:
            print(e)
            logger.error(e)

def returnb(rod):
    if rod == None or rod == "" or rod == b'':
        return ""
    else:
        return rod.decode()
@system_set.route('/systemcollecting', methods=['POST', 'GET'])
def systemcollecting():
    '''
    系统体检
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            dir = {}
            pool = redis.ConnectionPool(host=constant.REDIS_HOST)
            redis_conn = redis.Redis(connection_pool=pool, password=constant.REDIS_PASSWORD, decode_responses=True)
            dir["name"] = "采集服务"
            dir["startTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_start"))
            dir["endTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_end"))
            dir["successNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_runcount"))
            dir["errorNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_failcount"))
            dir["totalNumber"] = int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_runcount")))+int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_failcount")))
            dir["state"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "collecting_server_status"))
            return json.dumps(dir, cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "系统体检报错Error：" + str(e), current_user.Name)

@system_set.route('/systemredisdb', methods=['POST', 'GET'])
def systemredisdb():
    '''
    系统体检
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            dir = {}
            pool = redis.ConnectionPool(host=constant.REDIS_HOST)
            redis_conn = redis.Redis(connection_pool=pool, password=constant.REDIS_PASSWORD, decode_responses=True)
            dir["name"] = "写入历史数据库服务"
            dir["startTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_start"))
            dir["endTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_end"))
            dir["successNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_runcount"))
            dir["errorNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_failcount"))
            dir["totalNumber"] = int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_runcount")))+int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_failcount")))
            dir["state"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_insertdb_server_status"))
            return json.dumps(dir, cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "系统体检报错Error：" + str(e), current_user.Name)

@system_set.route('/systemdbincrment', methods=['POST', 'GET'])
def systemdbincrment():
    '''
    系统体检
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            dir = {}
            pool = redis.ConnectionPool(host=constant.REDIS_HOST)
            redis_conn = redis.Redis(connection_pool=pool, password=constant.REDIS_PASSWORD, decode_responses=True)
            dir["name"] = "写入增量服务"
            dir["startTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_start"))
            dir["endTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_end"))
            dir["successNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_runcount"))
            dir["errorNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_failcount"))
            dir["totalNumber"] = int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_runcount")))+int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_failcount")))
            dir["state"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "redis_incremeninsertdb_server_status"))
            return json.dumps(dir, cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "系统体检报错Error：" + str(e), current_user.Name)

@system_set.route('/systemwebsocket', methods=['POST', 'GET'])
def systemwebsocket():
    '''
    系统体检
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            dir = {}
            pool = redis.ConnectionPool(host=constant.REDIS_HOST)
            redis_conn = redis.Redis(connection_pool=pool, password=constant.REDIS_PASSWORD, decode_responses=True)
            dir["name"] = "实时数据服务（websocket）"
            dir["startTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_start"))
            dir["endTime"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_end"))
            dir["successNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_runcount"))
            dir["errorNumber"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_failcount"))
            dir["totalNumber"] = int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_runcount")))+int(returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_failcount")))
            dir["state"] = returnb(redis_conn.hget(constant.REDIS_TABLENAME, "websocket_status"))
            return json.dumps(dir, cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "系统体检报错Error：" + str(e), current_user.Name)

from sqlalchemy import Table
def getTreeChildrenMap(id, ParentCode, tableName, Name, Code):
    sz = []
    try:
        db_session.commit()
        newTable = Table(tableName, metadata, autoload=True, autoload_with=engine)
        orgs = db_session.query(newTable).filter(newTable.columns._data[ParentCode] == int(id)).all()
        dir = []
        for i in orgs:
            a = 0
            divi = {}
            for j in newTable.columns._data:
                divi[str(j)] = str(i[a])
                a = a + 1
            dir.append(divi)
        for obj in dir:
            if int(obj.get(ParentCode)) == int(id):
                sz.append(
                    {"label": obj.get(Name), "value": obj.get(Code), "children": getTreeChildrenMap(obj.get("ID"), ParentCode, tableName, Name, Code)})
        return sz
    except Exception as e:
        print(e)
        return json.dumps([{"status": "Error：" + str(e)}], cls=AlchemyEncoder, ensure_ascii=False)
@system_set.route('/selectTree')
def selectTree():
    '''查询树形结构'''
    data = request.values
    if request.method == 'GET':
        try:
            ParentCode = data.get("ParentCode")#父节点字段名
            tableName = data.get("tableName")#表名
            Name = data.get("Name")#展示的字段名
            Code = data.get("Code")#展示的字段code
            id = 0
            return json.dumps(getTreeChildrenMap(id, ParentCode, tableName, Name, Code), cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            print(e)
            insertSyslog("error", "查询树形结构报错Error：" + str(e), current_user.Name)
            return json.dumps([{"status": "Error：" + str(e)}], cls=AlchemyEncoder, ensure_ascii=False)



pool = redis.ConnectionPool(host=connect_db.REDIS_HOST,decode_responses=True)
redis_conn = redis.Redis(connection_pool=pool)
def selectRedisBykey(data):
    '''通过key查询增加修改Redis单个的值'''
    try:
        key = data.get("key")
        value = redis_conn.hget(connect_db.REDIS_TABLENAME, key)
        return json.dumps(value, cls=AlchemyEncoder, ensure_ascii=False)
    except Exception as e:
        print(e)
        insertSyslog("error", "通过key查询Redis单个的值报错Error：" + str(e), current_user.Name)
        return json.dumps([{"status": "Error：" + str(e)}], cls=AlchemyEncoder, ensure_ascii=False)

def addUpdateRedisBykey(data):
    '''通过key查询增加修改Redis单个的值'''
    try:
        key = data.get("key")
        value = data.get("value")
        redis_conn.hset(connect_db.REDIS_TABLENAME, key, value)
        return json.dumps("OK", cls=AlchemyEncoder, ensure_ascii=False)
    except Exception as e:
        print(e)
        insertSyslog("error", "增加redis单个值报错Error：" + str(e), current_user.Name)
        return json.dumps([{"status": "Error：" + str(e)}], cls=AlchemyEncoder, ensure_ascii=False)

def deleteRedisBykey(data):
    '''通过key查询增加修改Redis单个的值'''
    try:
        key = data.get("key")
        redis_conn.delete(key)
        return json.dumps("OK", cls=AlchemyEncoder, ensure_ascii=False)
    except Exception as e:
        print(e)
        insertSyslog("error", "删除redis单个值报错Error：" + str(e), current_user.Name)
        return json.dumps([{"status": "Error：" + str(e)}], cls=AlchemyEncoder, ensure_ascii=False)

import os
dirpath = os.path.join(system_set.root_path,'files')
@system_set.route('/ManualDownload', methods=['get'])
def ManualDownload():
    # fname = request.values.get('FileName', '')
    fname = request.values.get('FileName', '')
    print(fname)
    print(os.path.join(dirpath, fname))
    if os.path.isfile(os.path.join(dirpath, fname)):
        response = make_response(send_from_directory(dirpath, fname, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(fname.encode().decode('latin-1'))
        return response
    else:
        json.dumps({"code": "200", "message": "参数错误！"})


