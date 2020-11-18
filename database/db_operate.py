import json

import redis
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from flask_login import current_user
import pymssql
from database import constant
from enum import Enum, IntEnum, unique
DB_URL = 'mysql+pymysql://root:root@127.0.0.1:3306/sz?charset=utf8'#Ty123456@192.168.2.101

engine = create_engine(DB_URL)#Qcsw@758@192.168.2.123  root@127.0.0.1
Session = sessionmaker(bind=engine)
db_session = Session()
pool = redis.ConnectionPool(host=constant.REDIS_HOST, password=constant.REDIS_PASSWORD,decode_responses=True)
class SchedulingStatus(Enum):
    Locl = "1" #排产表批次已经生产则为锁定状态
    Unlock = "0" #批次还未生产


