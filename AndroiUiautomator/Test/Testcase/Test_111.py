#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击每日鲜活，设置焕新自动启动时间，点击开启
测试结果：设置成功，定时触发焕新操控
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case111(self):
		pass
if __name__ == "__main__":
	unittest.test_case111()
	Actions.logout()