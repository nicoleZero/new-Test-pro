# coding=gbk
'''
ִ�в������������������������
'''
import time, os, unittest
import HTMLTestRunner
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging

d = datetime.datetime.now()

test_dir = r'C:\Users\jiang\PycharmProjects\AndroiUiautomator\Test\Testcase'
filepath=r"C:\Users\jiang\PycharmProjects\AndroiUiautomator\Test\Report"
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
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"���Ա���",description=u"����")
    suite = createSuite(test_dir)
    runner.run(suite)
    fp.close()
    return fp

def sendEmail(testFile):
    host_server = "smtp.126.com"  # ���÷�����
    sender = "jiang_sisi@126.com"  # �û���
    pwd = "ZCOMYVVKCWLYJDCB"  # ����
    receiver = ['jiang_sisi@126.com']


    try:
        server = smtplib.SMTP_SSL("smtp.126.com", 465)
        server.login(sender, pwd)
        msg = MIMEText('���Ա��淢��', 'plain', 'utf-8')
        msg['Subject'] = Header("���Խ��", 'utf-8')
        msg['From'] = sender
        msg['To'] = sender
        server.sendmail(sender, sender,msg.as_string())
        server.quit()
        print("�����ʼ��ɹ�")
    except smtplib.SMTPException:
        print("Error: �޷������ʼ�")

if __name__ == "__main__":
    try:
        testunit = createSuite(test_dir)
        result = runTestCase(testunit)
        sendEmail(result)
    except Exception as e:
        print(e)
        logging.debug(msg="ERROR:%s"%e)