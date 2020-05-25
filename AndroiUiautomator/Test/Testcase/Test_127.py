#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择设置，删除设备，点击取消
测试结果：删除失败，设备仍在
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case127(self):
		pass
if __name__ == "__main__":
	unittest.test_case127()
	Actions.logout()