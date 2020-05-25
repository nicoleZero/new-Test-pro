#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：已注册邮箱用户，验证码输入超时
测试结果：提示验证码错误
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case29(self):
		pass
if __name__ == "__main__":
	unittest.test_case29()
	Actions.logout()