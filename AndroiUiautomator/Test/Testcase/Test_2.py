#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：未勾选，点击登录
测试结果：跳转失败，提示请先勾选
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case2(self):
		pass
if __name__ == "__main__":
	unittest.test_case2()
	Actions.logout()