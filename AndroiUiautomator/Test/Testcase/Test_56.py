#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：点击退出登录，取消
测试结果：再次进入app不需要登录
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case56(self):
		pass
if __name__ == "__main__":
	unittest.test_case56()
	Actions.logout()