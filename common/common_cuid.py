import json
from sqlalchemy import create_engine, desc
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from flask_login import current_user
import re

from werkzeug.security import generate_password_hash

from database.connect_db import CONNECT_DATABASE
import socket
import datetime
from common.system import SysLog, User, AuditTrace
from common.MESLogger import MESLogger
from common.BSFramwork import AlchemyEncoder

engine = create_engine(CONNECT_DATABASE, deprecate_large_types=True)
Session = sessionmaker(bind=engine)
db_session = Session()

from sqlalchemy import MetaData

metadata = MetaData()
from sqlalchemy import Table
Base = automap_base()
Base.prepare(engine, reflect=True)

logger = MESLogger('../equipment_backend/logs', 'log')
#插入日志OperationType OperationContent OperationDate UserName ComputerName IP
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
                SysLog(OperationType=operationType, OperationContent=operationContent,OperationDate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), UserName=userName,
                       ComputerName=ComputerName, IP=socket.gethostbyname(ComputerName)))
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            print(e)
            logger.error(e)

def insert(data):
    '''
    :param data: 需要添加的数据
    :return:
    '''
    if isinstance(data, dict) and len(data) > 0:
        try:
            tableName = str(data.get("tableName"))
            obj = Base.classes.get(tableName)
            ss = obj()
            for key in data:

                if key != "ID" and key != "tableName" and key != "id":
                    if key == "Password":
                        setattr(ss, key, generate_password_hash(data['Password']))
                        if tableName == "User":
                            setattr(ss, "Creater", current_user.Name)
                    elif key == "WorkNumber":
                        ocal = db_session.query(User).filter(User.WorkNumber == data['WorkNumber']).first()
                        if ocal != None:
                            return "工号重复，请重新录入！"
                        else:
                            setattr(ss, key, data['WorkNumber'])
                    else:
                        setattr(ss, key, data[key])
            db_session.add(ss)
            aud = AuditTrace()
            aud.TableName = tableName
            aud.Operation = current_user.Name + " 对表" + tableName + "添加一条数据！"
            aud.DeitalMSG = "用户：" + current_user.Name + " 对表" + tableName + "添加一条数据！"
            aud.ReviseDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            aud.User = current_user.Name
            db_session.add(aud)
            db_session.commit()
            return  {"code": "200", "message": "添加成功"}
        except Exception as e:
            print(e)
            db_session.rollback()
            logger.error(e)
            insertSyslog("error", "%s数据添加报错："%tableName + str(e), current_user.Name)
            return {"code": "500", "message": "请求错误", "data": "%s数据添加报错："%tableName + str(e)}

def delete(data):
    '''
    :param data: 要删除的数据
    :return:
    '''
    try:
        tableName = str(data.get("tableName"))
        jsonstr = json.dumps(data.to_dict())
        if len(jsonstr) > 10:
            jstr = data.get("delete_data")
            jsonnumber = re.findall(r"\d+\.?\d*", jstr)
            for key in jsonnumber:
                try:
                    sql = "delete from "+"[LIMS].[dbo].["+tableName+"] where ID = "+str(key)
                    db_session.execute(sql)
                    aud = AuditTrace()
                    aud.TableName = tableName
                    aud.Operation = current_user.Name + " 对表" + tableName + "中的ID为"+key+"的数据做了删除操作！"
                    aud.DeitalMSG = "用户：" + current_user.Name + " 对表" + tableName + "中的ID为"+key+"的数据做了删除操作！"
                    aud.ReviseDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    aud.User = current_user.Name
                    db_session.add(aud)
                    db_session.commit()
                except Exception as ee:
                    print(ee)
                    db_session.rollback()
                    insertSyslog("error", "删除户ID为"+str(id)+"报错Error：" + str(ee), current_user.Name)
                    return {"code": "500", "message": "请求错误", "data": "删除户ID为"+str(id)+"报错Error：" + str(ee)}
            return {"code": "200", "message": "删除成功"}
    except Exception as e:
        db_session.rollback()
        logger.error(e)
        insertSyslog("error", "%s数据删除报错："%tableName + str(e), current_user.Name)
        return {"code": "500", "message": "请求错误", "data": "%s数据删除报错："%tableName + str(e)}

def update(data):
    '''
    :param data: 更新数据
    :return:
    '''
    if isinstance(data, dict) and len(data) > 0:
        try:
            tableName = str(data.get("tableName"))
            obj = Base.classes.get(tableName)
            ss = obj()
            ID = data.get('ID')
            oclass = db_session.query(obj).filter_by(ID=int(data.get('ID'))).first()
            if oclass:
                for key in data:
                    if hasattr(oclass, key) and key != 'ID' and key != 'tableName' and key != "id" and key != "Creater":
                        if key == "Password":
                            setattr(oclass, key, generate_password_hash(data['Password']))
                        elif key == "WorkNumber":
                            ocal = db_session.query(User).filter(User.WorkNumber == data['WorkNumber']).first()
                            if ocal != None:
                                if oclass.WorkNumber != data['WorkNumber']:
                                    return "工号重复，请重新录入！"
                            else:
                                setattr(oclass, key, data['WorkNumber'])
                        else:
                            setattr(oclass, key, data[key])
                db_session.add(oclass)
                aud = AuditTrace()
                aud.TableName = tableName
                aud.Operation =current_user.Name+" 对表"+tableName+"的数据做了更新操作！"
                aud.DeitalMSG = "用户："+current_user.Name+" 对表"+tableName+"ID为："+ID+"做了更新操作"
                aud.ReviseDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                aud.User = current_user.Name
                db_session.add(aud)
                db_session.commit()
                return {"code": "200", "message": "修改成功"}
            else:
                return {"code": "200", "message": "修改成功", "data": "当前记录不存在"}
        except Exception as e:
            db_session.rollback()
            logger.error(e)
            insertSyslog("error", "%s数据更新报错："%tableName + str(e), current_user.Name)
            return {"code": "500", "message": "请求错误", "data": "%s数据更新报错："%tableName + str(e)}

def select(data):
    '''
    :param tablename: 查询表
    :param pages: 页数
    :param rowsnumber: 一页多少行
    :return:
    '''
    try:
        tableName = data.get("tableName")
        pages = data.get("offset")
        if pages == None or pages == "":
            pages = ""
        else:
            pages = int(data.get("offset")) + 1
            rowsnumber = int(data.get("limit"))
        newTable = Table(tableName, metadata, autoload=True, autoload_with=engine)
        columns = ""
        for column in newTable.columns:
            if columns == "":
                columns = "[" + str(column).split(".")[1] + "]"
            else:
                columns = columns + ",[" + str(column).split(".")[1] + "]"
        params = ""
        searchModes = data.get("searchModes")
        for key in data.keys():
            if key != "offset" and key != "limit" and key != "tableName" and key != "":
                if searchModes == None or searchModes == "":#模糊查询
                    if key != "searchModes":
                        if params == "":
                            params = key + " like '%" + data[key] + "%'"
                        else:
                            params = params + " AND " + key + " like '%" + data[key] + "%'"
                else:#精确查询
                    if key != "searchModes":
                        if params == "":
                            params = key + " = '" + data[key] + "'"
                        else:
                            params = params + " AND " + key + " = '" + data[key] + "'"
        if pages == "":
            if params == "":
                sql = "select " + columns + " from [LIMS].[dbo].[" + tableName + "] ORDER BY ID DESC"
                sqlcount = "select count(ID) from [LIMS].[dbo].[" + tableName + "]"
            else:
                sql = "select " + columns + " from [LIMS].[dbo].[" + tableName + "] where " + params + " ORDER BY ID DESC"
                sqlcount = "select count(ID) from [LIMS].[dbo].[" + tableName + "] where " + params
        else:
            if params == "":
                sql = "select top " + str(
                    rowsnumber) + " " + columns + " from [LIMS].[dbo].[" + tableName + "] where ID not in (select top " + str(
                    (pages - 1) * rowsnumber) + " ID FROM [LIMS].[dbo].[" + tableName + "] ORDER BY ID DESC) ORDER BY ID DESC"
                sqlcount = "select count(ID) from [LIMS].[dbo].[" + tableName + "]"
            else:
                sql = "select top " + str(
                    rowsnumber) + " " + columns + " from [LIMS].[dbo].[" + tableName + "] where " + params + \
                      "AND ID not in (select top " + str(
                    (pages - 1) * rowsnumber) + " ID FROM [LIMS].[dbo].[" + tableName + "] where " + params +" ORDER BY ID DESC) ORDER BY ID DESC"
                sqlcount = "select count(ID) from [LIMS].[dbo].[" + tableName + "] where " + params
        re = db_session.execute(sql).fetchall()
        recount = db_session.execute(sqlcount).fetchall()
        dict_list = []
        for i in re:
            dir = {}
            column_list = columns.split(",")
            for column in column_list:
                if isinstance(i[column[1:-1]], datetime.datetime) == True:
                    dir[column[1:-1]] = datetime.datetime.strftime(i[column[1:-1]],'%Y-%m-%d %H:%M:%S')
                else:
                    dir[column[1:-1]] = i[column[1:-1]]
            dict_list.append(dir)
        return {"code": "200", "message": "请求成功", "data": {"total": recount[0][0], "rows": dict_list}}
    except Exception as e:
        print(e)
        logger.error(e)
        insertSyslog("error", "查询报错Error：" + str(e), current_user.Name)
        return {"code": "500", "message": "请求错误", "data": "查询报错Error：" + str(e)}
# dir = []
# for i in oclass:
#     a = 0
#     divi = {}
#     for j in newTable.columns._data:
#         divi[str(j)] = str(i[a])
#         a = a + 1
#     dir.append(divi)