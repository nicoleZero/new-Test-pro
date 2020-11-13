#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击立即焕新，点击确认
测试结果：开始焕新，提示“设备正在焕新中不能进行其他操控”
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case113(self):
		pass
if __name__ == "__main__":
	unittest.test_case113()
	Actions.logout()