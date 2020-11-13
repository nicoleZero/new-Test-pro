#!/usr/bin/python
# coding: utf-8
'''
Mon Nov  2 00:00:00 2020
@author:jiangsisi
测试步骤：初次安装app，出现静态画面，直接点击退出后进入
测试结果：仍是静态画面显示
'''
from Test.Method import Actions
import unittest, time
from appium import webdriver
class EcomoTest(unittest.TestCase):
	def test_case1(self):
		find_elements = Actions.find_elements()
		elements=find_elements.find_element(ways='xpath', icon='//*[@class=android.widget.LinearLayout]').swipeLeft()
		self.assertEqual(elements,find_elements.find_element(ways='xpath', icon='//*[@class=android.widget.LinearLayout[contains(@text,"查看历史数据")]'))
		#按home键退出app
		find_elements.keyevent(82)

