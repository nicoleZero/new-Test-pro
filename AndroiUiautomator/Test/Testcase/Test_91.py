#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：点击右上方刷新按钮
测试结果：开始发送水质监测请求，一段时间后，水质监测更新为当前的数据
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case91(self):
		pass
if __name__ == "__main__":
	unittest.test_case91()
	Actions.logout()