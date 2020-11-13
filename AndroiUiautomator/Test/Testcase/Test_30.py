#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：已注册邮箱用户，验证码输入错误
测试结果：提示验证码错误
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case30(self):
		pass
if __name__ == "__main__":
	unittest.test_case30()
	Actions.logout()