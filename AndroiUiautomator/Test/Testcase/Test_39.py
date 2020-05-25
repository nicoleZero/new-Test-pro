#!/usr/bin/python
# coding: utf-8
'''
Mon May 25 00:00:00 2020
@author:jiangsisi
测试步骤：登录app后，点击头像更改，使用相机，拍照点击取消
测试结果：头像更改失败
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case39(self):
		pass
if __name__ == "__main__":
	unittest.test_case39()
	Actions.logout()