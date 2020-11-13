#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：未注册手机用户，点击发送验证码
测试结果：提示用户未注册
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case25(self):
		pass
if __name__ == "__main__":
	unittest.test_case25()
	Actions.logout()