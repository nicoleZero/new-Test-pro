#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：登录app后，点击头像更改，使用相册，拍照点击完成
测试结果：头像更改成功
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
	def test_case42(self):
		pass
if __name__ == "__main__":
	unittest.test_case42()
	Actions.logout()