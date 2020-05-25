#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：添加设备，未勾选已确认上述操控，点击下一步
测试结果：跳转失败，提示请先勾选
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case69(self):
		pass
if __name__ == "__main__":
	unittest.test_case69()
	Actions.logout()