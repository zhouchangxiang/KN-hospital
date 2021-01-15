import xlrd
from common.asd import db_session
from common.asd import db_session, TagDetail, IncrementElectricTable, IncrementWaterTable


def read_Excel(file_dir):
    # 打开文件
    workbook = xlrd.open_workbook(file_dir)
    if workbook:
        # 获取所有sheet
        # print(workbook.sheet_names())# [u'sheet1', u'sheet2']
        # sheet1_name = workbook.sheet_names()[0]
        # 根据sheet索引或者名称获取sheet内容
        # sheet1 = workbook.sheet_by_index(0)
        sheet1 = workbook.sheet_by_name('2020年月度能耗记录')

        # sheet的名称，行数，列数
        print(sheet1.name, sheet1.nrows, sheet1.ncols)
        list1 = ['2020-01-31 23:00:00', '2020-02-29 23:00:00', '2020-03-31 23:00:00', '2020-04-30 23:00:00',
                 '2020-05-31 23:00:00', '2020-06-30 23:00:00', '2020-07-31 23:00:00', '2020-08-31 23:00:00',
                 '2020-09-30 23:00:00', '2020-10-31 23:00:00']
        if sheet1:
            if sheet1.nrows <= 0:
                return
            for row in range(1, sheet1.nrows):
                row_value = sheet1.row_values(row)
                if row_value[0] is None or row_value[0] == '':
                    continue
                i = 1
                for item in list1:
                    db_session.add(IncrementElectricTable(
                        Address=row_value[0],
                        IncremenValue='%.2f' % row_value[i],
                        CollectionDate=item,
                        IncremenType='电表'
                        ))
                    db_session.commit()
                    i += 1

    # 获取单元格内容的数据类型
    # print(sheet2.cell(1, 0).ctype)


if __name__ == '__main__':
    file_dir = r'D:\KN-hospital\202001101康宁医院罗湖院区用能表水表(1).xls'
    read_Excel(file_dir)
