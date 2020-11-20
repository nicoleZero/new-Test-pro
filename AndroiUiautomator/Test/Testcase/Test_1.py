#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：初次安装app，出现静态画面，直接点击退出后进入
测试结果：仍是静态画面显示
'''
from Test.Common.LoginPage import Login
import unittest, time
login = Login()
class EcomoTest(unittest.TestCase):
	def test_case1(self):
		time.sleep(3)
		login.click_protocol()
		login.beforelogin()
		#输入错误的用户名密码,点击登录,返回toast提示用户名密码错误
		login.afterlogin(user='18221730139',pwd='1234567')
		message = login.gettoast(2)
		assert message == '手机号或密码不正确'
		#login.resetPwd()
		#断言出现用户名密码错误

		#assert result == ''


