#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击水质检测，选择立即检测
测试结果：页面出现开始水质检测提示，一段时间后刷新数据和显示
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case98(self):
		pass
if __name__ == "__main__":
	unittest.test_case98()
	Actions.logout()