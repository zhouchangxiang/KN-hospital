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


class CheckForm(Base):
    """请验单"""
    __tablename__ = 'CheckForm'
    Id = Column(Integer, autoincrement=True, primary_key=True)
    # 请验单号
    CheckNumber = Column(Unicode(32), nullable=True)
    # 品名
    Name = Column(Unicode(32), nullable=True)
    # 规格
    Specs = Column(Unicode(32), nullable=True)
    # 供货单位
    Supplier = Column(Unicode(32), nullable=True, default='无')
    # 来料批号
    ProductNumber = Column(Unicode(32), nullable=True)
    # 批号（物料代码）
    Number = Column(Unicode(32), nullable=True)
    # 数量
    Amount = Column(Unicode(16), nullable=True)
    # 请验工序
    CheckProcedure = Column(Unicode(32), nullable=True)
    # 请验部门
    CheckDepartment = Column(Unicode(32), nullable=True)
    # 请验时间
    CheckDate = Column(Unicode(32), default=datetime.now().strftime('%Y-%m-%d'))
    # 请验人
    CheckUser = Column(Unicode(16), nullable=True)
    # 请验单类型（标准请验，小样请验）
    Type = Column(Unicode(16), nullable=True)
    # 小样请验单审核状态（待审核，未通过，已通过）
    Status = Column(Unicode(16), nullable=True, default='待审核')
    # 备注
    Comment = Column(Unicode(32), nullable=True)


# 生成表单的执行语句
Base.metadata.create_all(engine)
