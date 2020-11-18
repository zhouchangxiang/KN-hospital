import datetime
import decimal
import json
from flask_sqlalchemy import BaseQuery
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        # if isinstance(obj.__class__, AppenderBaseQuery):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                try:
                    data = obj.__getattribute__(field)
                    if isinstance(obj.__getattribute__(field), (str, int)):
                        fields[field] = data
                    elif isinstance(data, (BaseQuery, type)):
                        pass
                    elif isinstance(data, datetime.datetime):
                        fields[field] = data.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                    elif isinstance(data, datetime.date):
                        fields[field] = data.strftime("%Y-%m-%d")
                    elif isinstance(data, decimal.Decimal):
                        fields[field] = float(data)
                    # 数据库表多对多查询序列化
                    elif isinstance(data, InstrumentedList):
                        fields[field] = '数据库表多对多查询序列化'
                        # fields[field] = MyEncoder.default(self, data)
                    else:
                        fields[field] = MyEncoder.default(self, data)
                        # pass
                except TypeError as e:
                    print('序列化错误原因：', e)
            return fields
        return json.JSONEncoder.default(self, obj)
