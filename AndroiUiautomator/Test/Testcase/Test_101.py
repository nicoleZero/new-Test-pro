#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击水质监测，选择立即监测，上述操控两次
测试结果：
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case101(self):
		pass
if __name__ == "__main__":
	unittest.test_case101()
	Actions.logout()