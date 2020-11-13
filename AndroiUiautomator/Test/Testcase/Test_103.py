#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击水质检测，选择历史记录
测试结果：可按照月份显示一个月的数据曲线
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case103(self):
		pass
if __name__ == "__main__":
	unittest.test_case103()
	Actions.logout()