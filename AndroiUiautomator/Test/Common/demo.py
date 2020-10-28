# coding=utf-8
import logging
from selenium import webdriver
import os
'''
提供当前的基础操作，下载apk和连接驱动
'''
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

desire_caps = {}
desire_caps['platformName'] = 'Android'
desire_caps['platformVersion'] = '7.1.2'
desire_caps['deviceName'] = '127.0.0.1:62001'
desire_caps['appPackage'] = 'org.ecomo.tap'
desire_caps['appActivity'] = 'org.ecomo.user.mvp.SplashActivity'
desire_caps['unicodeKeyboard'] = True
desire_caps['resetKeyboard'] = True
desire_caps['noReset'] = True
desire_caps['sessionOverride'] = True
        #print(self.desire_caps)
def install_apk():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps)
    #driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desire_caps)
    return driver

install_apk()





