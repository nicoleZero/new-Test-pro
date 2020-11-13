#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：长按设备，选择重命名，输入大于40各自的名字，点击确定
测试结果：提示超长
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case80(self):
		pass
if __name__ == "__main__":
	unittest.test_case80()
	Actions.logout()