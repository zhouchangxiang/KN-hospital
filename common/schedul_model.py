from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, DateTime, Integer, Unicode

from flask_login import LoginManager
from database.connect_db import CONNECT_DATABASE

login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)

# 工厂日历
class plantCalendarScheduling(Base):
    __tablename__ = "plantCalendarMode"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 时间
    start = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)
    # 排产
    title = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)
    #颜色
    color = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)


# 排产表
class Scheduling(Base):
    __tablename__ = "Scheduling"
    ## ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 产品名称
    PRName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    #排产时间(工厂日历)
    SchedulingTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 排产序列号
    SchedulingNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 批数
    BatchNumS = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 排产状态
    SchedulingStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 创建时间
    create_time = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)
    # 修改时间
    update_time = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)


# 排产日历
class scheduledate(Base):
    __tablename__ = "scheduledate"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 日期
    WorkDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 类型
    DateType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 注释
    comment = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)
    # 颜色
    color = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)

# 日期类型
class scheduleDateType(Base):
    __tablename__ = "scheduleDateType"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 类型编码
    DateTypeCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 类型名称
    DateTypeName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 注释
    Description = Column(Unicode(200), primary_key=False, autoincrement=False, nullable=True)
    # 颜色
    color = Column(Unicode(30), primary_key=False, autoincrement=False, nullable=True)

# 得率维护表
class YieldMaintain(Base):
    __tablename__ = "YieldMaintain"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 产品定义名称:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)
    # 得率PRName
    Yield = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 成品总重量
    FinishProduct = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 取样量
    SamplingQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 药材总投料量
    TotalQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

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

# 每日生产批数
class SchedulingStandard(Base):
    __tablename__ = "SchedulingStandard"
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 产品定义名称:
    BrandName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)
    # 批数（批/每天）
    DayBatchNumS = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 物料重量（kg/批）
    Batch_quantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

# 生产计划表
class product_plan(Base):
    '''ERP同步计划'''
    __tablename__ = "product_plan"
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 编号
    PlanNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 药品类型
    BrandType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 计划产值
    PlanQuantity = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 产值单位
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 计划时长
    PlanTimeLen = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 创建时间
    CreateTimeTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 计划交付时间
    PlanFinishTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 实际完成时间
    ActFinishTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 备注
    Description = Column(Unicode(100), primary_key=False, autoincrement=False, nullable=True)
    # 状态
    PlanStatus = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)



# 设备批次运行时间统计表
class EquipmentBatchRunTime(Base):
    __tablename__ = "EquipmentBatchRunTime"
    # id:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    # 批次号
    BatchID = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)
    # 品名编码:
    BrandCode = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 品名名称:
    BrandName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 设备编码:
    EQPCode = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)
    # 设备名称:
    EQPName = Column(Unicode(64), primary_key=False, autoincrement=False, nullable=True)
    # 工艺段
    PUCode = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)
    # 工艺段名称:
    PUName = Column(Unicode(50), primary_key=False, autoincrement=False, nullable=True)
    # 批次开始运行时间
    StartTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 批次结束运行时间
    EndTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 批次开始运行班次
    StartBC = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 批次结束运行班次
    EndBC = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 设备运行时长
    WorkTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)
    # 设备等待时长
    WaitTime = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)



# 生成表单的执行语句
Base.metadata.create_all(engine)
