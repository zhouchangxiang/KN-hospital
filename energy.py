import json
from flask import Blueprint
import redis
from datetime import datetime

from database.constant import REDIS_PASSWORD, REDIS_HOST, REDIS_TABLENAME
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable, ElectricEnergy, WaterEnergy
from tools.handle import MyEncoder

energy = Blueprint('energy', __name__)

redis_coon = redis.Redis(host=REDIS_HOST, password=REDIS_PASSWORD, decode_responses=True)


@energy.route('/history', methods=['GET'])
def index():
    address = db_session.query(TagDetail).all()
    result = {}
    for tag in address:
        data = redis_coon.hget(REDIS_TABLENAME, tag.Address)

        if tag.Type == '电表' and data is not None:
            result[tag.Address] = data
        # elif tag.Type == '水表' and data is not None:
        #     db_session.add(
        #         WaterEnergy(WaterSum=str(data), AreaName=tag.AreaName, CollectionDate=datetime.now(),
        #                     Address=tag.Address))
        #     db_session.commit()
        #     # db_session.close()
        else:
            pass

    return json.dumps({'data': result}, cls=MyEncoder, ensure_ascii=False)