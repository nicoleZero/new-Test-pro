#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：添加设备，勾选已确认上述操控，下拉选择wifi，输入密码
测试结果：wifi可选，密码正常输入
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case70(self):
		pass
if __name__ == "__main__":
	unittest.test_case70()
	Actions.logout()