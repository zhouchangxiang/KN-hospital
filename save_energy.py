import time

import redis
from datetime import datetime, date, timedelta

# from database.db_operate import REDIS_PASSWORD, REDIS_HOST, REDIS_TABLENAME
from common.asd import db_session

# redis_coon = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, decode_responses=True)
redis_coon = redis.Redis(host='127.0.0.1', password='liaicheng*521', decode_responses=True)
REDIS_TABLENAME = 'data_realtime'

while True:
    # 计算每日预估能耗nage
    print('开始计算每日预估能耗')
    start_time = '"' + (date.today() - timedelta(7)).strftime('%Y-%m-%d') + " 00:00:00" + '"'
    last_time = '"' + (date.today()).strftime('%Y-%m-%d') + " 23:59:59" + '"'
    # end_time = "'" + (date.today()).strftime('%Y-%m-%d ') + datetime.now().strftime('%H:%M:%S') + "'"
    # start_time = "'" + date.today().strftime('%Y-%m-%d') + " 00:00:00" + "'"
    # today_end_time = "'" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'"
    # 今日运行小时能耗
    sql1 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {start_time} and {last_time} '
    # # 昨日同等小时能耗
    # sql2 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {yesterday_start_time} and {yesterday_end_time} '
    # # 昨日总能耗
    # sql3 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {yesterday_start_time} and {yesterday_last_time} '
    result1 = db_session.execute(sql1).fetchall()
    # result2 = db_session.execute(sql2).fetchall()
    # result3 = db_session.execute(sql3).fetchall()
    save_energy = redis_coon.hget(REDIS_TABLENAME, 'save_energy')
    if result1[0]['value'] is not None:
        print(result1[0]['value'])
        data = float(132900) - float('%.2f' % result1[0]['value'])
        value = float(save_energy) + float(data)
        redis_coon.hset(REDIS_TABLENAME, 'save_energy', data)
        redis_coon.hset(REDIS_TABLENAME, 'save_energy_time', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # if result2[0]['value'] is not None:
    #     print(result2[0]['value'])
    #     redis_coon.hset(REDIS_TABLENAME, 'yesterday_energy', result2[0]['value'])
    # if result3[0]['value'] is not None:
    #     print(result3[0]['value'])
    #     redis_coon.hset(REDIS_TABLENAME, 'yesterday_total_energy', result3[0]['value'])from
        print(value)
    time.sleep(604800)
