import logging
from selenium import webdriver
import time, os, unittest
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import HTMLTestRunner

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)
try:
    desire_caps = {}
    desire_caps['platformName'] = 'Android'
    desire_caps['platformVersion'] = '7.1.2'
    desire_caps['deviceName'] = '127.0.0.1:62001'
    # desire_caps['app'] = PATH(r"C:\app-release.apk")
    desire_caps['appPackage'] = 'org.ecomo.tap'
    desire_caps['appActivity'] = 'org.ecomo.user.mvp.SplashActivity'
    desire_caps['unicodeKeyboard'] = True
    desire_caps['resetKeyboard'] = True
    # desire_caps['Accept-Language'] = 'zh-CN,zh;q=0.9'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps)

    '''
    login
    '''
    wait = WebDriverWait(driver, 10, 0.5)
    a = wait.until(EC.presence_of_element_located((By.ID, 'org.ecomo.tap:id/btn_login')))
    driver.find_element_by_id('org.ecomo.tap:id/iv_protocol').click()
    a.click()

    a = wait.until(EC.presence_of_element_located((By.ID, 'org.ecomo.tap:id/et_user')))
    a.send_keys("18221730139")
    driver.find_element_by_id('org.ecomo.tap:id/et_password').send_keys('18221730139')
    driver.find_elements_by_class_name('android.widget.Button').click()



except Exception as e:
    logging.debug(e)

