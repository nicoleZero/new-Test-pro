#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击回到主界面
测试结果：页面正常跳转至主界面
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case119(self):
		pass
if __name__ == "__main__":
	unittest.test_case119()
	Actions.logout()