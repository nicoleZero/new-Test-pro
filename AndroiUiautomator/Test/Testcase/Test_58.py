#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：退出app后，重新登陆
测试结果：系统通知打开
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case58(self):
		pass
if __name__ == "__main__":
	unittest.test_case58()
	Actions.logout()