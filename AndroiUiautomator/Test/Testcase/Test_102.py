#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击水质检测，选择历史记录，退出
测试结果：回到上一页面
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case102(self):
		pass
if __name__ == "__main__":
	unittest.test_case102()
	Actions.logout()