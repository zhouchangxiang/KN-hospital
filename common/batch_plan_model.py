from tkinter.tix import MAX

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, ForeignKey, Column, DateTime, Integer, Unicode, Float, BigInteger
from sqlalchemy.dialects.mssql.base import BIT

from flask_login import LoginManager
from database.connect_db import CONNECT_DATABASE

login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)




# 电子批记录
class ElectronicBatch(Base):
    '''电子批记录'''
    __tablename__ = 'ElectronicBatch'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # id:
    TaskID = Column(Integer, primary_key=False, autoincrement=True, nullable=False)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PDUnitRouteID = Column(Integer, nullable=False, primary_key=False)

    # 设备编码
    EQPID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 类型:
    OpcTagID = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 类型:
    BrandID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 类型:
    BrandName = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 采样值:
    SampleValue = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 采样时间:
    SampleDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

    # 重复次数：
    RepeatCount = Column(Integer, primary_key=False, autoincrement=False, nullable=True, default=0)

    # 描述:
    Description = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Type = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# BatchMaintain_START:
class BatchMaintainTask(Base):
    '''
    任务表
    '''
    __tablename__ = "BatchMaintainTask"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 工艺段:
    PuidName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划单号:
    PlanNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名:
    BrandName = Column(Unicode(52), primary_key=False, autoincrement=False, nullable=True)

    # 计划重量:
    PlanQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 水用量:
    WaterConsumption = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 汽用量:
    SteamConsumption = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 创建日期:
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 生产日期:
    ProductionDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 开始时间:
    StartTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 结束时间:
    EndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class BrandMaintain(Base):
    '''品名维护表'''
    __tablename__ = "BrandMaintain"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 产品名称:
    BrandName = Column(Unicode(64), nullable=False, primary_key=False)

    # 产品编码:
    BrandCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 创建日期:
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


class PUIDMaintain(Base):
    '''工艺维护表'''
    __tablename__ = "PUIDMaintain"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 工艺名称:
    PUIDName = Column(Unicode(64), nullable=False, primary_key=False)

    # 工艺编码:
    PUIDCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 产品名称:
    BrandName = Column(Unicode(64), nullable=False, primary_key=False)

    # 产品编码:
    BrandCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 创建日期:
    CreateDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# ZYPlan:
class ZYPlan(Base):
    '''工艺段生产计划'''
    __tablename__ = "ZYPlan"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)

    # 计划日期:
    PlanDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 制药计划单号:
    PlanNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 顺序号:
    PlanSeq = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 计划类型:
    PlanType = Column(Unicode(16), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # ERP订单号:
    ERPOrderNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划重量:
    PlanQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际重量:
    ActQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 录入时间:
    EnterTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划开始时间:
    PlanBeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    PlanEndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际开始时间:
    ActBeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际完成时间:
    ActEndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划状态:
    ZYPlanStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划锁定状态:
    LockStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 接口处理状态:
    INFStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 仓储送料状态:
    WMSStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# ZYTask:
class ZYTask(Base):
    '''工艺段计划任务'''
    __tablename__ = "ZYTask"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)

    # 设备编码:
    EQPCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 设备名称:
    EQPName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 计划日期:
    PlanDate = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 制药任务单号:
    TaskID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次号:
    BatchID = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 顺序号:
    PlanSeq = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺路线名称:
    PDUnitRouteName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 计划类型:
    PlanType = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名名称:
    BrandName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 计划重量:
    PlanQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际重量:
    ActQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划开始时间
    PlanStartTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划结束时间
    PlanEndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际开始时间:
    ActBeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际完成时间:
    ActEndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次开始运行班次
    StartBC = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次结束运行班次
    EndBC = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # # 设定重复次数:
    # SetRepeatCount = Column(Integer, primary_key=False, autoincrement=False, nullable=True, default=1)
    #
    # # 当前重复次数:
    # CurretnRepeatCount = Column(Integer, primary_key=False, autoincrement=False, nullable=True, default=0)

    # 实际罐号:
    ActTank = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 任务状态:
    TaskStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 任务锁定状态:
    LockStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# ProductLine:
class ProductLine(Base):
    '''生产线定义'''
    __tablename__ = "ProductLine"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 生产线编码:
    PLineCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 生产线名称:
    PLineName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 区域编码:
    AreaCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域名称:
    AreaName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 产线能力:
    PLineCapacity = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划类型:
    Seq = Column(Integer, primary_key=False, autoincrement=False, nullable=True)


# ProcessUnit:
class ProcessUnit(Base):
    '''工艺段定义'''
    __tablename__ = "ProcessUnit"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 相关任务数:
    RelateTaskCount = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段额定生产能力:
    PURateCapacity = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段计划生产能力:
    PUPLanCapacity = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)

    # 能力单位:
    CapacityUnit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 静置时间:
    PlaceTime = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)

    # 时间单位:
    TimeUnit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺运行时长:
    PURunTime = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)

    # 工艺等待时长:
    PUWaitTime = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)


# ProductRule:
class ProductRule(Base):
    '''产品定义'''
    __tablename__ = "ProductRule"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 产品定义编码:
    BrandCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 产品定义名称:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 药品类型
    BrandType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次重量:
    BatchWeight = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次时长
    BatchTimeLength = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)

    # 发布日期:
    Publish_date = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 使用日期:
    Appy_date = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否使用:
    IsUsed = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 发送WMS:
    SendFlag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # # 可用生产线:
    # AvalProductLine = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)


# ProductUnit:
class ProductUnit(Base):
    '''产品段定义'''
    __tablename__ = "ProductUnit"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 产品定义编码:
    BrandCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 产品定义名称:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 顺序号:
    Seq = Column(Integer, primary_key=False, autoincrement=False, nullable=True)


# ProductControlTask:
class ProductControlTask(Base):
    '''产品段任务配置'''
    __tablename__ = "ProductControlTask"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)

    # 产品段编码:
    PDCtrlTaskCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 产品段名称:
    PDCtrlTaskName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 低限:
    LowLimit = Column(Float(53), primary_key=False, autoincrement=False, nullable=True)

    # 高限:
    HighLimit = Column(Float(53), primary_key=False, autoincrement=False, nullable=True)

    # 相关任务数:
    RelateTaskCount = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 产品定义ID:
    ProductRuleID = Column(Integer, nullable=False, primary_key=False)

    # 顺序号:
    Seq = Column(Integer, primary_key=False, autoincrement=False, nullable=True)


# ProductParameter:
class ProductParameter(Base):
    '''工艺参数配置'''
    __tablename__ = "ProductParameter"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)

    # 产品段工艺参数编码:
    PDParaCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 产品段工艺参数名称:
    PDParaName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 品名:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 值:
    Value = Column(Float(53), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)



# ProductUnitRoute:
class ProductUnitRoute(Base):
    '''工艺路线'''
    __tablename__ = "ProductUnitRoute"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)

    # 工艺路线编码:
    PDUnitRouteCode = Column(Unicode(64), nullable=False, primary_key=False)

    # 工艺路线名称:
    PDUnitRouteName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 持续时间:
    Duration = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 产品定义ID:
    ProductRuleID = Column(Integer, nullable=False, primary_key=False)

    # 工艺段ID:
    PUID = Column(Integer, nullable=False, primary_key=False)

    # 顺序号:
    Seq = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

#生产计划
class PlanManager(Base):
    '''生产计划'''
    __tablename__ = "PlanManager"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 调度编号:
    SchedulePlanCode = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 计划编号
    PlanNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次号:
    BatchID = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 计划重量:
    PlanQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 药品类型
    BrandType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划状态:
    PlanStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划开始时间:
    PlanBeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划完成时间:
    PlanEndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际开始时间:
    ActBeginTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 实际完成时间:
    ActEndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 调度类型:
    Type = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    #描述
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 保存设备:
    EqpCodes = Column(Unicode(300), primary_key=False, autoincrement=False, nullable=True)

    # # 生产线编码:
    # PLineCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)
    #
    # # 生产线名称:
    # PLineName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)


    # 序号:
    Seq = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# PLineID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)
#
# PLineName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)



class TypeDetail(Base):
    '''电子批记录type维护表'''
    __tablename__ = "TypeDetail"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 类型编码
    TypeCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 类型名称
    TypeName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 所属工艺段
    PUID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 注释
    Description = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)


class MaterialBOM(Base):
    '''物料BOM表'''
    __tablename__ = "MaterialBOM"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 物料编码:
    MATCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 物料名称:
    MATName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 投料批总重量:
    BatchTotalWeight = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 投料单一物料计划重量:
    BatchSingleMATWeight = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 百分比:
    BatchPercentage = Column(Unicode(53), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 等级:
    Grade = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

class TaskNoGenerator(Base):
    '''企业编码'''
    __tablename__ = "TaskNoGenerator"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 单位编码:
    TaskNoInt = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 单位名称:
    TaskNoVar = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

class ZYPlanWMS(Base):
    '''与WMS计划管理'''
    __tablename__ = 'ZYPlanWMS'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名ID:
    BrandID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段
    PUIDName = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 执行状态
    ExcuteStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 操作人:
    OperationPeople = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(60), primary_key=False, autoincrement=False, nullable=True)

    # 操作时间:
    OperationDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

    #是否发送
    IsSend = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)


class Material(Base):
    '''物料基础信息表'''
    __tablename__ = "Material"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 物料编码:
    MATCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 物料名称:
    MATName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 物料描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 物料类型:
    MATType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 顺序号:
    Seq = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 等级:
    Grade = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 发送WMS:
    SendFlag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # # 物料标识:1为排产所常用表标识
    # MATBatchNo = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)


class BatchMaterialInfo(Base):
    '''物料明细表'''
    __tablename__ = "BatchMaterialInfo"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 设备编码:
    EQPCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 设备名称:
    EQPName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 物料名称:
    MATName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 投料顺序:
    FeedingSeq = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 桶号:
    BucketNum = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 重量:
    BucketWeight = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 标识（桶/托盘）:
    Flag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 发送WMS:
    SendFlag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 投料完成时间:
    FinishDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 操作时间:
    OperationDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 轮次:
    TaskTurn = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)




# 批记录模板
class BatchModel(Base):
    __tablename__ = "BatchModel"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段
    PUIDName = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 文件（文件名）:FilePath
    FileName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 文件路径（文件名）:
    FilePath = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 上传人:
    UserName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 模板的字符串:
    Parameter = Column(Unicode(MAX), primary_key=False, autoincrement=False, nullable=True)

# 批次使用模板
class BatchUseModel(Base):
    __tablename__ = "BatchUseModel"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段
    PUIDName = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 使用的字符串:
    UseParameter = Column(Unicode(MAX), primary_key=False, autoincrement=False, nullable=True)

# 原料单检验
class StapleProducts(Base):
    __tablename__ = 'StapleProducts'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 单据号:
    BillNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次号:
    BatchNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    #关联SAP的采购订单号
    product_code = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单据类型
    btype = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 物料编码:
    mid = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计划数量
    Num = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 实际数量
    FinishNum = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 库房编码
    StoreDef_ID = Column(Unicode(25), default="1", primary_key=False, autoincrement=False, nullable=True)

    # 确认人:
    Confirmer = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 确认状态
    ConfirmStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 复核人:
    CheckedPeople = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 复核状态
    CheckedStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 审核人:
    Reviewer = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 审核状态
    ReviewStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 质保确认:
    QAConfirmer = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 质保确认状态
    QAConfirmStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 修改日期:
    OperationDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否关联:
    IsRelevance= Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# WMS对应托盘信息
class WMSTrayNumber(Base):
    __tablename__ = 'WMSTrayNumber'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 批次号:
    BatchNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 桶号:
    TrayNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 产品编号
    MID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 托盘号:
    PalletID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 配方号:
    FormulaID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 重量:
    MWeight = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 设备名称:
    EQPName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 进罐时间
    inTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 出罐时间
    outTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 更新时间
    UpdateTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)



# 排产库存表
class SchedulingStock(Base):
    __tablename__ = "SchedulingStock"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 产品(即物料)编码
    product_code = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)
    # 物料名称
    MATName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 仓库库存
    StockHouse = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 安全库存
    SafetyStock = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 创建时间
    create_time = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)
    # 修改时间
    update_time = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

# 与WMS状态同步表
class WMStatusLoad(Base):
    __tablename__ = 'WMStatusLoad'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 工单号:
    BillNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 物料编码:
    mid = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 批次号:
    BatchNo = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 库房号（缺省值为1）
    StoreDef_ID = Column(Unicode(25), default="1",primary_key=False, autoincrement=False, nullable=True)

    # 原状态
    OldStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)

    # 新状态
    NewStatus = Column(Unicode(25), primary_key=False, autoincrement=False, nullable=True)


# SchedulePlan:
class SchedulePlan(Base):
    __tablename__ = "SchedulePlan"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)

    # 调度编号:
    SchedulePlanCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 调度计划开始时间:
    PlanBeginTime = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

    # 调度计划结束时间:
    PlanEndTime = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

    # 调度类型:
    Type = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

class ProductEquipment(Base):
    '''生产设备定义（用于维护工艺段下的生产设备）'''
    __tablename__ = "ProductEquipment"

    # ID:
    ID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=True)

    # 设备编码:
    EQPCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 设备名称:
    EQPName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 设备状态:
    EQPStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 描述:
    Description = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)

    # 设备编号:
    Number = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

# 批记录操作步骤（SOP）
class EletronicBatchDataStore(Base):
    __tablename__ = 'EletronicBatchDataStore'
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 批次号:
    BatchID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 工艺段编码:
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)

    # 操作步骤内容:
    Content = Column(Unicode(60), primary_key=False, autoincrement=False, nullable=True)

    # 操作值:
    OperationpValue = Column(Unicode(20), primary_key=False, autoincrement=False, nullable=True)

    #操作人:
    Operator = Column(Unicode(32), primary_key = False, autoincrement = False, nullable = True)

    # 描述:
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)

    # 品名ID
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# 投料规则表
class FeedingRules(Base):
    __tablename__ = "FeedingRules"
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 对应桶/托盘数:
    BucketSum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 投料条件:
    Condition = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)



# 生成表单的执行语句
Base.metadata.create_all(engine)
