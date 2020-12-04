import time

import redis
from datetime import datetime, date, timedelta

from database.constant import REDIS_PASSWORD, REDIS_HOST, REDIS_TABLENAME
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable, ElectricEnergy, WaterEnergy

redis_coon = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, decode_responses=True)


while True:
    start_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d') + " 00:00:00" + "'"
    end_time = "'" + (date.today() - timedelta(1)).strftime('%Y-%m-%d') + " 23:59:59" + "'"
    now_energy_sql = ''
    pass