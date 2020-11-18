#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：初次安装app，出现静态画面，直接点击退出后进入
测试结果：仍是静态画面显示
'''
from Test.Common.LoginPage import Login
from Test.Method import Actions
import unittest, time
login = Login()
class EcomoTest(unittest.TestCase):
	def test_case1(self):
		time.sleep(10)
		login.click_protocol()
		login.beforelogin()



