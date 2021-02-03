from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, DateTime, Float, Integer, Unicode

from database.db_operate import DB_URL

# 创建对象的基类
engine = create_engine(DB_URL, pool_size=10, max_overflow=10, pool_timeout=60, pool_recycle=1800)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)


# TagDetail_START:
class TagDetail(Base):
    __tablename__ = "TagDetail"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 区域名称:
    AreaName = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 器件号:
    DeviceNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # IP地址:
    IP = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 端口:
    Port = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 虚拟分配COM号:
    COMNum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集点名称:
    FEFportIP = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 位置:
    Area = Column(Unicode(65), primary_key=False, autoincrement=False, nullable=True)

    # 备注:
    Description = Column(Unicode(150), primary_key=False, autoincrement=False, nullable=True)

    # 水电汽分类:
    EnergyClass = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # Tag点:
    Address = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 厂商
    Type = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 用电设备
    Equipment = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 是否导出
    # IsExport = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# ElectricEnergy_START:
class ElectricEnergy(Base):
    """电能"""
    __tablename__ = "ElectricEnergy"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 仪表ID:
    EquipmnetID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 价格ID:
    PriceID = Column(Float(53), primary_key=False, autoincrement=False, nullable=True)

    # 采集点:
    Address = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集时间:
    CollectionDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

    # 采集年:
    CollectionYear = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集月:
    CollectionMonth = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集天:
    CollectionDay = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 总功率:
    ZGL = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # A相电压:
    AU = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # A相电流:
    AI = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # B相电压:
    BU = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # B相电流:
    BI = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # C相电压:
    CU = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # C相电压:
    CI = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计算增量更新标识:
    IncrementFlag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 两个相邻采集点上一个采集点ID:
    PrevID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域:
    AreaName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# WaterEnergy_START:
class WaterEnergy(Base):
    """水能"""
    __tablename__ = "WaterEnergy"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 水瞬时流量单位:
    FlowWUnit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 仪表ID:
    EquipmnetID = Column(Integer, primary_key=False, autoincrement=False, nullable=True)

    # 价格ID:
    PriceID = Column(Float(53), primary_key=False, autoincrement=False, nullable=True)

    # 采集点:
    Address = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集时间:
    CollectionDate = Column(DateTime, primary_key=False, autoincrement=False, nullable=True)

    # 采集年:
    CollectionYear = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集月:
    CollectionMonth = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集天:
    CollectionDay = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 瞬时流量:
    WaterFlow = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 累计流量:
    WaterSum = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 水累计量体积单位:
    SumWUnit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 计算增量更新标识:
    IncrementFlag = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 两个相邻采集点上一个采集点ID:
    PrevID = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域:
    AreaName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 水增量表
class IncrementWaterTable(Base):
    __tablename__ = "IncrementWaterTable"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 增量值:
    IncremenValue = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 增量类型:
    IncremenType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集点:
    Address = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集时间:
    CollectionDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域:
    AreaName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 电增量表
class IncrementElectricTable(Base):
    __tablename__ = "IncrementElectricTable"

    # ID:
    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # 增量值:
    IncremenValue = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 增量类型:
    IncremenType = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 单位:
    Unit = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集点:
    Address = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 采集时间:
    CollectionDate = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)

    # 区域:
    AreaName = Column(Unicode(32), primary_key=False, autoincrement=False, nullable=True)


# 生成表单的执行语句_START
Base.metadata.create_all(engine)
