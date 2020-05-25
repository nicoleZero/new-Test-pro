#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：输入正确的旧密码和相同的新密码
测试结果：提示密码更改成功，使用新密码登录成功
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case53(self):
		pass
if __name__ == "__main__":
	unittest.test_case53()
	Actions.logout()