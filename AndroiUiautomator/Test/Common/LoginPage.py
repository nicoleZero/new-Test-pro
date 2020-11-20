#!/usr/bin/python
# coding: utf-8
#登录前和登录页面
#可以选择邮箱登录，手机登录和微信登陆,登录页面
from Test.Common.DeviceShowPage import DeviceShow
from Test.Method import Actions
#elements = Actions.find_elements()
class Login:
    def __init__(self):
        self.elements = Actions.find_elements()
    def click_protocol(self,input="yes"):
        if input == "yes":
            self.elements.find_element("id","org.ecomo.tap:id/iv_protocol").click()

    def beforelogin(self):
        loginelements = self.elements.find_element("id","org.ecomo.tap:id/btn_login").click()
        return loginelements

    def user_register(self):
        registerelements = self.elements.find_element("id","org.ecomo.tap:id/btn_sign_up").click()
        return registerelements

    def wx_login(self):
        wxelements = self.elements.find_element("id","org.ecomo.tap:id/btn_webhcat").click()
        return wxelements

    def afterlogin(self, user, pwd):
        self.elements.find_element("id","org.ecomo.tap:id/et_user").send_keys(user)
        self.elements.find_element("id","org.ecomo.tap:id/et_password").send_keys(pwd)
        inputuser = self.elements.find_element("class","android.widget.Button")[2].click()
        return inputuser

    def resetPwd(self):
        resetpwd = self.elements.find_element("id","org.ecomo.tap:id/tv_forget").click()
        return resetpwd

    def gettoast(self,num):
        #当出现弹框时,返回弹框内容,当未出现弹框时,返回登录后首页
        toast_message = {
            1:"手机号或邮箱不能为空",
            2:"手机号或密码不正确",
            3:""
        }
        message = '//*[@text=\'{}\']'.format(toast_message[num])
        if self.elements.find_element('xpath',message):
            return message
        else:
            return DeviceShow


