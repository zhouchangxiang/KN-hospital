import xlrd
import pymysql
from datetime import datetime
from xlrd import xldate_as_tuple

# 打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("202001101康宁医院罗湖院区用能表(1).xls")
sheet = book.sheet_by_name("Sheet1")
# 建立一个MySQL连接
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Hstl_2020',
    db='hstl',
    port=3306,
    charset='utf8'
)
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
query = 'insert into Equipment (EquipmentNo,EquipmentCode,EquipmentType,EquipmentName,Area,AddTime,Status) values (%s, %s, %s, %s, %s, %s,%s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行,
i = sheet.nrows
for r in range(1, sheet.nrows):
    EquipmentNo = sheet.cell(r, 0).value
    EquipmentCode = sheet.cell(r, 1).value
    EquipmentType = sheet.cell(r, 2).value
    EquipmentName = sheet.cell(r, 3).value
    Area = sheet.cell(r, 4).value
    cell_date = datetime(*xldate_as_tuple(sheet.cell(r, 5).value, 0)).strftime('%Y-%d-%m %H:%M:%S')
    AddTime = cell_date
    Status = sheet.cell(r, 6).value
    values = (EquipmentNo, EquipmentCode, EquipmentType, EquipmentName, Area, AddTime, Status)
    # 执行sql语句
    cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")


