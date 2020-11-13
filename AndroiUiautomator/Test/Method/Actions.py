from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import logging
import selenium
from Test.Common import AppiumBase
import time
from appium import webdriver
'''
进行常用操作设置：显示等待操作
'''
User="18221730139"
Pwd="18221730139"

class find_elements:
    def __init__(self):

        self.app = AppiumBase.install_app()
        self.driver = self.app.setUp()

    def find_element(self,ways, icon, timeout=10):
        logging.info("查找元素:" + icon)

        try:
            if ways == "id":
                element = WebDriverWait(self.driver, timeout, 1, NoSuchElementException).until(
                    lambda driver: self.driver.find_element_by_id(icon))
                return element
            elif ways == "class":
                element = WebDriverWait(self.driver, timeout, 1, NoSuchElementException).until(
                    lambda driver: self.driver.find_elements_by_class_name(icon))
                return element
            elif ways == "xpath":
                element = WebDriverWait(self.driver, timeout, 1, NoSuchElementException).until(
                    lambda driver: self.driver.find_element_by_xpath(icon))
                return element
            else:
                return "需要其他定位方式"
        except selenium.common.exceptions.TimeoutException:
            logging.error("超时找不到元素")
        except selenium.common.exceptions.NoSuchElementException:
            logging.error("不存在这个元素")
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y

    def swipeLeft(self,t):
        l=self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self,t):
        l=self.getSize()
        x1=int(l[0]*0.25)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipeUp(self,t):
        l=self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.4)
        self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(5)

    def swipeDown(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    def login(self):
        a = self.find_element("id", 'org.ecomo.tap:id/iv_protocol', 10)#点击同意协议
        a.click()
        a = self.find_element("id", 'org.ecomo.tap:id/btn_login', 10)#点击登录
        a.click()



    def logout(self):
        self.driver.quit()

    def sign_up(self):
        a = self.find_element("id", 'org.ecomo.tap:id/iv_protocol', 10)#点击同意协议
        a.click()
        a = self.find_element("id", 'org.ecomo.tap:id/btn_sign_up', 10)#点击注册
        a.click()


    def screenshot(self,path,scriptname):
        self.driver.get_screenshot_as_file(path)
        self.driver.save_screenshot('%s'%scriptname+'.png')
        return "saveIMG OK!"

    def tap(self,x,y):
        self.driver.tap(x,y)





