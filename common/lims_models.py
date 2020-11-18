from datetime import datetime

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


# class ConclusionRecord(Base):
#     """报告完成记录"""
#     __tablename__ = 'ConclusionRecord'
#     Id = Column(Integer, autoincrement=True, primary_key=True)
#     # 检验编号
#     TestNumber = Column(Unicode(32), nullable=True)
#     # 请验单日期
#     TestDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d'))
#     # 实际送样时间
#     ActualTime = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d'))
#     # 检验日期
#     CheckDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d'))
#     # 产品名称
#     Name = Column(Unicode(32), nullable=True)
#     # 产品批号
#     ProductNumber = Column(Unicode(32), nullable=True)
#     # 送样部门
#     SampleDepartment = Column(Unicode(32), nullable=True)
#     # 类别(成品、药膏、中间产品、原料、辅料)
#     Type = Column(Unicode(32), nullable=True)
#     # 药剂类型
#     medicine = Column(Unicode(32), nullable=True)
#     # 规格
#     Specs = Column(Unicode(32), nullable=True)
#     # 大小样
#     BigLevel = Column(Unicode(32), nullable=True)
#     # 药膏
#     ointment = Column(Unicode(32), nullable=True)
#     # 检验项目
#     CheckProject = Column(Unicode(32), nullable=True)
#     # 法定标准
#     StatutoryStandards = Column(Unicode(32), nullable=True)
#     # 内验标准
#     InnerStandards = Column(Unicode(32), nullable=True)
#     # 检验结果
#     Comment = Column(Unicode(32), nullable=True)
#     # 判定
#     Judge = Column(Unicode(32), nullable=True)
#     # 检验人
#     CheckName = Column(Unicode(32), nullable=True)
#
#
# class ProductSave(Base):
#     """产品留样"""
#     __tablename__ = 'ProductSave'
#     Id = Column(Integer, autoincrement=True, primary_key=True)
#     # 产品名称
#     Name = Column(Unicode(32), nullable=True)
#     # 规格
#     Specs = Column(Unicode(32), nullable=True)
#     # 包装规格
#     PackSpecs = Column(Unicode(32), nullable=True)
#     # 产品批号
#     ProductNumber = Column(Unicode(32), nullable=True)
#     # 理论产量
#     TheoreticalYield = Column(Unicode(32), nullable=True)
#     # 留样数量
#     BatchAmount = Column(Unicode(32), nullable=True)
#     # 留样部门
#     BatchDepartment = Column(Unicode(32), nullable=True)
#     # 留样人
#     BatchName = Column(Unicode(32), nullable=True)
#     # 经手人
#     Handler = Column(Unicode(32), nullable=True)
#     # 生产日期
#     ProductionDate = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d'))
#     # 有效日期
#     ValidityDate = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d'))
#     # 备注
#     Comment = Column(Unicode(32), nullable=True)
#
#
# class ProductSaveSurvey(Base):
#     """产品留样观察表"""
#     __tablename__ = 'ProductSaveSurvey'
#
#     Id = Column(Integer, autoincrement=True, primary_key=True)
#     # 品名
#     Name = Column(Unicode(32), nullable=True)
#     # 温度
#     Temperature = Column(Unicode(32), nullable=True)
#     # 相对湿度
#     RH = Column(Unicode(32), nullable=True)
#     # 留样位置
#     position = Column(Unicode(32), nullable=True)
#     # 留样批号
#     BatchNumber = Column(Unicode(32), nullable=True)
#     # 留样日期
#     BatchDate = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d'))
#     # 规格
#     Specs = Column(Unicode(32), nullable=True)
#     # 留样量
#     BatchAmount = Column(Unicode(32), nullable=True)
#     # 经手人
#     Handler = Column(Unicode(32), nullable=True)
#     # 观察项目
#     Project = Column(Unicode(32), nullable=True)
#     # 观察结果（按月统计）
#     # 6个月
#     SixMonth = Column(Unicode(32), nullable=True)
#     # 12个月
#     TwelveMonth = Column(Unicode(32), nullable=True)
#     # 18个月
#     EighteenMonth = Column(Unicode(32), nullable=True)
#     # 24个月
#     TwentyFourMonth = Column(Unicode(32), nullable=True)
#     # 30个月
#     ThirtyMonth = Column(Unicode(32), nullable=True)
#     # 36个月
#     ThirtySix = Column(Unicode(32), nullable=True)
#     # 48个月
#     FortyEight = Column(Unicode(32), nullable=True)
#     # 结论
#     Conclude = Column(Unicode(32), nullable=True)
#     # 备注
#     Comment = Column(Unicode(32), nullable=True)
#
#
# class KeepPlan(Base):
#     """仪器保养计划表"""
#     __tablename__ = 'KeepPlan'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
#     # 仪器编码
#     InstrumentCode = Column(Unicode(128), nullable=True)
#     # 制定计划人
#     Worker = Column(Unicode(32), nullable=True)
#     # 工单状态
#     Status = Column(Unicode(32), default="待保养")
#     # 制定计划时间
#     ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 保养班组
#     # Group = Column(Unicode(32), nullable=True)
#     # 任务开始时间（递增）
#     StartTime = Column(Unicode(32), nullable=True)
#     # 计划描述
#     Describe = Column(Unicode(128), nullable=True)
#     # 工作周期
#     WeekTime = Column(Unicode(128), nullable=True)
#     # 工作类型
#     Type = Column(Unicode(32), nullable=True)
#     # 工作时间
#     WorkTime = Column(Unicode(128), nullable=True)
#
#
# class KeepTask(Base):
#     """保养任务表"""
#     __tablename__ = 'KeepTask'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
#     # 仪器编码
#     InstrumentCode = Column(Unicode(128), nullable=True)
#     # 制定计划人
#     Worker = Column(Unicode(32), nullable=True)
#     # 保养班组
#     Group = Column(Unicode(32), nullable=True)
#     # 工单状态
#     Status = Column(Unicode(32), nullable=True)
#     # 制定计划时间
#     ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 保养确认人
#     # KeepWorker = Column(Unicode(32), nullable=True)
#     # 任务开始时间（递增）
#     StartTime = Column(Unicode(32), nullable=True, default='尚未接单')
#     # 计划描述
#     Describe = Column(Unicode(128), nullable=True)
#     # 工作周期
#     WeekTime = Column(Unicode(128), nullable=True)
#     # 工作类型
#     Type = Column(Unicode(32), nullable=True)
#     # 工作时间
#     WorkTime = Column(Unicode(128), nullable=True)
#
#
# class KeepRecord(Base):
#     """保养记录表"""
#     __tablename__ = 'KeepRecord'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
#     # 仪器编码
#     InstrumentCode = Column(Unicode(128), nullable=True)
#     # 制定计划人
#     Worker = Column(Unicode(32), nullable=True)
#     # 保养班组
#     Group = Column(Unicode(32), nullable=True)
#     # 工单状态
#     Status = Column(Unicode(32), default="已完成")
#     # 制定计划时间
#     ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 保养确认人
#     KeepWorker = Column(Unicode(32), nullable=True)
#     # 任务开始时间（递增）
#     StartTime = Column(Unicode(32), nullable=True)
#     # 计划描述
#     Describe = Column(Unicode(128), nullable=True)
#     # 保养内容
#     Content = Column(Unicode(128), nullable=True)
#     # 工作周期
#     WeekTime = Column(Unicode(128), nullable=True)
#     # 完成时间
#     EndTime = Column(Unicode(32), nullable=True)
#     # 工作类型
#     Type = Column(Unicode(32), nullable=True)
#
#
# class Repair(Base):
#     """维修申请表"""
#     __tablename__ = 'Repair'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     No = Column(Unicode(128), nullable=True, default=datetime.now().strftime('%Y%m%d%H%M%S'))
#     # 仪器编码
#     InstrumentCode = Column(Unicode(128), nullable=True)
#     # 申请人
#     Worker = Column(Unicode(32), nullable=True)
#     # 故障阐述
#     FaultExpound = Column(Unicode(128), nullable=True)
#     # 工单状态（待接单，已接单）
#     Status = Column(Unicode(32), default="待接单")
#     # 申请时间
#     ApplyTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     # 接单人
#     ReceiveWorker = Column(Unicode(32), nullable=True, default='')
#     # 接单时间
#     ReceiveTime = Column(Unicode(32), nullable=True, default='尚未接单')
#
#
# class RepairTask(Base):
#     """维修任务表"""
#     __tablename__ = 'RepairTask'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     # 工单号
#     No = Column(Unicode(128), nullable=True)
#     # 仪器编码
#     InstrumentCode = Column(Unicode(128), nullable=True)
#     # 仪器名称
#     # Name = Column(Unicode(32), nullable=True)
#     # 申请人
#     Worker = Column(Unicode(32), nullable=True)
#     # 维修人
#     ReceiveWorker = Column(Unicode(32), nullable=True)
#     # 工单状态（维修完成）
#     Status = Column(Unicode(32), default="维修完成")
#     # 维修内容
#     Content = Column(Unicode(128), nullable=True)
#     # 申请时间
#     ApplyTime = Column(Unicode(32), nullable=True)
#     # 接单时间
#     ReceiveTime = Column(Unicode(32), nullable=True)
#     # 完成时间
#     EndTime = Column(Unicode(32), nullable=True)


# 生成表单的执行语句
Base.metadata.create_all(engine)
