import json
import xlwt
from io import BytesIO
import pandas as pd
from flask import make_response, Blueprint, request
from sqlalchemy.exc import InvalidRequestError

from common.asd import db_session
from tools.handle import MyEncoder
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable, ElectricEnergy, WaterEnergy


foo = Blueprint('foo', __name__)

electric = Blueprint('electric', __name__)


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
                data.append({"AreaName": result[0], "Address": result[1], "Value": value, "StartTime": request.values.get('start_time'), "EndTime": request.values.get('start_time'), "Unit": "KW/h"})
        else:
            sql = f'select AreaName,Address, sum(IncremenValue) as value from IncrementWaterTable where CollectionDate between {start_time} and {end_time} group by Address'
            results = db_session.execute(sql).fetchall()
            db_session.close()
            # print(results)
            for result in results:
                value = '%.2f' % result[2] if result[2] is not None else '0.0'
                data.append({"AreaName": result[0], "Address": result[1], "Value": value,
                             "StartTime": request.values.get('start_time'), "EndTime": request.values.get('start_time'), "Unit": "m³"})
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
            sql = "select AreaName,Address, sum(IncremenValue) as value from IncrementWaterTable where CollectionDate between" + start_time + " and " + end_time + " group by Address"
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
                    value = '%.2f' % ta[2] if ta[2] is not None else '0.0'
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
