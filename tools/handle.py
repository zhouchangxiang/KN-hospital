import os
import sys
import datetime
import decimal
import json
import time

from flask_sqlalchemy import BaseQuery
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList

from common.KN_model import RunError
from common.asd import db_session


def get_time_stamp(s):
    time_array = time.strptime(s)
    time_stamp = int(time.mktime(time_array))
    return 0 < int(time.time()) - time_stamp < 86400


# 文件类型检查
def is_allowed_type(content_type):
    return content_type.lower() in ['image/jpeg', 'image/png', 'application/msword', 'application/vnd.ms-powerpoint',
                                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                    'application/pdf']


def is_allowed_image(content_type):
    return content_type.lower() in ['image/jpeg', 'image/png']


# 生成时间戳文件名
def generate_filename():
    return f'{str(round(time.time() * 1000))}'


# 获取项目跟路径
def get_root_path():
    path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    return os.path.join(path, 'instruction')


def my_log(e):
    """
    程序日志记录
    :param e:捕获异常参数`
    """
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(root_path, 'run_log\\logs.txt')
    call_func = sys._getframe().f_back.f_code.co_name
    # user = login_user if login_user is None else 'no login'
    with open(file_path, 'a', encoding='utf-8') as f:
        print(f'{datetime.datetime.now()} -- {call_func} --- {e}' + "\n\n")
        f.write(f'{datetime.datetime.now()} -- {call_func} --- {e}' + "\n\n")
        f.close()
        db_session.add(RunError(Time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), Func=call_func, Error=e))
        db_session.commit()
        db_session.close()
    return '日志写入成功'

