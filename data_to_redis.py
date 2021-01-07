import time
import calendar
import redis
from datetime import datetime, date, timedelta

from database.constant import REDIS_PASSWORD, REDIS_HOST, REDIS_TABLENAME
from common.asd import db_session

redis_coon = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, decode_responses=True)

month_of_days31 = [1, 3, 5, 7, 8, 10, 12]
month_of_days30 = [4, 6, 9, 11]
feb_month = 2


def is_leap_year(year):
    """
    判断当前年份是不是闰年，年份公元后，且不是过大年份
    :param year: 年份
    :return: True 闰年， False 平年
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def get_day_of_year(year, month, day):
    """
    获取一个日期在这一年中的第几天
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :return: 在这一年中的第几天
    """
    if month == 1:
        return day

    if month == 2:
        return day + 31

    days_of_31_num = 0
    days_of_30_num = 0
    # 31天月份数
    for days_of_31 in month_of_days31:
        if days_of_31 < month:
            days_of_31_num += 1
        else:
            break

    # 30天月份数
    for days_of_30 in month_of_days30:
        if days_of_30 < month:
            days_of_30_num += 1
        else:
            break
    return days_of_31_num * 31 + days_of_30_num * 30 + (29 if is_leap_year(year) else 28) + day


while True:
    # 电
    print('开始计算每日预估能耗')
    now = date.today()
    this_month_start = datetime(now.year, now.month, 1).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    this_month_end = datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]).strftime('%Y-%m-%d') + " 23:59:59" + "'"
    this_year_start = datetime(now.year, 1, 1).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    this_year_end = datetime(now.year, 12, 1).strftime('%Y-%m-%d') + " 23:59:59" + "'"
    yesterday_start_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    yesterday_last_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d') + " 23:59:59" + "'"
    yesterday_end_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d ') + datetime.now().strftime('%H:%M:%S') + "'"
    today_start_time = "'" + date.today().strftime('%Y-%m-%d') + " 00:00:00" + "'"
    today_end_time = "'" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'"

    now_year = date.today().strftime('%Y')
    now_month = date.today().strftime('%m')
    now_day = date.today().strftime('%d')
    year_day_data = get_day_of_year(now_year, now_month, now_day)

    # 今日用电总量
    sql1 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {today_start_time} and {today_end_time} '
    # 昨日同等小时能耗
    sql2 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {yesterday_start_time} and {yesterday_end_time} '
    # 昨日总能耗
    sql3 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {yesterday_start_time} and {yesterday_last_time} '
    # 今年用电总量
    sql4 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {this_year_start} and {this_year_end} '
    # 本月用电总量
    sql5 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {this_month_start} and {this_month_end} '
    result1 = db_session.execute(sql1).fetchall()
    result2 = db_session.execute(sql2).fetchall()
    result3 = db_session.execute(sql3).fetchall()
    result4 = db_session.execute(sql4).fetchall()
    result5 = db_session.execute(sql5).fetchall()
    if result1[0]['value'] is not None:
        print(result1[0]['value'])
        redis_coon.hset(REDIS_TABLENAME, 'today_energy', result1[0]['value'])
    if result2[0]['value'] is not None:
        print(result2[0]['value'])
        redis_coon.hset(REDIS_TABLENAME, 'yesterday_energy', result2[0]['value'])
    if result3[0]['value'] is not None:
        print(result3[0]['value'])
        redis_coon.hset(REDIS_TABLENAME, 'yesterday_total_energy', result3[0]['value'])
    if result4[0]['value'] is not None:
        print(result4[0]['value'])
        # 今年日均
        year_avg_day = float(result4[0]['value']) / float(year_day_data)
        # 今年月均
        year_avg_month = float(result4[0]['value']) / float(now_month)
        redis_coon.hset(REDIS_TABLENAME, 'year_avg_day', result4[0]['value'])
        redis_coon.hset(REDIS_TABLENAME, 'year_avg_month', result4[0]['value'])
        redis_coon.hset(REDIS_TABLENAME, 'year_total_energy', result4[0]['value'])
    if result5[0]['value'] is not None:
        print(result5[0]['value'])
        redis_coon.hset(REDIS_TABLENAME, 'month_total_energy', result5[0]['value'])

    # 水
    # 今年累积流量
    water_year_total = float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今年累积流量')) + float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER9F.今年累积流量'))
    # 今月累积流量
    water_month_total = float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今月累积流量')) + float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER9F.今月累积流量'))
    # 今日累积流量
    water_day_total = float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今日累积流量')) + float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今日累积流量'))
    # 日均用水量
    water_avg_day = water_year_total / float(year_day_data)
    # 月均用水量
    water_avg_month = water_year_total / float(now_month)
    redis_coon.hset(REDIS_TABLENAME, 'water_year_total', water_year_total)
    redis_coon.hset(REDIS_TABLENAME, 'water_month_total', water_month_total)
    redis_coon.hset(REDIS_TABLENAME, 'water_day_total', water_day_total)
    redis_coon.hset(REDIS_TABLENAME, 'water_avg_day', water_avg_day)
    redis_coon.hset(REDIS_TABLENAME, 'water_avg_month', water_avg_month)
    print('结束计算能耗数据')
    time.sleep(180)
