import json

from flask import Blueprint, request
from common.MESLogger import logger,insertSyslog
from flask_login import current_user, LoginManager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from common.BSFramwork import AlchemyEncoder
from common.system import DepartmentManager, AreaMaintain, Role, RoleUser, User, ShiftsGroup, UserShiftsGroup
from database.connect_db import CONNECT_DATABASE
login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)

user_manager = Blueprint('user_manager', __name__)


@user_manager.route('/system_tree', methods=['GET'])
def get_user():
    departments = db_session.query(DepartmentManager).all()
    factory = db_session.query(AreaMaintain).first()
    queryset = []
    for department in departments:
        role_query = db_session.query(Role).filter(Role.ParentNode == department.DepartCode).all()
        role_list = []
        for data in role_query:
            d1 = db_session.query(DepartmentManager).filter(DepartmentManager.DepartCode == data.ParentNode).first()
            user_list = {'name': data.RoleName, 'value': data.RoleCode, 'role_description': data.Description, 'type': 'role', 'rid': data.ID, 'did': d1.ID, 'department_name': department.DepartName, 'children': []}
            user_role_query = db_session.query(RoleUser).filter(RoleUser.RoleName == data.RoleName).all()
            for user_role in user_role_query:
                user_query = db_session.query(User).filter(User.ID == user_role.UserID).first()
                if user_query:
                    d2 = db_session.query(DepartmentManager).filter(DepartmentManager.DepartName == user_query.OrganizationName).first()
                    if d2:
                        user_data = {'name': user_query.Name, 'value': user_query.WorkNumber, 'type': 'user', 'rid': data.ID,
                                     'did': d2.ID}
                    else:
                        user_data = {'name': user_query.Name, 'value': user_query.WorkNumber, 'type': 'user', 'rid': data.ID, 'did': ''}
                    # for user in user_query:
                    #     d2 = db_session.query(DepartmentManager).filter(DepartmentManager.DepartName == user.OrganizationName).first()
                    #     if d2:
                    #         user_data = {'name': user.Name, 'value': user.WorkNumber, 'type': 'user', 'rid': data.ID, 'did': d2.ID}
                    #     else:
                    #         user_data = {'name': user.Name, 'value': user.WorkNumber, 'type': 'user', 'rid': data.ID, 'did': ''}
                    user_list['children'].append(user_data)
            role_list.append(user_list)
        department_data = {'name': department.DepartName, 'value': department.DepartCode, 'type': 'department', 'did': department.ID, 'factory_name': factory.FactoryName, 'children': role_list}
        area = db_session.query(AreaMaintain).filter(AreaMaintain.FactoryName == department.DepartLoad).first()
        if area:
            department_data['fid'] = area.ID
        queryset.append(department_data)
    data = {'name': factory.FactoryName, 'value': factory.AreaCode, 'type': 'factory', 'fid': factory.ID, 'children': queryset}
    return json.dumps(data, cls=AlchemyEncoder, ensure_ascii=False)


@user_manager.route('/system_tree/add_department', methods=['POST'])
def add_department():
    did = request.json.get('department_code')
    dname = request.json.get('department_name')
    fname = request.json.get('factory_name')
    depart = DepartmentManager(DepartCode=did, DepartName=dname, DepartLoad=fname)
    db_session.add(depart)
    db_session.commit()
    return json.dumps({'code': 10000, 'msg': '新增成功', 'data': {'Did': depart.ID}})


@user_manager.route('/system_tree/delete_department', methods=['DELETE'])
def delete_department():
    code = request.headers.get('department_code')
    department = db_session.query(DepartmentManager).filter(DepartmentManager.DepartCode == code).first()
    role_query = db_session.query(Role).filter(Role.ParentNode == department.DepartCode).all()
    for item in role_query:
        item.ParentNode = ''
    db_session.commit()
    user_query = db_session.query(User).filter(User.OrganizationName == department.DepartName).all()
    for item in user_query:
        item.OrganizationName = ''
    db_session.commit()
    db_session.delete(department)
    db_session.commit()
    return json.dumps({'code': 10001, 'msg': '删除成功'})


@user_manager.route('/system_tree/update_department', methods=['PATCH'])
def update_department():
    did = request.json.get('did')
    code = request.json.get('department_code')
    department_name = request.json.get('department_name')
    department = db_session.query(DepartmentManager).filter(DepartmentManager.ID == int(did)).first()
    role_query = db_session.query(Role).filter(Role.ParentNode == department.DepartCode).all()
    for item in role_query:
        item.ParentNode = code
    department.DepartCode = code
    department.DepartName = department_name
    db_session.commit()
    user_query = db_session.query(User).filter(User.OrganizationName == department.DepartName).all()
    for user in user_query:
        user.OrganizationName = department_name
    db_session.commit()
    return json.dumps({'code': 10002, 'msg': '更新成功'})


@user_manager.route('/system_tree/add_role', methods=['POST'])
def add_role():
    rcode = request.json.get('role_code')
    did = request.json.get('did')
    rname = request.json.get('role_name')
    rdes = request.json.get('role_description')
    department = db_session.query(DepartmentManager).filter(DepartmentManager.ID == int(did)).first()
    role = Role(RoleCode=rcode, RoleName=rname, Description=rdes, ParentNode=department.DepartCode)
    db_session.add(role)
    db_session.commit()
    return json.dumps({'code': 10003, 'msg': '新增成功', 'data': {'rid': role.ID}})


@user_manager.route('/system_tree/delete_role', methods=['DELETE'])
def delete_role():
    rid = request.headers.get('rid')
    role = db_session.query(Role).filter(Role.ID == rid).first()
    user_query = db_session.query(RoleUser).filter(RoleUser.RoleName == role.RoleName).all()
    for item in user_query:
        db_session.delete(item)
    db_session.delete(role)
    db_session.commit()
    return json.dumps({'code': 10004, 'msg': '删除成功'})


@user_manager.route('/system_tree/update_role', methods=['PATCH'])
def update_role():
    rid = request.json.get('rid')
    code = request.json.get('role_code')
    role_name = request.json.get('role_name')
    rdes = request.json.get('role_description')
    role = db_session.query(Role).filter(Role.ID == rid).first()
    user_query = db_session.query(RoleUser).filter(RoleUser.RoleName == role.RoleName).all()
    for item in user_query:
        item.RoleName = role_name
    role.RoleCode = code
    role.RoleName = role_name
    role.Description = rdes
    db_session.commit()
    return json.dumps({'code': 10005, 'msg': '更新成功'})



@user_manager.route('/user_manage/userselect')
def userselect(data):#table, page, rows, fieid, param
    '''
    :param tablename: 查询表
    :param pages: 页数
    :param rowsnumber: 一页多少行
    :param fieid: 查询字段
    :param param: 查询条件
    :return:用户查询
    '''
    try:
        pages = int(data.get("offset"))
        rowsnumber = int(data.get("limit"))
        param = data.get("field")
        tableName = data.get("tableName")
        paramvalue = data.get("fieldvalue")
        if (paramvalue == "" or paramvalue == None):
            oclass = db_session.query(User).filter(User.WorkNumber == paramvalue).all()
            total = db_session.query(User).filter(User.WorkNumber == paramvalue).count()
        jsonoclass = '{"total"' + ":" + str(total) + ',"rows"' + ":\n" + oclass + "}"
        return jsonoclass
    except Exception as e:
        print(e)
        logger.error(e)
        insertSyslog("error", "用户查询报错Error：" + str(e), current_user.Name)


@user_manager.route('/saveuserusershiftsgroup', methods=['POST', 'GET'])
def saveuserusershiftsgroup():
    '''
    用户添加班组
    :return:
    '''
    if request.method == 'POST':
        data = request.values
        try:
            userID = data.get("userID")
            shiftsgroupIDs = data.get("shiftsgroupIDs")
            if shiftsgroupIDs:
                shiftsgroupIDs = eval(shiftsgroupIDs)
            userclass = db_session.query(User).filter(User.ID == int(userID)).first()
            sql = "delete from usershiftsgroup where UserID = " + userID
            db_session.execute(sql)
            db_session.commit()
            for pid in shiftsgroupIDs:
                shiftsgroupcalss = db_session.query(ShiftsGroup).filter(ShiftsGroup.ID == int(pid)).first()
                rpclas = db_session.query(UserShiftsGroup).filter(UserShiftsGroup.UserID == userclass.ID, UserShiftsGroup.ShiftsGroupID == shiftsgroupcalss.ID).first()
                if not rpclas:
                    rp = UserShiftsGroup()
                    rp.UserID = userclass.ID
                    rp.Name = userclass.Name
                    rp.ShiftsGroupID = shiftsgroupcalss.ID
                    rp.ShiftsGroupName = shiftsgroupcalss.ShiftsGroupName
                    db_session.add(rp)
                    db_session.commit()
            return json.dumps("OK", cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            db_session.rollback()
            print(e)
            logger.error(e)
            insertSyslog("error", "角色添加权限Error：" + str(e), current_user.Name)

@user_manager.route('/selectUserShiftsGroup', methods=['POST', 'GET'])
def selectUserShiftsGroup():
    '''
    根据用户查班组
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            dir = {}
            userID = data.get("userID")
            pids = db_session.query(UserShiftsGroup).filter(UserShiftsGroup.UserID == int(userID)).all()
            perids_list = []
            for pid in pids:
                perids_list.append(pid.ShiftsGroupID)
            if len(perids_list) > 0:
                existingRows = db_session.query(ShiftsGroup).filter(ShiftsGroup.ID.in_(perids_list)).all()
                dir["existingRows"] = existingRows
            else:
                dir["existingRows"] = []
            notHaveRows = db_session.query(ShiftsGroup).filter().all()
            dir["notHaveRows"] = notHaveRows
            return json.dumps(dir, cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            print(e)
            logger.error(e)
            insertSyslog("error", "根据角色查询权限Error：" + str(e), current_user.Name)


