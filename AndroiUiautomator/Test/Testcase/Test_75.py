#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：添加设备，勾选已确认上述操控，不输入wifi和密码，点击下一步
测试结果：不可跳转
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case75(self):
		pass
if __name__ == "__main__":
	unittest.test_case75()
	Actions.logout()