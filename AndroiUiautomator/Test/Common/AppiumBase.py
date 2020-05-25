import logging
from selenium import webdriver

'''
提供当前的基础操作，下载apk和连接驱动
'''
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

class install_app():
    def __init__(self):
        self.desire_caps = {}
        self.desire_caps['platformName'] = 'Android'
        self.desire_caps['platformVersion'] = '4.4.2'
        self.desire_caps['deviceName'] = '127.0.0.1:62001'
        self.desire_caps['appPackage'] = 'org.ecomo.tap'
        self.desire_caps['appActivity'] = 'org.ecomo.user.mvp.SplashActivity'
        self.desire_caps['unicodeKeyboard'] = True
        self.desire_caps['resetKeyboard'] = True
        self.desire_caps['noReset'] = True
        self.desire_caps['sessionOverride'] = True
    def install_apk(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desire_caps)
        return driver





