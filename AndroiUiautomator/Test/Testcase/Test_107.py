#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击每日鲜活，点击立即焕新
测试结果：出现提示，焕新需要时间等
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case107(self):
		pass
if __name__ == "__main__":
	unittest.test_case107()
	Actions.logout()