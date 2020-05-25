#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击水质检测，选择历史记录
测试结果：历史数据显示正确，按钮可选择，按照日期可查看当天的具体数据显示内容
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case100(self):
		pass
if __name__ == "__main__":
	unittest.test_case100()
	Actions.logout()