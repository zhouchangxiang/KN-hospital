import json

import redis
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from flask_login import current_user
import pymysql
from database import constant
from enum import Enum, IntEnum, unique
DB_URL = 'mysql+pymysql://root:1qaz2wsx@127.0.0.1:3306/hstl?charset=utf8'

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
db_session = Session()
pool = redis.ConnectionPool(host=constant.REDIS_HOST, password=constant.REDIS_PASSWORD, decode_responses=True)
class SchedulingStatus(Enum):
    Locl = "1" #排产表批次已经生产则为锁定状态
    Unlock = "0" #批次还未生产


