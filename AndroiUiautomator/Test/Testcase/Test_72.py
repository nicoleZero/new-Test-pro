#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：添加设备，勾选已确认上述操控，选择密码可见
测试结果：输入的密码正常显示
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case72(self):
		pass
if __name__ == "__main__":
	unittest.test_case72()
	Actions.logout()