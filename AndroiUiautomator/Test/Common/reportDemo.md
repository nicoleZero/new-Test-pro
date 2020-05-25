HTMLTestRunner文件中需要修改的地方：
```buildoutcfg
第94行，将import StringIO修改成import io
第539行，将self.outputBuffer = StringIO.StringIO()修改成self.outputBuffer = io.StringIO()
第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
第766行，将uo = o.decode('latin-1')修改成uo = o
第775行，将ue = e.decode('latin-1')修改成ue = e
第631行，将print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))

```
```buildoutcfg
import logging
from selenium import webdriver
import time, os, unittest
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import HTMLTestRunner

class testadd(unittest.TestCase):
    def __int__(self):
        pass
    def setUp(self):
        pass
    def test_add1(self):
        self.assertEqual(2+3+5,10)
    def test_add2(self):
        self.assertEqual(0+8+7,15)
    def tearDown(self):
        pass
def suite():
    suiteTest =  unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    return suiteTest

if __name__=="__main__":
    filepath="D:\\RESULT.html"
    fp=open(filepath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"描述")
    runner.run(suite())
    fp.close()


```