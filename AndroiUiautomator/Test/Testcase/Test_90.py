#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择水质监测，点击TOC,TDS,COD
测试结果：正确显示三项内容
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case90(self):
		pass
if __name__ == "__main__":
	unittest.test_case90()
	Actions.logout()