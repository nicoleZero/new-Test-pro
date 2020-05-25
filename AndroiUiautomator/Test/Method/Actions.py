from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import logging
import selenium
from Test.Common import AppiumBase
'''
进行常用操作设置：显示等待操作
'''
User="18221730139"
Pwd="18221730139"
app = AppiumBase.install_app()
driver = app.install_apk()

def find_element(ways, icon, timeout=10,driver=driver):

    logging.info("查找元素:" + icon)
    try:
        if ways == "id":
            element = WebDriverWait(driver, timeout, 1, NoSuchElementException).until(
                lambda driver: driver.find_element_by_id(icon))
            return element
        elif ways == "class Name":
            element = WebDriverWait(driver, timeout, 1, NoSuchElementException).until(
                lambda driver: driver.find_elements_by_class_name(icon))
            return element
        else:
            return "需要其他定位方式"
    except selenium.common.exceptions.TimeoutException:
        logging.error("超时找不到元素")
    except selenium.common.exceptions.NoSuchElementException:
        logging.error("不存在这个元素")


def login():
    a = find_element("id", 'org.ecomo.tap:id/iv_protocol', 10)#点击同意协议
    a.click()
    a = find_element("id", 'org.ecomo.tap:id/btn_login', 10)#点击登录
    a.click()



def logout(driver=driver):
    driver.quit()

def sign_up():
    a = find_element("id", 'org.ecomo.tap:id/iv_protocol', 10)#点击同意协议
    a.click()
    a = find_element("id", 'org.ecomo.tap:id/btn_sign_up', 10)#点击注册
    a.click()


