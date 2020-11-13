#静态页面,有四幅静态页面显示
#20201112134
from Test.Method import Actions
elements = Actions.find_elements()
class ClickStaticPage:
    def showStaticspic(self,times=1):
        for i in range(1,times):
            Staticspic = elements.find_element(ways='xpath', icon='//*[@class=android.widget.LinearLayout]').swipeLeft()
        return Staticspic
