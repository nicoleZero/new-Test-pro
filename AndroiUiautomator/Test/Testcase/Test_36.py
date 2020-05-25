#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：点击退出登录，确定退出
测试结果：再次进入app需重新登录
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case36(self):
		pass
if __name__ == "__main__":
	unittest.test_case36()
	Actions.logout()