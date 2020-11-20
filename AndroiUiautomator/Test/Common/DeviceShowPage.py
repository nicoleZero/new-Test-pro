#!/usr/bin/python
# coding: utf-8
#设备管理页面
from Test.Method import Actions
elements = Actions.find_elements()
class DeviceShow:
    '''
    获得设备个数
    '''
    def getCounts(self):
        device_counts = elements.sign_up()
        return device_counts

    def user_info(self):
        user_elements = elements.find_element("id","org.ecomo.tap:id/tvTitle").click()
        return user_elements

    def user_info_right(self):
        user_right_element = elements.find_element("id","org.ecomo.tap:id/action_user").click()
        return user_right_element

    def add_devices(self):
        add_element = elements.find_element("id","org.ecomo.tap:id/fbAdd").click()
        return add_element

    def logout_right(self):
        self.user_info_right()
        logout_element = elements.find_element("id","org.ecomo.tap:id/btnLogOutRight").click()
        return logout_element

    def logout(self):
        self.user_info()
        logout_element = elements.find_element("id","org.ecomo.tap:id/btnLogOutLeft").click()
        return logout_element

