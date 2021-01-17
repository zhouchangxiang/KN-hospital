import time

import redis
from datetime import datetime

# from database.db_operate import REDIS_PASSWORD, REDIS_HOST, REDIS_TABLENAME
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable, ElectricEnergy, WaterEnergy
from tools.handle import my_log

# redis_coon = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, decode_responses=True)
redis_coon = redis.Redis(host='127.0.0.1', password='liaicheng*521', decode_responses=True)
REDIS_TABLENAME = 'data_realtime'


while True:
    try:
        print('开始写入增量数据')
        address = db_session.query(TagDetail).all()
        for tag in address:
            print(tag.Address)
            data = redis_coon.hget(REDIS_TABLENAME, tag.Address)
            if tag.Type == '电表' and data != 'None' and data != 'init':
                old_data = redis_coon.hget(REDIS_TABLENAME, tag.Address + '_old')
                if data == 'None' or old_data == 'None' or data is None or old_data is None:
                    pass
                else:
                    value = float(data) - float(old_data)
                    db_session.add(
                        IncrementElectricTable(AreaName=tag.AreaName, IncremenValue=str(value), IncremenType='电',
                                               CollectionDate=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                               Address=tag.Address))
                    db_session.commit()
                    redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old', data)
                    redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old_time',
                                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    # if value < 500:
                    #
                    # else:
                    #     pass
            if tag.Type == '水表':
                db_session.add(
                    IncrementWaterTable(AreaName=tag.AreaName, IncremenValue=data, IncremenType='水', CollectionDate=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        Address=tag.Address))
                db_session.commit()
            else:
                pass
        print('结束写入增量数据')
        time.sleep(600)
    except Exception as err:
        my_log(err)


# def write_old_data():
#     address = db_session.query(TagDetail).all()
#     for tag in address:
#         print(tag.Address)
#         data = redis_coon.hget(REDIS_TABLENAME, tag.Address)
#         if tag.Type == '电表' and data is not None and data != 'init':
#             redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old', data)
#             redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old_time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# write_old_data()