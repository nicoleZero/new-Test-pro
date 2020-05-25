'''
根据测试用例生成python文件，文件名称为Test_01.py等编号，
内部加上该测试用例描述
'''
#coding=utf-8
import importlib,sys
importlib.reload(sys)   #引用sys模块进来，并不是进行sys的第一次加载
import xlrd
from datetime import date
import os
import logging

try:
    workbook = xlrd.open_workbook(r"C:\Users\jiang\Desktop\C端APP\一目APP.xlsx")
    names = workbook.sheet_names()
    worksheet = workbook.sheet_by_index(0)
    nrows=worksheet.nrows
    ncols=worksheet.ncols
    script_steps= worksheet.col_values(5)
    expected_result= worksheet.col_values(6)
    d = date.today()
    for i in range(1,len(script_steps)):
        if script_steps[i] == '':
            continue
        else:
            description = worksheet.cell_value(i,5).encode('raw_unicode_escape')
            description = description.decode('utf-8')
            description = description.encode('utf-8').decode('unicode_escape')
            expected_results = worksheet.cell_value(i,6).encode('raw_unicode_escape')
            expected_results = expected_results.decode('utf-8')
            expected_results = expected_results.encode('utf-8').decode('unicode_escape')
            '''
            生成文件名称为Test_01.py文件，当文件存在时，不修改，文件不存在时新增
            '''
            if os.path.exists(r'C:\Users\jiang\PycharmProjects\AndroiUiautomator\Test\Testcase\Test_%d.py' %i):
                continue
            else:
                f = open(r'C:\Users\jiang\PycharmProjects\AndroiUiautomator\Test\Testcase\Test_%d.py' %i,"w",encoding='utf-8')
                f.write("#!/usr/bin/python\n" )
                f.write("# coding: utf-8\n")
                f.write("'''\n%s\n"%d.ctime())
                f.write("@author:jiangsisi\n")
                f.write(u"测试步骤：%s\n测试结果：%s\n'''" % (description, expected_results))
                f.write('\nfrom Test.Method import Actions\nimport unittest, time\nclass EcomoTest(unittest.TestCase):\n')
                f.write('\tdef test_case%d(self):\n'%i)
                f.write('\t\tpass\n')
                f.write('if __name__ == "__main__":\n\tunittest.test_case%d()\n\tActions.logout()'%i)
                f.close()
except Exception as e:
    logging.debug(msg="ERROR:%s"%e)

