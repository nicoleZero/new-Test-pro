#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：未勾选，点击微信登陆
测试结果：跳转失败，提示请先勾选
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case3(self):
		pass
if __name__ == "__main__":
	unittest.test_case3()
	Actions.logout()