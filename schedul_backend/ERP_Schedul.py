from typing import Optional, Any
from collections import Counter
import time
import xlrd
import xlwt
from flask import Blueprint, render_template, send_from_directory
from openpyxl.compat import file
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy import create_engine, func
from flask import render_template, request, make_response
import json
import socket
import datetime
from flask_login import login_required, logout_user, login_user,current_user,LoginManager
import re
from sqlalchemy import create_engine, Column, ForeignKey, Table, Integer, String, and_, or_, desc,extract
from io import StringIO
import calendar

import schedul_backend
from common import Global
from common.BSFramwork import AlchemyEncoder
from common.MESLogger import insertAuditTrace
from common.common_cuid import logger,insertSyslog,insert,delete,update,select
import os
import openpyxl
import suds
from suds.client import Client
from datetime import timedelta

from common.batch_plan_model import ProductUnit, ProductRule, PlanManager, ZYPlan, ZYTask, TaskNoGenerator, \
    ZYPlanWMS, Material, MaterialBOM, ProductEquipment, ProcessUnit, ProductLine
from common.schedul_model import Scheduling, plantCalendarScheduling, SchedulingStandard, \
    scheduledate, product_plan, SchedulingStock, EquipmentBatchRunTime
from common.system import Shifts
from database.connect_db import CONNECT_DATABASE
from enum import Enum, IntEnum, unique

login_manager = LoginManager()
# 创建对象的基类
engine = create_engine(CONNECT_DATABASE)
Session = sessionmaker(bind=engine)
db_session = Session()

erp_schedul = Blueprint('erp_schedul', __name__)

class SchedulingStatus(Enum):
    Locl = "1" #排产表批次已经生产则为锁定状态
    Unlock = "0" #批次还未生产

@erp_schedul.route('/addscheduledates', methods=['GET', 'POST'])
def addscheduledates():
    '''
    添加工作日休息日
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            month = data['month']
            count = db_session.query(scheduledate).filter(scheduledate.WorkDate.like("%"+month+"%")).count()
            if count < 20:
                mou = month.split("-")
                monthRange = calendar.monthrange(int(mou[0]), int(mou[1]))
                re = timeChange(mou[0], str(int(mou[1])), monthRange[1])
                lis = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', ]
                dic = dict(enumerate(lis))
                for i in re:
                    ymr = i.split("-")
                    w = datetime.date(int(ymr[0]), int(ymr[1]), int(ymr[2]))
                    xq = dic[w.weekday()]
                    if xq == "星期六" or xq == "星期日":
                        # dc = db_session.query(scheduleDateType).filter(scheduleDateType.DateTypeName == "周末").first()
                        DateType = "周末"
                        color = "#FA7D00"
                    else:
                        DateType = "工作日"
                        color = "#00CAFA"
                    sc = scheduledate()
                    sc.WorkDate = i
                    sc.DateType = DateType
                    sc.comment = xq
                    sc.color = color
                    db_session.add(sc)
                    db_session.commit()
                db_session.close_all()
            return 'OK'
        except Exception as e:
            db_session.rollback()
            logger.error(e)
            insertSyslog("error", "添加工作日休息日报错Error：" + str(e), current_user.Name)
            return json.dumps("添加工作日休息日报错", cls=AlchemyEncoder, ensure_ascii=False)

@erp_schedul.route('/batchequimentselect', methods=['GET', 'POST'])
def batchequimentselect():
    '''
    查询批次下对应的设备
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            BatchID = data.get('BatchID')
            BrandCode = data.get('BrandCode')
            oclass = db_session.query(PlanManager).filter(PlanManager.BatchID == BatchID, PlanManager.BrandCode == BrandCode).first()
            dir = {}
            if oclass:
                pres = db_session.query(ProductUnit).filter(ProductUnit.BrandCode == oclass.BrandCode).all()
                dir_list = []
                for pre in pres:
                    dir_list_i = {}
                    dir_list_i["PUName"] = pre.PUName
                    dir_list_i["PUCode"] = pre.PUCode
                    dir_list_i["Seq"] = pre.Seq
                    puoclass = db_session.query(ProcessUnit).filter(ProcessUnit.PUCode == pre.PUCode).first()
                    dir_list_i["RelateTaskCount"] = puoclass.RelateTaskCount
                    eqList = []
                    eqps = db_session.query(ProductEquipment).filter(ProductEquipment.PUCode == pre.PUCode).all()
                    for eqp in eqps:
                        eqp_dir = {}
                        eqp_dir["EQPCode"] = eqp.EQPCode
                        eqp_dir["EQPName"] = eqp.EQPName
                        eqp_dir["EQPStatus"] = eqp.EQPStatus
                        runeqp = db_session.query(EquipmentBatchRunTime).filter(
                            EquipmentBatchRunTime.EQPCode == eqp.EQPCode,
                            EquipmentBatchRunTime.BrandCode == oclass.BrandCode,
                            EquipmentBatchRunTime.BatchID == oclass.BatchID, EquipmentBatchRunTime.PUCode == pre.PUCode).first()
                        eqp_dir["isSelected"] = False
                        if runeqp:#如果被选中过True，没被选中就是False
                            eqp_dir["isSelected"] = True
                            eqp_dir["StartTime"] = runeqp.StartTime[0:10]
                            eqp_dir["EndTime"] = runeqp.EndTime[0:10]
                            eqp_dir["StartBC"] = runeqp.StartBC
                            eqp_dir["EndBC"] = runeqp.EndBC
                        else:
                            eqp_dir["StartTime"] = ""
                            eqp_dir["EndTime"] = ""
                            eqp_dir["StartBC"] = ""
                            eqp_dir["EndBC"] = ""
                        eqList.append(eqp_dir)
                    dir_list_i["eqList"] = eqList
                    dir_list.append(dir_list_i)
                dir["processList"] = dir_list
            return json.dumps({"code": "200", "message": "查询成功！", "data": dir})
        except Exception as e:
            db_session.rollback()
            logger.error(e)
            insertSyslog("error", "查询批次下对应的设备报错Error：" + str(e), current_user.Name)
            return json.dumps("查询批次下对应的设备报错", cls=AlchemyEncoder, ensure_ascii=False)

@erp_schedul.route('/batchconflictequimentselect', methods=['GET', 'POST'])
def batchconflictequimentselect():
    '''
    查询选择时间段下对应的冲突设备的批次品名
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            EQPCode = data.get('EQPCode')
            DateTime = data.get('DateTime')
            BCType = data.get('BCType')
            PlanNum = data.get('PlanNum')
            BatchID = data.get('BatchID')
            BrandCode = data.get('BrandCode')
            sft = db_session.query(Shifts).filter(Shifts.ShiftsName == BCType).first()
            if sft:
                beginoclass = db_session.query(EquipmentBatchRunTime).filter(
                    EquipmentBatchRunTime.EQPCode == EQPCode,
                    EquipmentBatchRunTime.StartTime.between(str(DateTime +" "+ sft.BeginTime),str(DateTime +" " + sft.EndTime))).all()
                endoclass = db_session.query(EquipmentBatchRunTime).filter(
                    EquipmentBatchRunTime.EQPCode == EQPCode,
                    EquipmentBatchRunTime.EndTime.between(str(DateTime +" "+ sft.BeginTime),str(DateTime +" " + sft.EndTime))).all()
                dict_list = []
                for i in beginoclass:
                    if i.BatchID == BatchID and i.BrandCode == BrandCode:
                        continue#跳出当前循环
                    dict_list.append(i)
                for j in endoclass:
                    if j.BatchID == BatchID and j.BrandCode == BrandCode:
                        continue
                    if j not in dict_list:
                        dict_list.append(j)
            return json.dumps({"code": "200", "message": "查询成功！", "data": dict_list}, cls=AlchemyEncoder, ensure_ascii=False)
        except Exception as e:
            db_session.rollback()
            logger.error(e)
            insertSyslog("error", "查询选择时间段下对应的冲突设备的批次品名报错Error：" + str(e), current_user.Name)
            return json.dumps("查询选择时间段下对应的冲突设备的批次品名报错", cls=AlchemyEncoder, ensure_ascii=False)

import ast
import math
@erp_schedul.route('/planschedul', methods=['GET', 'POST'])
def planschedul():
    '''
    计划排产
    :return:
    '''
    if request.method == 'POST':
        data = request.values
        try:
            data_list = json.loads(data.get('selectPlanList'))
            for i in data_list:
                dir = {}
                proclass = db_session.query(ProductRule).filter(
                    ProductRule.BrandCode == i.get("BrandCode")).first()
                for BatchNo in range(0,int(i.get("BatchNum"))):
                    pm = PlanManager()
                    pm.PlanNum = i.get("PlanNum")
                    pm.SchedulePlanCode = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[0:10]
                    # nowtime = datetime.datetime.now().strftime("%Y-%m %M:%S").replace(":","").replace("-","").replace(" ","")
                    pm.BatchID = ""
                    pm.Seq = BatchNo
                    pm.PlanQuantity = proclass.BatchWeight
                    pm.Unit = proclass.Unit
                    pm.BrandCode = i.get("BrandCode")
                    pm.BrandName = i.get("BrandName")
                    # #计算计划开始时间结束时间
                    # pu = db_session.query(ProductUnit).filter(ProductUnit.BrandCode == oclass.BrandCode, ProductUnit.PUName.like("%提%")).first()
                    # proc = db_session.query(ProcessUnit).filter(ProcessUnit.PUCode == pu.PUCode).first()
                    # beg = int(proclass.BatchTimeLength)*BatchNo
                    # end = beg + int(proclass.BatchTimeLength)
                    # PlanBeginTime = (datetime.datetime.strptime(StartTime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=beg)).strftime("%Y-%m-%d %H:%M:%S")
                    # PlanEndTime = (datetime.datetime.strptime(StartTime,
                    #                                             "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
                    #     hours=end)).strftime("%Y-%m-%d %H:%M:%S")
                    # pm.PlanBeginTime = PlanBeginTime
                    # pm.PlanEndTime = PlanEndTime
                    pm.BrandType = proclass.BrandType
                    pm.PlanStatus = Global.PlanStatus.Confirm.value
                    db_session.add(pm)
                    db_session.commit()
                PlanNums = i.get("PlanNum").split(",")
                for pn in PlanNums:
                    oc = db_session.query(product_plan).filter(product_plan.PlanNum == pn).first()
                    if oc:
                        oc.PlanStatus = "已分批"
                        db_session.commit()
                    insertAuditTrace("订单排产", "订单号是：" + oc.PlanNum + "的" + oc.BrandName + "在" +
                                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "进行订单排产操作", "PlanManager",
                                     current_user.Name, "")
            return json.dumps({"code": "200", "message": "排产成功！", "data": "OK"})
        except Exception as e:
            db_session.rollback()
            print(e)
            logger.error(e)
            insertSyslog("error", "计划排产报错Error：" + str(e), current_user.Name)
            return json.dumps("计划排产报错", cls=AlchemyEncoder, ensure_ascii=False)

import ast
@erp_schedul.route('/addEquipmentBatchRunTime', methods=['GET', 'POST'])
def addEquipmentBatchRunTime():
    '''
    生产配置添加设备
    :return:
    '''
    if request.method == 'POST':
        data = request.values
        try:
            ID = data.get('ID')
            processList = json.loads(data.get('processList'))
            oclass = db_session.query(PlanManager).filter(PlanManager.ID == ID).first()
            #清空之前保存的数据
            delete_list = db_session.query(EquipmentBatchRunTime).filter(EquipmentBatchRunTime.BrandCode ==
                                                           oclass.BrandCode, EquipmentBatchRunTime.BatchID == oclass.BatchID).all()
            for i in delete_list:
                db_session.delete(i)
                db_session.commit()
            dir = {}
            if oclass:
                for pl in processList:
                    PUName = pl.get("PUName")
                    PUCode = pl.get("PUCode")
                    eqList = pl.get('eqList')
                    for el in eqList:
                        isSelected = el.get("isSelected")
                        if isSelected == True:#选中过的设备
                            ert = EquipmentBatchRunTime()
                            ert.BatchID = oclass.BatchID
                            ert.BrandCode = oclass.BrandCode
                            ert.BrandName = oclass.BrandName
                            ert.EQPCode = el.get("EQPCode")
                            ert.EQPName = el.get("EQPName")
                            ert.PUCode = PUCode
                            ert.PUName = PUName
                            ert.StartBC = el.get("StartBC")
                            ert.EndBC = el.get("EndBC")
                            sft = db_session.query(Shifts).filter(Shifts.ShiftsName == ert.StartBC).first()
                            ert.StartTime = str(el.get("StartTime")) + " " + sft.BeginTime
                            eft = db_session.query(Shifts).filter(Shifts.ShiftsName == ert.EndBC).first()
                            if eft.ShiftsName == "中" or eft.ShiftsName == "晚":
                                endt = (datetime.datetime.strptime(el.get("EndTime"), "%Y-%m-%d") + datetime.timedelta(hours=24)).strftime("%Y-%m-%d")
                            else:
                                endt = el.get("EndTime")
                            ert.EndTime = str(endt) + " " + eft.EndTime
                            db_session.add(ert)
                oclass.PlanStatus = Global.PlanStatus.WaitRealse.value
                db_session.commit()
                insertAuditTrace("生产配置添加设备", "批次号是：" + oclass.BatchID + "的" + oclass.BrandName + "在" +
                                 datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "进行生产配置添加设备操作", "PlanManager",
                                 current_user.Name, "")
            return json.dumps({"code": "200", "message": "保存成功！", "data": "OK"})
        except Exception as e:
            db_session.rollback()
            print(e)
            logger.error(e)
            insertSyslog("error", "生产配置添加设备报错Error：" + str(e), current_user.Name)
            return json.dumps("生产配置添加设备报错", cls=AlchemyEncoder, ensure_ascii=False)

@erp_schedul.route('/selectpaichanrule', methods=['GET', 'POST'])
def selectpaichanrule():
    '''
    查询排产规则
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            data_list = json.loads(data.get('selectPlanList'))
            redata_list = []
            for i in data_list:
                dir = {}
                flag = 0
                proclass = db_session.query(ProductRule).filter(ProductRule.BrandCode == i.get("BrandCode")).first()
                for j in redata_list:
                    if j.get("BrandCode") == i.get("BrandCode"):
                        flag = 1
                        j["BatchNum"] = math.ceil((float(i.get("PlanQuantity")) + float(j.get("PlanQuantityTotal")))/float(proclass.BatchWeight))
                        j["PlanQuantityTotal"] = float(i.get("PlanQuantity")) + float(j.get("PlanQuantityTotal"))
                        j["orderNum"] = int(j.get("orderNum"))+1
                        j["PlanNum"] = i.get("PlanNum")+","+j.get("PlanNum")
                if flag == 0:
                    dir["BatchNum"] = math.ceil(float(i.get("PlanQuantity"))/float(proclass.BatchWeight))
                    dir["PlanQuantityTotal"] = i.get("PlanQuantity")
                    dir["BatchWeight"] = proclass.BatchWeight
                    dir["BrandName"] = i.get("BrandName")
                    dir["BrandCode"] = i.get("BrandCode")
                    dir["PlanNum"] = i.get("PlanNum")
                    dir["unit"] = proclass.Unit
                    dir["orderNum"] = 1
                    redata_list.append(dir)
            return json.dumps({"code": "200", "message": "查询成功！", "data": redata_list})
        except Exception as e:
            db_session.rollback()
            print(e)
            logger.error(e)
            insertSyslog("error", "查询排产规则报错Error：" + str(e), current_user.Name)
            return json.dumps("查询排产规则报错", cls=AlchemyEncoder, ensure_ascii=False)

from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
metadata = MetaData()
from sqlalchemy import Table
Base = automap_base()
Base.prepare(engine, reflect=True)
@erp_schedul.route('/selectplanmanager', methods=['GET', 'POST'])
def selectplanmanager():
    '''
    查询排产好的计划
    :return:
    '''
    if request.method == 'GET':
        data = request.values
        try:
            PlanNums = json.loads(data.get('PlanNums'))
            tableName = "PlanManager"
            pages = data.get("offset")
            pages = int(data.get("offset")) + 1
            rowsnumber = int(data.get("limit"))
            newTable = Table(tableName, metadata, autoload=True, autoload_with=engine)
            columns = ""
            for column in newTable.columns:
                if columns == "":
                    columns = "[" + str(column).split(".")[1] + "]"
                else:
                    columns = columns + ",[" + str(column).split(".")[1] + "]"
            params = ""
            for key in PlanNums:
                if params == "":
                    params = "PlanNum like '%" +key + "%'"
                else:
                    params = params + " OR PlanNum like '%" + key + "%'"
            sql = "select top " + str(
                rowsnumber) + " " + columns + " from [LIMS].[dbo].[" + tableName + "] where (" + params + \
                  ") AND ID not in (select top " + str(
                (
                            pages - 1) * rowsnumber) + " ID FROM [LIMS].[dbo].[" + tableName + "] where " + params +" ORDER BY ID DESC) ORDER BY ID DESC"
            sqlcount = "select count(ID) from [LIMS].[dbo].[" + tableName + "] where " + params
            re = db_session.execute(sql).fetchall()
            recount = db_session.execute(sqlcount).fetchall()
            dict_list = []
            for i in re:
                dir = {}
                column_list = columns.split(",")
                for col in column_list:
                    dir[col[1:-1]] = i[col[1:-1]]
                dict_list.append(dir)
            return json.dumps({"code": "200", "message": "查询成功！", "data": {"total": recount[0][0], "rows": dict_list}})
        except Exception as e:
            db_session.rollback()
            print(e)
            logger.error(e)
            insertSyslog("error", "查询排产好的计划报错Error：" + str(e), current_user.Name)
            return json.dumps("查询排产好的计划报错", cls=AlchemyEncoder, ensure_ascii=False)