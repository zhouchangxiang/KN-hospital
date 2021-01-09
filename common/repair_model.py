from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, ForeignKey, Table, DateTime, Integer, String
from sqlalchemy import Column, DateTime, Float, Integer, String, Unicode, BigInteger
from sqlalchemy.dialects.mssql.base import BIT
from datetime import datetime
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


# 创建对象的基类
from database.db_operate import DB_URL
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)


class Equipment(Base):
    __tablename__ = "Equipment"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编号
    EquipmentNo = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(32), nullable=True)
    # 设备类型
    EquipmentType = Column(Unicode(512), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(512), nullable=True)
    # 区域
    Area = Column(Unicode(32), nullable=True)
    # 添加日期
    AddTime = Column(Unicode(32), nullable=True)
    # 设备状态（正常，维修中）
    Status = Column(Unicode(32), default="正常", nullable=True)
    # 注释:
    Comment = Column(Unicode(32), nullable=True, default='')


class Plan(Base):
    __tablename__ = 'Plan'

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编码:
    EquipmentCode = Column(Unicode(30), nullable=True)
    # 班组
    WorkNo = Column(Unicode(32), nullable=False)
    # 工单类型(维修，保养)
    Type = Column(Unicode(32), nullable=True)
    # 计划状态（良好,异常）
    Status = Column(Unicode(32), default="待处理")
    # 提醒状态（待提醒，已提醒）
    RemindStatus = Column(Unicode(32), default="待提醒", nullable=True)
    # 预工作时间
    WorkTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class KeepPlan(Base):
    """保养计划表"""
    __tablename__ = 'keepplan'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
    # 设备名称
    EquipmentName = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 制定计划人
    Worker = Column(Unicode(32), nullable=True)
    # 工单状态
    Status = Column(Unicode(32), default="待保养")
    # 制定计划时间
    ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 保养班组
    # Group = Column(Unicode(32), nullable=True)
    # 任务开始时间（递增）
    StartTime = Column(Unicode(32), nullable=True)
    # 计划描述
    Describe = Column(Unicode(128), nullable=True)
    # 工作周期
    WeekTime = Column(Unicode(128), nullable=True)
    # 工作类型
    Type = Column(Unicode(32), nullable=True)
    # 工作时间
    WorkTime = Column(Unicode(128), nullable=True)


class KeepTask(Base):
    """保养任务表"""
    __tablename__ = 'keeptask'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
    # 设备名称
    EquipmentName = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 制定计划人
    Worker = Column(Unicode(32), nullable=True)
    # 保养班组
    GroupNo = Column(Unicode(32), nullable=True)
    # 工单状态
    Status = Column(Unicode(32), nullable=True)
    # 制定计划时间
    ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 保养确认人
    # KeepWorker = Column(Unicode(32), nullable=True)
    # 任务开始时间（递增）
    StartTime = Column(Unicode(32), nullable=True, default='尚未接单')
    # 计划描述
    Describe = Column(Unicode(128), nullable=True)
    # 工作周期
    WeekTime = Column(Unicode(128), nullable=True)
    # 工作类型
    Type = Column(Unicode(32), nullable=True)
    # 工作时间
    WorkTime = Column(Unicode(128), nullable=True)


class KeepRecord(Base):
    """保养记录表"""
    __tablename__ = 'keeprecord'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
    # 设备名称
    EquipmentName = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 制定计划人
    Worker = Column(Unicode(32), nullable=True)
    # 保养班组
    MaintainGroup = Column(Unicode(32), nullable=True)
    # 工单状态
    Status = Column(Unicode(32), default="已完成")
    # 制定计划时间
    ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 保养确认人
    KeepWorker = Column(Unicode(32), nullable=True)
    # 任务开始时间（递增）
    StartTime = Column(Unicode(32), nullable=True)
    # 计划描述
    Describtion = Column(Unicode(128), nullable=True)
    # 保养内容
    Content = Column(Unicode(128), nullable=True)
    # 工作周期
    WeekTime = Column(Unicode(128), nullable=True)
    # 完成时间
    EndTime = Column(Unicode(32), nullable=True)
    # 工作类型
    Type = Column(Unicode(32), nullable=True)


class Repair(Base):
    """维修申请表"""
    __tablename__ = 'repair'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
    # 设备名称
    EquipmentName = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 申请人
    Worker = Column(Unicode(32), nullable=True)
    # 故障阐述
    FaultExpound = Column(Unicode(128), nullable=True)
    # 工单状态（待接单，已接单）
    Status = Column(Unicode(32), default="待接单")
    # 申请时间
    ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 接单人
    ReceiveWorker = Column(Unicode(32), nullable=True, default='')
    # 接单时间
    ReceiveTime = Column(Unicode(32), nullable=True, default='尚未接单')


class RepairTask(Base):
    """维修任务表"""
    __tablename__ = 'repairtask'

    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 工单号
    No = Column(Unicode(128), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 申请人
    Worker = Column(Unicode(32), nullable=True)
    # 维修人
    ReceiveWorker = Column(Unicode(32), nullable=True)
    # 工单状态（维修完成）
    Status = Column(Unicode(32), default="维修完成")
    # 维修内容
    Content = Column(Unicode(128), nullable=True)
    # 申请时间
    ApplyTime = Column(Unicode(32), nullable=True)
    # 接单时间
    ReceiveTime = Column(Unicode(32), nullable=True)
    # 完成时间
    EndTime = Column(Unicode(32), nullable=True)


class Disease(Base):
    """病患表"""
    __tablename__ = 'Disease'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 楼层
    Floor = Column(Unicode(128), nullable=True)
    # 患病程度(轻-中-重)
    Degree = Column(Unicode(32), nullable=True)
    # 轻人数
    LightNumber = Column(Unicode(32), nullable=True)
    # 中人数
    CentreNumber = Column(Unicode(32), nullable=True)
    # 重人数
    HeightNumber = Column(Unicode(32), nullable=True)
    # 跨区人数
    Region = Column(Unicode(32), nullable=True)
    # 移动人数
    Move = Column(Unicode(32), nullable=True)


Base.metadata.create_all(engine)
