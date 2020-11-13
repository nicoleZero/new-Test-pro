#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择设置，删除设备，点击确认
测试结果：删除成功，数据库中设备valid字段置为0
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case128(self):
		pass
if __name__ == "__main__":
	unittest.test_case128()
	Actions.logout()