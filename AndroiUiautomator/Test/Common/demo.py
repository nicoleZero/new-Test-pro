# coding=utf-8
import logging
from appium import webdriver
import os

'''
提供当前的基础操作，下载apk和连接驱动
'''
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)


class install_app():
    @classmethod
    def setUp(self):
        self.desire_caps = {}
        '''
        self.desire_caps['deviceName'] = '127.0.0.1:62001'

        self.desire_caps['appPackage'] = 'org.ecomo.tap'
        self.desire_caps['appActivity'] = 'org.ecomo.desktop.mvp.home.MainActivity'


        self.desire_caps['appPackage'] = 'com.vphone.launcher'
        self.desire_caps['appActivity'] = 'com.vphone.launcher.Launcher'
        self.desire_caps['platformName'] = 'Android'
        self.desire_caps['platformVersion'] = '7.1.2'
        #self.desire_caps['unicodeKeyboard'] = True
        self.desire_caps['resetKeyboard'] = True
        self.desire_caps['noReset'] = True
        self.desire_caps['sessionOverride'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desire_caps)

        '''
        self.desire_caps['deviceName'] = '127.0.0.1:62001'

        self.desire_caps['appPackage'] = 'com.taobao.taobao'
        self.desire_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'

        self.desire_caps['platformName'] = 'Android'
        self.desire_caps['platformVersion'] = '7.1.2'
        # self.desire_caps['unicodeKeyboard'] = True
        self.desire_caps['resetKeyboard'] = True
        self.desire_caps['noReset'] = True
        self.desire_caps['sessionOverride'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desire_caps)
        self.driver.find_element_by_id('org.ecomo.tap:id/vf_page')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    a = install_app.setUp()












