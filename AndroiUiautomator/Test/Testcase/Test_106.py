#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击每日鲜活
测试结果：进入每日鲜活，默认时间时当前时间，且关闭
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case106(self):
		pass
if __name__ == "__main__":
	unittest.test_case106()
	Actions.logout()