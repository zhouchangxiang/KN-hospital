from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, ForeignKey, Table, DateTime, Integer, String
from sqlalchemy import Column, DateTime, Float, Integer, String, Unicode, BigInteger
from sqlalchemy.dialects.mssql.base import BIT
from datetime import datetime
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
# 创建对象的基类
from database.db_operate import DB_URL
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base(engine)


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

