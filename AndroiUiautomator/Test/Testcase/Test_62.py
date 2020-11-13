#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：退出app后，重新登录
测试结果：系统通知关闭
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case62(self):
		pass
if __name__ == "__main__":
	unittest.test_case62()
	Actions.logout()