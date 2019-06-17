from xlutils.copy import copy
import xlrd
import xlwt





# 读excel文件
workbook = xlrd.open_workbook('C:/Users/boyete1550865707/Desktop/1宝贝王Oracle制单、审核过账统计新.xls')
    # 获取所有sheet
sheet_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
sheet = workbook.sheet_by_index(0)

# 3. 新建一个工作薄，copy打开的工作薄
#new_excel = copy(workbook)

# 4. 在新的工作表中获取到第0个工作表
#new_sheet = new_excel.get_sheet(0)


i = 1
for i in range(3, sheet.nrows):
    if not sheet.cell_value(i, 3) == '':
        print(sheet.row_values(i))
