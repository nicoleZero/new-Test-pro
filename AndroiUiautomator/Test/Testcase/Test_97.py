#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击水质检测，点击返回
测试结果：回到远程操控页面
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case97(self):
		pass
if __name__ == "__main__":
	unittest.test_case97()
	Actions.logout()