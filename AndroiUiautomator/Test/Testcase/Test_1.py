#!/usr/bin/python
# coding: utf-8
'''
Wed May 20 00:00:00 2020
@author:jiangsisi
测试步骤：未勾选，点击注册
测试结果：跳转失败，提示请先勾选
'''
from Test.Method import Actions
import unittest, time
class EcomoTest(unittest.TestCase):
    def test_case1(self):
        self.driver = Actions.find_element(ways='id',icon='org.ecomo.tap:id/btn_login')
        self.driver.click()
        self.assertEqual(1,1)


if __name__ == "__main__":
    unittest.test_case1()
    Actions.logout()