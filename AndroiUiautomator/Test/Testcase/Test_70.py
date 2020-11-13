#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：添加新设备，输入超长的wifi名称和错误的密码
测试结果：添加设备失败，失败原因可点击查看
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case70(self):
		pass
if __name__ == "__main__":
	unittest.test_case70()
	Actions.logout()