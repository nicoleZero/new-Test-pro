#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：选择远程操控，点击UV杀菌，点击立即杀菌
测试结果：设备开始工作，提示“可正常使用其他功能，分析完成数据自动更新”
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case113(self):
		pass
if __name__ == "__main__":
	unittest.test_case113()
	Actions.logout()