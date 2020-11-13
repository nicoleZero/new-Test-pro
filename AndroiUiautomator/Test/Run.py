# coding=utf-8
'''
执行测试用例并将结果返回至邮箱
'''
import sys
import time, os, unittest
import HTMLTestRunner
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
from Test.Common import AppiumBase
d = datetime.datetime.now()
path = "\\".join(sys.path[0].split("\\")[:5])

test_dir = path+r'\Testcase'
filepath=path+r"\Report"
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

def createSuite(test_dir):
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='Test_*.py')

    for suite in discover:
        for case in suite:
            testunit.addTest(case)
    return testunit

def runTestCase(testunit):
    fp=open(filepath+"\RESULT_%s.html"%d.strftime('%Y-%m-%d-%H-%M-%S'),'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"描述")
    suite = createSuite(test_dir)
    runner.run(suite)
    fp.close()
    return fp

def sendEmail(testFile):
    host_server = "smtp.126.com"  # 设置服务器
    sender = "jiang_sisi@126.com"  # 用户名
    pwd = "ZCOMYVVKCWLYJDCB"  # 口令
    receiver = ['jiang_sisi@126.com']


    try:
        server = smtplib.SMTP_SSL(host_server, 465)
        server.login(sender, pwd)
        msg = MIMEText('测试报告发送', 'plain', 'utf-8')
        msg['Subject'] = Header("测试结果", 'utf-8')
        msg['From'] = receiver
        msg['To'] = receiver
        server.sendmail(sender, sender,msg.as_string())
        server.quit()
        print("发送邮件成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



if __name__ == "__main__":
    try:
        #install = AppiumBase.install_app
        testunit = createSuite(test_dir)
        result = runTestCase(testunit)
        sendEmail(result)

    except Exception as e:
        print(e)
        logging.debug(msg="ERROR:%s"%e)