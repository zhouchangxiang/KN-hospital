import json

from flask import Blueprint

from common.energy_model import CheckForm, db_session
from tools.handle import MyEncoder

energy = Blueprint('energy', __name__)


@energy.route('/index', methods=['GET'])
def index():
    data = db_session.query(CheckForm).filter_by().all()
    return json.dumps({'data': data}, cls=MyEncoder, ensure_ascii=False)