from sqlalchemy import Column, Integer, Unicode
from datetime import datetime

from common.asd import Base, engine


class CleanRecord(Base):
    """清洗记录"""
    __tablename__ = 'CleanRecord'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 日期
    Time = Column(Unicode(128), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 具体位置
    Position = Column(Unicode(512), nullable=True)
    # 盘管台数
    PanAmount = Column(Unicode(512), nullable=True)
    # 清洗消毒回风口过滤网及台数
    HuiFengAmount = Column(Unicode(512), nullable=True)
    # 清洗消毒送风口个数
    SongFengAmount = Column(Unicode(512), nullable=True)
    # 托水盘清洗加药台数
    TuoPanAmount = Column(Unicode(512), nullable=True)
    # 乙方人员
    YUser = Column(Unicode(512), nullable=True)
    # 甲方人员
    JUser = Column(Unicode(512), nullable=True)
    # 备注
    Comment = Column(Unicode(512), nullable=True)


class NoClean(Base):
    """未清洗记录"""
    __tablename__ = 'NoClean'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 日期
    Time = Column(Unicode(128), nullable=True)
    # 位置
    Position = Column(Unicode(512), nullable=True)
    # 设备编号
    EquipmentNo = Column(Unicode(512), nullable=True)


class WaterOperation(Base):
    """水处理工作单"""
    __tablename__ = 'WaterOperation'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 甲方单位名称
    A1 = Column(Unicode(128), nullable=True)
    # 水处理工作内容
    A2 = Column(Unicode(128), nullable=True)
    # 7001
    A3 = Column(Unicode(128), nullable=True)
    # 8002
    B3 = Column(Unicode(128), nullable=True)
    # 8005
    C3 = Column(Unicode(128), nullable=True)
    # 8006
    D3 = Column(Unicode(128), nullable=True)
    # 8010
    E3 = Column(Unicode(128), nullable=True)
    # 8020
    F3 = Column(Unicode(128), nullable=True)
    # 8022
    G3 = Column(Unicode(128), nullable=True)
    # 8026
    H3 = Column(Unicode(128), nullable=True)
    # 8036
    I3 = Column(Unicode(128), nullable=True)
    # 9002
    A4 = Column(Unicode(128), nullable=True)
    # 9008
    B4 = Column(Unicode(128), nullable=True)
    # 9016
    C4 = Column(Unicode(128), nullable=True)
    # 9017
    D4 = Column(Unicode(128), nullable=True)
    # 9009
    E4 = Column(Unicode(128), nullable=True)
    # 9010
    F4 = Column(Unicode(128), nullable=True)
    # 9004B
    G4 = Column(Unicode(128), nullable=True)
    # 9004A
    H4 = Column(Unicode(128), nullable=True)
    # 9005
    I4 = Column(Unicode(128), nullable=True)
    # 清洗冷却塔盘
    A5 = Column(Unicode(128), nullable=True)
    B5 = Column(Unicode(128), nullable=True)
    C5 = Column(Unicode(128), nullable=True)
    A6 = Column(Unicode(128), nullable=True)
    B6 = Column(Unicode(128), nullable=True)
    C6 = Column(Unicode(128), nullable=True)
    A8 = Column(Unicode(128), nullable=True)
    # 7001
    A9 = Column(Unicode(128), nullable=True)
    # 8002
    B9 = Column(Unicode(128), nullable=True)
    # 8010
    C9 = Column(Unicode(128), nullable=True)
    # 9004B
    D9 = Column(Unicode(128), nullable=True)
    # 9004A
    E9 = Column(Unicode(128), nullable=True)
    # 9010
    F9 = Column(Unicode(128), nullable=True)
    # 9015
    G9 = Column(Unicode(128), nullable=True)
    # 9005
    H9 = Column(Unicode(128), nullable=True)
    # 9007
    I9 = Column(Unicode(128), nullable=True)
    A10 = Column(Unicode(128), nullable=True)
    B10 = Column(Unicode(128), nullable=True)
    A11 = Column(Unicode(128), nullable=True)
    B11 = Column(Unicode(128), nullable=True)
    A12 = Column(Unicode(128), nullable=True)
    A13 = Column(Unicode(128), nullable=True)
    B13 = Column(Unicode(128), nullable=True)
    C13 = Column(Unicode(128), nullable=True)
    A14 = Column(Unicode(128), nullable=True)
    A15 = Column(Unicode(128), nullable=True)


class RunError(Base):
    """系统运行错误 """
    __tablename__ = 'RunError'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 发生时间
    Time = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 操作IP
    IP = Column(Unicode(32), nullable=True)
    # 请求路径
    Path = Column(Unicode(32), nullable=True)
    # 调用函数
    Func = Column(Unicode(32), nullable=True)
    # 请求方法
    Method = Column(Unicode(32), nullable=True)
    # 错误信息
    Error = Column(Unicode(128), nullable=True)


class Notice(Base):
    """通知公告"""
    __tablename__ = 'Notice'
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 公告标题
    Title = Column(Unicode(128), nullable=True)
    # 类型
    NoticeType = Column(Unicode(128), nullable=True)
    # 状态
    Status = Column(Unicode(128), nullable=True)
    # 工作内容
    Content = Column(Unicode(1024), nullable=True)
    # 创建人
    Name = Column(Unicode(64), nullable=True)
    # 创建时间
    NoticeTime = Column(Unicode(64), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


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
    # 设备型号
    EquipmentModel = Column(Unicode(512), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(512), nullable=True)
    # 楼层
    Floor = Column(Unicode(32), nullable=True)
    # 区域
    Area = Column(Unicode(32), nullable=True)
    # 添加日期
    AddTime = Column(Unicode(32), nullable=True)
    # 设备状态（正常）
    Status = Column(Unicode(32), default="正常", nullable=True)
    # 供应商
    Manufacturer = Column(Unicode(128), nullable=True)
    # 供应商联系人
    ManufacturerUser = Column(Unicode(128), nullable=True)
    # 供应商电话
    ManufacturerPhone = Column(Unicode(128), nullable=True)
    # 保养公司
    KeepCompany = Column(Unicode(128), nullable=True)
    # 保养公司联系人
    KeepUser = Column(Unicode(128), nullable=True)
    # 保养公司电话
    KeepPhone = Column(Unicode(128), nullable=True)
    # 维修公司
    RepairCompany = Column(Unicode(128), nullable=True)
    # 维修公司联系人
    RepairUser = Column(Unicode(128), nullable=True)
    # 维修公司
    RepairPhone = Column(Unicode(128), nullable=True)
    # 注释:
    Comment = Column(Unicode(512), nullable=True, default='')


class EquipmentLife(Base):
    """设备全生命周期"""
    __tablename__ = 'EquipmentLife'
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编号
    EquipmentNo = Column(Unicode(32), nullable=True)
    # 操作时间
    OperationTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 事项
    Item = Column(Unicode(32), nullable=True)
    # 内容
    Content = Column(Unicode(128), nullable=True)
    # 处理情况
    Situation = Column(Unicode(128), nullable=True, default='已处理')
    # 处理人
    Name = Column(Unicode(32), nullable=True)
    # 完成时间
    CompleteTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


class Inspection(Base):
    """巡检记录"""
    __tablename__ = 'Inspection'

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编号
    EquipmentNo = Column(Unicode(32), nullable=True)
    # 巡检时间
    InspectionTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 计划状态（正常,预警，故障，保养）
    Status = Column(Unicode(32), nullable=True)
    # 注释:
    Comment = Column(Unicode(512), nullable=True, default='')


class YunWei(Base):
    """运维大师"""
    __tablename__ = 'YunWei'
    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编号
    EquipmentNo = Column(Unicode(32), nullable=True)
    # 人员
    Name = Column(Unicode(32), nullable=True)
    # 邮箱
    Mail = Column(Unicode(32), nullable=True)
    # 时间
    YunWeiTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 维护位置
    Position = Column(Unicode(32), nullable=True)
    # 问题数量
    WNumber = Column(Unicode(32), nullable=True)
    # 平台指令
    Instructions = Column(Unicode(32), nullable=True)
    # 结果
    Result = Column(Unicode(32), nullable=True)


class BaoYang(Base):
    """资产列表-设备保养"""
    __tablename__ = 'BaoYang'

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编号
    EquipmentNo = Column(Unicode(32), nullable=True)
    # 巡检时间
    BaoYangTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 注释:
    Comment = Column(Unicode(512), nullable=True, default='')


class Tags(Base):
    """设备采集点配置"""
    __tablename__ = 'Tags'
    # ID
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    # 设备编码:
    EquipmentCode = Column(Unicode(32), nullable=True)
    # 采集点参数
    Tag = Column(Unicode(128), nullable=True)
    # 描述
    Comment = Column(Unicode(128), nullable=True)
    # 设备类型
    EquipmentType = Column(Unicode(128), nullable=True)
    # 设备楼层
    Floor = Column(Unicode(128), nullable=True)


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
    # 保养计划名称
    KeepName = Column(Unicode(128), nullable=True)
    # 设备名称
    EquipmentName = Column(Unicode(32), nullable=True)
    # 设备编码
    EquipmentCode = Column(Unicode(128), nullable=True)
    # 计划负责人
    Worker = Column(Unicode(32), nullable=True)
    # # 工单状态
    # Status = Column(Unicode(32), default="待保养")
    # 保养时间
    KeepTime = Column(Unicode(32), nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 进度
    Speed = Column(Unicode(32), nullable=True)


class Responsible(Base):
    """负责人维护"""
    __tablename__ = 'Responsible'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 姓名
    Name = Column(Unicode(32), nullable=True)
    # 电话
    Phone = Column(Unicode(32), nullable=True)
    # 邮箱
    Mail = Column(Unicode(32), nullable=True)


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
