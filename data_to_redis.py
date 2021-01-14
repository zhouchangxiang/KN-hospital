import json
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


def count_energy(tags, start_time, end_time):
    result = 0.0
    for tag in tags:
        sql = f'select sum(IncremenValue) as value from IncrementElectricTable where Address="{tag}" and CollectionDate between {start_time} and {end_time} '
        data = db_session.execute(sql).fetchall()
        if data[0]['value'] is not None:
            result += float(data[0]['value'])
        else:
            result += 0.0
    return result


def count_floor_energy(tags, start_time, end_time, water_day_total, total_energy):
    try:
        total = 0.0
        i = 0
        floorData = []
        print('total_energy_2: ', total_energy)
        for tag in tags:
            i += 1
            floor_total_energy = 0.0
            AreaName = f'厚德楼{i}楼'
            for item in tag:
                print('采集点: ', item)
                sql = f'select sum(IncremenValue) as value from IncrementElectricTable where Address="{item}" and CollectionDate between {start_time} and {end_time} '
                data = db_session.execute(sql).fetchall()
                if data[0]['value'] is not None:
                    floor_total_energy += float(data[0]['value'])
                    total += floor_total_energy
                else:
                    floor_total_energy += 0.0
                    total += 0.0
            ratio = '%.2f' % (floor_total_energy / total_energy * 100)
            if i == 7 or i == 8:
                floorData.append({'areaName': AreaName, 'electricity': floor_total_energy, 'water': water_day_total, 'ratio': ratio})
            else:
                floorData.append({'areaName': AreaName, 'electricity': floor_total_energy, 'water': 0.0, 'ratio': ratio})
        return floorData
    except Exception as e:
        print('错误信息：', str(e))
        return []

while True:
    # 电
    print('开始计算每日预估能耗')
    now = date.today()
    this_month_start = "'" + datetime(now.year, now.month, 1).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    this_month_end = "'" + datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]).strftime(
        '%Y-%m-%d') + " 23:59:59" + "'"
    this_year_start = "'" + datetime(now.year, 1, 1).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    this_year_end = "'" + datetime(now.year, 12, 31).strftime('%Y-%m-%d') + " 23:59:59" + "'"
    yesterday_start_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    yesterday_last_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d') + " 23:59:59" + "'"
    yesterday_end_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d ') + datetime.now().strftime(
        '%H:%M:%S') + "'"
    today_start_time = "'" + date.today().strftime('%Y-%m-%d') + " 00:00:00" + "'"
    today_end_time = "'" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "'"

    now_year = date.today().strftime('%Y')
    now_month = date.today().strftime('%m')
    now_day = date.today().strftime('%d')
    year_day_data = get_day_of_year(now_year, int(now_month), int(now_day))

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
    today_energy = 1 if result1[0]['value'] is None else result1[0]['value']
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
    water_year_total = float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今年累积流量')) + float(
        redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER9F.今年累积流量'))
    # 今月累积流量
    water_month_total = float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今月累积流量')) + float(
        redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER9F.今月累积流量'))
    # 今日累积流量
    water_day_total = float(redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今日累积流量')) + float(
        redis_coon.hget(REDIS_TABLENAME, 'COM1.WATER8F.今日累积流量'))
    # 日均用水量
    water_avg_day = water_year_total / float(year_day_data)
    # 月均用水量
    water_avg_month = water_year_total / float(now_month)
    redis_coon.hset(REDIS_TABLENAME, 'water_year_total', water_year_total)
    redis_coon.hset(REDIS_TABLENAME, 'water_month_total', water_month_total)
    redis_coon.hset(REDIS_TABLENAME, 'water_day_total', water_day_total)
    redis_coon.hset(REDIS_TABLENAME, 'water_avg_day', water_avg_day)
    redis_coon.hset(REDIS_TABLENAME, 'water_avg_month', water_avg_month)

    # 单位建筑面积电耗 年用电量*0.1229 / 20224.4
    d1 = '%.2f' % (float(result4[0]['value']) * 0.1229 / 20224.4)
    # 单位建筑面积水耗 8、9楼年用水量 / 2140
    d2 = '%.2f' % (water_year_total / 2140)
    # 单位建筑面积能耗 (年用电量*0.1229 + 8、9楼年用水量*0.000257) / 20224.4
    d3 = '%.2f' % ((float(result4[0]['value']) * 0.1229 + water_year_total * 0.000257) / 20224.4)
    # 单位面积空调能耗 电表13-27年总用电量 * 0.1229 / 13000
    tags1 = ['COM2.KT1F.总有功电量', 'COM2.KT2F.总有功电量', 'COM2.KT3F.总有功电量', 'COM2.KT4F.总有功电量', 'COM2.KT5F.总有功电量',
             'COM2.KT6F.总有功电量', 'COM2.KT7F.总有功电量', 'COM2.KT8F.总有功电量', 'COM2.KT9F.总有功电量', 'COM2.KT10F.总有功电量',
             'COM2.KT11F.总有功电量', 'COM2.KT12F.总有功电量', 'COM2.KT5F.总有功电量', 'COM2.KTCTR1.总有功电量', 'COM2.KTCTR2.总有功电量',
             'COM2.KTCTRADD.总有功电量']
    result_tags1 = count_energy(tags1, this_year_start, this_year_end)
    d4 = '%.2f' % (result_tags1 * 0.1229 / 13000)
    # 单位床位能耗 (年用电量*0.1229 + 8、9楼年用水量*0.000257) / 1330
    d5 = '%.2f' % ((float(result4[0]['value']) * 0.1229 + water_year_total * 0.000257) / 630)
    # 人均综合能耗 （8、9楼年用电量 *0.1229 + 8、9楼年用水量*0.000257）/ 210
    tags2 = ['COM2.KT8F.总有功电量', 'COM2.LIGHT8F.总有功电量', 'COM2.LIGHT9F.总有功电量', 'COM2.KT9F.总有功电量']
    result_tags2 = count_energy(tags2, this_year_start, this_year_end)
    d6 = '%.2f' % ((result_tags2 * 0.1229 + water_year_total * 0.000257) / 210)
    # 人均电耗 8、9楼年用电量*0.1229 / 210
    d7 = '%.2f' % (result_tags2 * 0.1229 / 120)
    # 人均水耗 8、9楼年用水量 / 210
    d8 = '%.2f' % (water_year_total / 210)
    data = [{'Desc': "单位建筑面积电耗", 'beforeValue': '0.59', 'companyValue': d1},
            {'Desc': "单位建筑面积水耗", 'beforeValue': '1.04', 'companyValue': d2},
            {'Desc': "单位建筑面积天然气耗", 'beforeValue': '0.0', 'companyValue': '0.0'},
            {'Desc': "单位建筑面积能耗", 'beforeValue': '0.59', 'companyValue': d3},
            {'Desc': "单位面积空调能耗", 'beforeValue': '6.38', 'companyValue': d4},
            {'Desc': "单位床位能耗", 'beforeValue': '25.53', 'companyValue': d5},
            {'Desc': "人均综合能耗", 'beforeValue': '4.99', 'companyValue': d6},
            {'Desc': "人均电耗", 'beforeValue': '40.59', 'companyValue': d7},
            {'Desc': "人均水耗", 'beforeValue': '10.59', 'companyValue': d8},
            ]
    json_data = json.dumps(data, ensure_ascii=False)
    redis_coon.hset(REDIS_TABLENAME, 'indicator', json_data)
    # 楼层实时用能数据
    L_tags = [['COM2.KT1F.总有功电量', 'COM2.LIGHT1F.总有功电量'], ['COM2.KT2F.总有功电量', 'COM2.LIGHT2F.总有功电量'],
              ['COM2.KT3F.总有功电量', 'COM2.LIGHT3F.总有功电量'], ['COM2.KT4F.总有功电量', 'COM2.LIGHT4F.总有功电量'],
              ['COM2.KT5F.总有功电量', 'COM2.LIGHT5F.总有功电量'], ['COM2.KT6F.总有功电量', 'COM2.LIGHT6F.总有功电量'],
              ['COM2.KT7F.总有功电量', 'COM2.LIGHT7F.总有功电量'], ['COM2.KT8F.总有功电量', 'COM2.LIGHT8F.总有功电量'],
              ['COM2.KT9F.总有功电量', 'COM2.LIGHT9F.总有功电量'], ['COM2.KT10F.总有功电量', 'COM2.LIGHT10F.总有功电量'],
              ['COM2.KT11F.总有功电量', 'COM2.LIGHT11F.总有功电量'], ['COM2.KT12F.总有功电量', 'COM2.LIGHT12F.总有功电量']]
    print('today_energy: ', today_energy)
    floor_data = count_floor_energy(L_tags, today_start_time, today_end_time, water_day_total, today_energy)
    data = json.dumps(floor_data, ensure_ascii=False)
    redis_coon.hset(REDIS_TABLENAME, 'floorData', data)
    print('结束计算能耗数据')
    time.sleep(180)
