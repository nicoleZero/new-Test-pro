#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：未勾选，点击登录
测试结果：跳转失败，提示请先勾选
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case4(self):
		pass
if __name__ == "__main__":
	unittest.test_case4()
	Actions.logout()