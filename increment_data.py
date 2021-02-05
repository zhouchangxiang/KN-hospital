import time

import redis
from datetime import datetime, timedelta

# from database.db_operate import REDIS_PASSWORD, REDIS_HOST, REDIS_TABLENAME
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable, ElectricEnergy, WaterEnergy
from tools.handle import my_log

# redis_coon = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, decode_responses=True)
redis_coon = redis.Redis(host='127.0.0.1', password='liaicheng*521', decode_responses=True)
REDIS_TABLENAME = 'data_realtime'

while True:
    try:
        print('开始写入增量数据')
        old_date = redis_coon.hget(REDIS_TABLENAME, 'old_date')
        now_date = datetime.now().strftime('%Y-%m-%d')
        address = db_session.query(TagDetail).filter_by(Address='COM1.WATER9F.今日累积流量').all()
        # address = db_session.query(TagDetail).all()
        for tag in address:
            print(tag.Address)
            data = redis_coon.hget(REDIS_TABLENAME, tag.Address)
            if tag.Type == '电表' and data != 'None' and data != 'init':
                old_data = redis_coon.hget(REDIS_TABLENAME, tag.Address + '_old')
                if data == 'None' or old_data == 'None' or data is None or old_data is None:
                    pass
                else:
                    value = float(data) - float(old_data)
                    if value > 0.0:
                        db_session.add(
                            IncrementElectricTable(AreaName=tag.AreaName, IncremenValue=str(value), IncremenType='电',
                                                   CollectionDate=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                   Address=tag.Address, Unit='KW/h'))
                        db_session.commit()
                        redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old', data)
                        redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old_time',
                                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        pass
            elif tag.Type == '水表':
                old_data = redis_coon.hget(REDIS_TABLENAME, tag.Address + '_old')
                value = float(data) - float(old_data)
                if value > 0.0:
                    db_session.add(
                        IncrementWaterTable(AreaName=tag.AreaName, IncremenValue=str(value), IncremenType='水',
                                            CollectionDate=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                            Address=tag.Address, Unit='m³'))
                    db_session.commit()
                    redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old', data)
                    redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old_time',
                                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    pass
            else:
                old_date = (datetime.now() + timedelta(1)).strftime('%Y-%m-%d')
                redis_coon.hset(REDIS_TABLENAME, 'old_date', old_date)
                old_data = redis_coon.hset(REDIS_TABLENAME, tag.Address + '_old', '0.0')
        print('结束写入增量数据')
        time.sleep(600)
    except Exception as err:
        db_session.rollback()
        db_session.close()
        my_log(err)
