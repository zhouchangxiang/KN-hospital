from tkinter.tix import MAX

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, Column, DateTime, Integer, Unicode
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import LoginManager

from database.connect_db import CONNECT_DATABASE
login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)


class SysLog(Base):
    __tablename__ = "SysLog"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # IP:
    IP = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 计算机名称:
    ComputerName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 操作用户:
    UserName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 操作日期:
    OperationDate = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 操作内容:
    OperationContent = Column(Unicode(2048), primary_key=False, autoincrement=False, nullable=True)

    # 类型:
    OperationType = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)


# Organization:
class Organization(Base):
    __tablename__ = "Organization"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 组织结构编码:
    OrganizationCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 父组织机构:
    ParentNode = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 顺序号:
    OrganizationSeq = Column(Unicode(10), primary_key=False, autoincrement=False, nullable=True)

    # 组织机构名称:
    OrganizationName = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 说明:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 创建人:
    CreatePerson = Column(Unicode(20), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间:
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 显示图标:
    Img = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True, default="antonio.jpg")

    # 显示图标:
    Color = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True, default="#1696d3")


# 审计追踪
class AuditTrace(Base):
    __tablename__ = 'AuditTrace'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 操作:
    Operation = Column(Unicode(300), primary_key=False, autoincrement=False, nullable=True)

    # 详细信息:
    DeitalMSG = Column(Unicode(800), primary_key=False, autoincrement=False, nullable=True)

    # 修改日期
    ReviseDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 操作表:
    TableName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 用户:
    User = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 其他:
    Other = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 数据库建表配置
class CreateTableSet(Base):
    __tablename__ = 'CreateTableSet'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 表名:
    TableName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 表的描述:
    TableDescrip = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # # 表类型（分页表/下拉框数据表）:
    # TableType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否在第一列显示多选框（checkbox）:
    ISFirstCheckBox = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否实现单选，设为true则复选框只能选择一行:
    SingleSelect = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否显示添加按钮:
    IsAdd = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否显示修改按钮:
    IsUpdate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否显示删除按钮:
    IsDelete = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # ID字段:
    TableID = Column(Unicode(32), default="ID", primary_key=False, autoincrement=False, nullable=True)


# 4.表字段配置：选择一个表，将此表的数据（字段）显示出来（新表只有ID）
# 字段表表头
class FieldSet(Base):
    __tablename__ = 'FieldSet'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 表名称:
    TableName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # title字段名称（名字）:
    TitleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # field字段名（name）:
    FieldName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # isedit是否做添加修改操作（默认否）:
    Isedit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # edittype输入类型，输入框/下拉框/时间选择框（满足上一条可做编辑操作，默认输入框）:
    Edittype = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # downtable下拉框的数据表（满足上一条选择下拉框，选择一个表）:
    Downtable = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # sortable该列是否排序,表头显示双箭头(默认false):
    Sortable = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # order该列排序方式，满足上条可排序，默认asc( asc/desc):
    Order = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # visible该列是否可见(默认true):
    Visible = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # VARCHAR长度:
    length = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 字段类型:
    type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 字段注释:
    comment = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 是否为主键（默认False）:
    primarykey = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否自增（默认False）:
    autoincrement = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否为空（默认True）:
    nullable = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 列宽:
    width = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 是否
class ISFlag(Base):
    __tablename__ = 'ISFlag'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 标识:
    Flag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 是否
class InputTypeTable(Base):
    __tablename__ = 'InputTypeTable'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 类型:
    Type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 名称:
    Title = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 表字段类型
class FieldType(Base):
    __tablename__ = 'FieldType'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 类型:
    Type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 用户班组表
class UserShiftsGroup(Base):
    __tablename__ = 'UserShiftsGroup'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 用户ID:
    UserID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 用户名:
    Name = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 班组ID:
    ShiftsGroupID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 班组名称
    ShiftsGroupName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 权限表
class Permission(Base):
    __tablename__ = 'Permission'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 权限名字:
    PermissionName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 权限类型:
    PermissionType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateData = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class DepartmentManager(Base):
    '''部门'''
    __tablename__ = "DepartmentManager"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 部门名称:
    DepartName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 部门编码:
    DepartCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    DepartLoad = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class Role(Base):
    '''角色'''
    __tablename__ = "Role"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 角色编码:
    RoleCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # RoleName:
    RoleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # Description:
    Description = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 所属部门:
    ParentNode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 角色默认权限表
class RolePermission(Base):
    __tablename__ = 'RolePermission'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 角色ID:
    RoleID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 角色名称:
    RoleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 权限ID:
    PermissionID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 权限名字:
    PermissionName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 角色用户表
class RoleUser(Base):
    __tablename__ = 'RoleUser'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 权限ID:
    UserID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 权限名字:
    UserName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 角色ID:
    RoleID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 角色名称:
    RoleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True,
                        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# User_START:
class User(Base):
    __tablename__ = "User"

    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 用户名:
    Name = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 密码:
    Password = Column(Unicode(150), primary_key=False, autoincrement=False, nullable=True)

    # 工号:
    WorkNumber = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 所属岗位:
    StationName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 登录状态:
    Status = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # session_id:
    session_id = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 所属部门:
    OrganizationName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    FactoryName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 班组类型
    ShiftsGroupType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 上次登录时间:
    LastLoginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间:
    CreateTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建用户:
    Creater = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 是否锁定:
    IsLock = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')

    # 定义password字段的写方法，我们调用generate_password_hash将明文密码password转成密文Shadow
    # @password.setter
    def password(self, password):
        self.Password = generate_password_hash(password)
        return self.Password

    # 定义验证密码的函数confirm_password
    def confirm_password(self, password):
        return check_password_hash(self.Password, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.ID)  # python 3


# User_END:

# 服务运行情况表
class SystemRunDetail(Base):
    __tablename__ = 'SystemRunDetail'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 总执行次数:
    RunTotalNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 开始执行时间:
    RunStartTime = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 最后刷新时间:
    RunRefreshTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 执行状态:
    RunStatus = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 执行成功数:
    RunSuccessNum = Column(Unicode(150), primary_key=False, autoincrement=False, nullable=True)

    # 执行失败数:
    RunFailNum = Column(Unicode(150), primary_key=False, autoincrement=False, nullable=True)



# 班时
class Shifts(Base):
    __tablename__ = "Shifts"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 班次编码
    ShiftsCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班次名称
    ShiftsName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班次开始时间
    BeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班次结束时间
    EndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 班制
class ShiftsClass(Base):
    __tablename__ = "ShiftsClass"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 班制编码
    ShiftsClassCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班制名称
    ShiftsClassName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 排班序号
    ShiftsClassNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班制开始时间
    BeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班制结束时间
    EndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# 班组
class ShiftsGroup(Base):
    __tablename__ = "ShiftsGroup"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 班组编码
    ShiftsGroupCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班组名称
    ShiftsGroupName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 班组类型
    ShiftsGroupType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)
    # 创建日期:
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class WorkShop(Base):
    '''车间'''
    __tablename__ = "WorkShop"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 车间名称:
    WorkShopName = Column(Unicode(52), primary_key=False, autoincrement=False, nullable=True)

    # 车间编码:
    WorkShopCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    FactoryName = Column(Unicode(52), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)


class Unit(Base):
    __tablename__ = "Unit"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 单位名称:
    UnitName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位值:
    UnitValue = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class LimitTable(Base):
    __tablename__ = "LimitTable"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 名称:
    LimitName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 编码:
    LimitCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 限值:
    LimitValue = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class AreaMaintain(Base):
    '''厂区'''
    __tablename__ = "AreaMaintain"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 区域编码:
    AreaCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域名称:
    AreaName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 所属厂区:
    FactoryName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

class Station(Base):
    '''岗位'''
    __tablename__ = "Station"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 地址:
    Address = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 电话:
    Phone = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 岗位负责人:
    PersonCharge = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 岗位职责:
    Responsibility = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 所属部门:
    DepartName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 岗位类型:
    StationType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 岗位名称:
    StationName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 岗位编码:
    StationCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class Factory(Base):
    __tablename__ = "Factory"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 所属企业:
    EnterpriseName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 厂名:
    FactoryName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 所在地区:
    Region = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

class Enterprise(Base):
    __tablename__ = "Enterprise"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 上级企业:
    ParentNode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 企业类型:
    Type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 父节点名称:
    ParentNodeName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 企业代码:
    EnterpriseNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 企业名称:
    EnterpriseName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 企业编码:
    EnterpriseCode = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

class MenuType(Base):
    __tablename__ = "MenuType"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 类型名称:
    TypeName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 类型编码:
    TypeCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class plantCalendarScheduling(Base):
    '''日历'''
    __tablename__ = "plantCalendarScheduling"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 颜色:
    color = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 标题:
    title = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 时间:
    start = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 结束:
    end = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class TechnologicalProcess(Base):
    '''流程'''
    __tablename__ = "TechnologicalProcess"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 流程名:
    ProcessName = Column(Unicode(80), primary_key=False, autoincrement=False, nullable=True)

    # 流程结构:
    ProcessStructure = Column(Unicode(MAX), primary_key=False, autoincrement=False, nullable=True)

    # 流程结构:
    Icon = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 注释:
    Describtion = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 录入时间:
    InputDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# 模块菜单表
class ModulMenus(Base):
    __tablename__ = 'ModulMenus'
    # 模块ID
    ID = Column(Integer, primary_key=True, autoincrement=True)

    # 模块菜单名字:
    ModulMenuName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 模块菜单编码:
    ModulMenuCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 菜单路由:
    ModulMenuRoute = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建时间
    CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)

    # 父节点
    ParentNode = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 菜单类型:
    MenuType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 菜单图标:
    MenuLogo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 菜单创建人:
    Creator = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# 流程存储
class ProcessStorage(Base):
    '''流程存储'''
    __tablename__ = 'ProcessStorage'
    # 模块ID
    ID = Column(Integer, primary_key=True, autoincrement=True)

    # 流程存储名:
    ProcessName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 流程存储code:
    ModulMenuCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 流程存储内容:
    ModulMenuRoute = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 存储时间
    CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)

# 首页模块存储
class HomeModule(Base):
    '''首页模块存储'''
    __tablename__ = 'HomeModule'
    # 模块ID
    ID = Column(Integer, primary_key=True, autoincrement=True)

    # 模块名称:
    HomeModuleName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 模块内容:
    HomeModuleContent = Column(Unicode(500), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 存储时间
    CreateDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=True)




# 生成表单的执行语句
Base.metadata.create_all(engine)
