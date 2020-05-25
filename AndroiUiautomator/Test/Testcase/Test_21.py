#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：取消授权
测试结果：登录失败
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case21(self):
		pass
if __name__ == "__main__":
	unittest.test_case21()
	Actions.logout()