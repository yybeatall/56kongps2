#!/usr/bin/env python
# coding:utf-8
import csv, xlrd
import time as t


def getCsv(file_name):
    rows = []
    with open(file_name, 'rb') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
    for row in readers:
        rows.append(row)
    return rows


def getExcel(rowValue, colValue, file_name='test.xlsx'):
    """
	:paramrowValue:
	表格的行
	:paramcolValue:
	表格的列
	:paramfile_name: excel
	文件
	:return:
	"""
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    return sheet.cell_value(rowValue, colValue)


def getDdtExcel(file_name='test.xlsx'):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
    return rows


# V客网登录
def clickLogin(driver, username, password):
    t.sleep(2)
    driver.find_element_by_id('l-1').send_keys(username)
    t.sleep(2)
    driver.find_element_by_id('l-2').send_keys(password)
    t.sleep(2)
    driver.find_element_by_id('l-4').click()


# 获取返回的错误信息
def getText(driver):
    return driver.find_element_by_xpath(".//*[@id='login-tips']").text
