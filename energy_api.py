import json
import xlwt
from io import BytesIO
import pandas as pd
from datetime import datetime, timedelta
from flask import make_response, Blueprint, request
from sqlalchemy.exc import InvalidRequestError

from common.asd import db_session
from common.repair_model import Equipment
from tools.handle import MyEncoder
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable, ElectricEnergy, WaterEnergy


foo = Blueprint('foo', __name__)

electric = Blueprint('electric', __name__)


@electric.route('/Pie', methods=['GET'])
def get_pie():
    try:
        start_time = "'" + request.values.get('StartTime') + "'"
        end_time = "'" + request.values.get('EndTime') + "'"
        if request.values.get('energy_type') == '水':
            sql = f'select sum(IncremenValue) as value from IncrementWaterTable where CollectionDate between {start_time} and {end_time} '
            result = db_session.execute(sql).fetchall()
            value_data = 0 if result[0]['value'] is None else result[0]['value']
            data = [{'设备类型': '设备能耗', '能耗': value_data}]
            return json.dumps({'code': '200', 'mes': '查询成功', 'data': data}, ensure_ascii=False)
        if request.values.get('energy_type') == '电':
            sql1 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {start_time} and {end_time} and AreaName like "%照明%"'
            sql2 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {start_time} and {end_time} and AreaName like "%空調%"'
            result1 = db_session.execute(sql1).fetchall()
            result2 = db_session.execute(sql2).fetchall()
            light_data = 0 if result1[0]['value'] is None else result1[0]['value']
            kt_data = 0 if result2[0]['value'] is None else result2[0]['value']
            data = [{'设备类型': '照明设备', '能耗': light_data}, {'设备类型': '制冷设备', '能耗': kt_data}]
            return json.dumps({'code': '200', 'mes': '查询成功', 'data': data}, ensure_ascii=False)
        else:
            return json.dumps({'code': '200', 'mes': '查询成功', 'data': []}, ensure_ascii=False)
    except Exception as e:
        print(str(e))
        return json.dumps({'code': '200', 'mes': '查询失败', 'error': str(e)}, ensure_ascii=False)


@electric.route('/IndexEquipment', methods=['GET'])
def get_index_equipment():
    try:
        query_type_data = db_session.query(Equipment.EquipmentType).filter_by().all()
        query_floor_data = db_session.query(Equipment.Floor).filter_by().order_by(Equipment.Floor.asc()).all()
        equipment_type = list(set(i[0] for i in query_type_data))
        equipment_floor = list(set(i[0] for i in query_floor_data))
        data = []
        for item_floor in equipment_floor:
            result = {"楼层": item_floor}
            for item_type in equipment_type:
                query_result = db_session.query(Equipment).filter_by(Floor=item_floor, EquipmentType=item_type).all()
                result[item_type] = len(query_result)
            data.append(result)
        return json.dumps({'code': '200', 'mes': '查询成功', 'data': data}, ensure_ascii=False)
    except Exception as e:
        print(str(e))
        return json.dumps({'code': '200', 'mes': '查询失败', 'error': str(e)}, ensure_ascii=False)


@electric.route('/energy_contrast', methods=['GET'])
def energy_contrast():
    try:
        hours = ['00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00', '06:00:00', '07:00:00',
                 '08:00:00', '09:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00',
                 '16:00:00', '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00',
                 '24:00:00']
        # yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d ')
        yesterday = request.values.get('date')
        now = datetime.now().strftime('%Y-%m-%d ')
        now_hour = datetime.now().strftime('%H:00:00')
        rows = []
        for i in range(0, len(hours)):
            if hours[i] != '24:00:00':
                yesterday_start_time = '"' + yesterday + ' ' + hours[i] + '"'
                yesterday_end_time = '"' + yesterday + ' ' + hours[i+1] + '"'
                now_start_time = '"' + now + hours[i] + '"'
                now_end_time = '"' + now + hours[i+1] + '"'
                sql1 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {yesterday_start_time} and {yesterday_end_time}'
                result1 = db_session.execute(sql1).fetchall()
                yesterday_value = result1[0]['value'] if result1[0]['value'] is not None else 0
                if hours[i] <= now_hour:
                    sql2 = f'select sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {now_start_time} and {now_end_time}'
                    result2 = db_session.execute(sql2).fetchall()
                    today_value = result2[0]['value'] if result2[0]['value'] is not None else 0
                else:
                    today_value = ' '
                data = {'时间':  hours[i], '今日能耗': today_value, '对比日能耗': yesterday_value}
                rows.append(data)
        return json.dumps({'code': '200', 'mes': '查询成功', 'data': rows}, cls=MyEncoder, ensure_ascii=False)
    except Exception as e:
        print(str(e))
        return json.dumps({'code': '200', 'mes': '查询失败', 'error': str(e)}, ensure_ascii=False)


@electric.route('/energy', methods=['GET'])
def energys():
    try:
        energy_type = request.values.get('energy_type')
        start_time = '"' + request.values.get('start_time') + '"'
        end_time = '"' + request.values.get('end_time') + '"'
        # start_time = '"' + '2020-01-31 23:00:00' + '"'
        # end_time = '"' + '22020-10-31 23:00:00' + '"'
        data = []
        if energy_type == '电':
            sql = f'select AreaName,Address, sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between {start_time} and {end_time} group by Address'
            results = db_session.execute(sql).fetchall()
            db_session.close()
            # print(results)
            for result in results:
                value = '%.2f' % result[2] if result[2] is not None else '0.0'
                data.append({"AreaName": result[0], "Address": result[1], "Value": value, "StartTime": request.values.get('start_time'), "EndTime": request.values.get('end_time'), "Unit": "KW/h"})
        else:
            sql = f'select AreaName,Address, IncremenValue as value from IncrementWaterTable where CollectionDate between {start_time} and {end_time} order by CollectionDate desc limit 2'
            results = db_session.execute(sql).fetchall()
            db_session.close()
            # print(results)
            for result in results:
                value = '%.2f' % float(result[2]) if result[2] is not None else '0.0'
                data.append({"AreaName": result[0], "Address": result[1], "Value": value,
                             "StartTime": request.values.get('start_time'), "EndTime": request.values.get('end_time'), "Unit": "m³"})
            # data = [(result[0], result[1], '%.2f' % result[2], request.values.get('start_time'), request.values.get('end_time'), 'm³') for result in results]
        return json.dumps({'code': '200', 'mes': '查询成功', 'data': data}, ensure_ascii=False)
    # except InvalidRequestError:
    #     print('rollback()')
    #     db_session.rollback()
    #     return json.dumps({'code': '200', 'mes': '事务回滚'}, ensure_ascii=False)
    except Exception as e:
        # db_session.rollback()
        print(str(e))
        return json.dumps({'code': '200', 'mes': '查询失败', 'error': str(e)}, ensure_ascii=False)


@electric.route('/exports', methods=['GET'])
def excelout():
    '''
    导出原始数据
    :return:
    '''
    try:
        if request.method == 'GET':
            energy_type = request.values.get('energy_type')
            start_time = '"' + request.values.get('start_time') + '"'
            end_time = '"' + request.values.get('end_time') + '"'
            # start_time = '"' + '2020-01-31 23:00:00' + '"'
            # end_time = '"' + '22020-10-31 23:00:00' + '"'
            output = exportx(start_time, end_time, energy_type)
            resp = make_response(output.getvalue())
            resp.headers["Content-Disposition"] = "attachment; filename=energy.xlsx"
            resp.headers['Content-Type'] = 'application/x-xlsx'
            return resp
    except Exception as e:
        print(str(e))
        return json.dumps({'code': '200', 'mes': '查询失败', 'error': str(e)}, ensure_ascii=False)


def exportx(start_time, end_time, energy_type):
    try:
        # 创建数据流
        output = BytesIO()
        # 创建excel work book
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        workbook = writer.book
        # 创建excel sheet
        worksheet = workbook.add_worksheet('sheet1')
        # cell 样式
        cell_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'Blue'})
        col = 0
        columns = ['区域', '设备', '能耗值', '开始时间', '结束时间', '单位']
        for item in columns:
            worksheet.write(0, col, item, cell_format)
            col += 1
        sql = ''
        if energy_type == '电':
            sql = "select AreaName,Address, sum(IncremenValue) as value from IncrementElectricTable where CollectionDate between"+ start_time + " and " + end_time + " group by Address"
        if energy_type == '水':
            sql = "select AreaName,Address, IncremenValue as value from IncrementWaterTable where CollectionDate between" + start_time + " and " + end_time + " order by CollectionDate desc limit 2"
        all_data = db_session.execute(sql).fetchall()
        print(all_data)
        i = 1
        for ta in all_data:
            for cum in columns:
                if cum == '区域':
                    worksheet.write(i, columns.index(cum), ta[0])
                if cum == '设备':
                    worksheet.write(i, columns.index(cum), ta[1])
                if cum == '能耗值':
                    value = '%.2f' % float(ta[2]) if ta[2] is not None else '0.0'
                    worksheet.write(i, columns.index(cum), value)
                if cum == '单位' and energy_type == '电':
                    worksheet.write(i, columns.index(cum), 'KW/h')
                if cum == '单位' and energy_type == '水':
                    worksheet.write(i, columns.index(cum), 'm³')
                if cum == '开始时间':
                    worksheet.write(i, columns.index(cum), request.values.get('start_time'))
                if cum == '结束时间':
                    worksheet.write(i, columns.index(cum), request.values.get('end_time'))
            i += 1
        writer.close()
        output.seek(0)
        return output
    except Exception as e:
        print(str(e))
        return json.dumps({'code': '200', 'mes': '查询失败', 'error': str(e)}, ensure_ascii=False)

