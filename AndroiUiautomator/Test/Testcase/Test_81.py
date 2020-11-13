#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：长按设备，选择重命名，前几取消
测试结果：重命名操控失败
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case81(self):
		pass
if __name__ == "__main__":
	unittest.test_case81()
	Actions.logout()