from Test.Method import Actions

elements = Actions.find_elements()
class Filter:
    def filter_detail(self):
        filter_1 = elements.find_element("id","org.ecomo.tap:id/pbFilter1")
        filter_2 = elements.find_element("id","org.ecomo.tap:id/pbFilter2")
        filter_3 = elements.find_element("id","org.ecomo.tap:id/pbFilter3")


    def buy_filter(self,num=1):
        buy = elements.find_element("id","org.ecomo.tap:id/btnBuy").click()

    def to_shop(self,shopee,num=1):
        self.buy_filter(num=num)
        if shopee=="天猫":
            elements.find_element("id","org.ecomo.tap:id/btnTaobao")
            shop_element = elements.find_element("id","org.ecomo.tap:id/btnOk").click()
        elif shopee=="京东":
            elements.find_element("id","org.ecomo.tap:id/btnJd")
            shop_element = elements.find_element("id", "org.ecomo.tap:id/btnOk").click()
        elif shopee == "有品":
            elements.find_element("id","org.ecomo.tap:id/btnYoupin")
            shop_element = elements.find_element("id", "org.ecomo.tap:id/btnOk").click()
        return shop_element

    def water_monitor(self):
        water_element = elements.find_element("id", "org.ecomo.tap:id/menuRefresh").click()
        return water_element

"""    def share_data(self):
        share_element = elements.find_element("id", "org.ecomo.tap:id/menuShare").click()
        return share_element

    def home(self):
        elements.tap([414, 1480][486, 1552])
        elements.find_element('id', "org.ecomo.tap:id/fbAdd")
        return elements

    def setting(self):
        setting_element = elements.find_element("class","android.widget.ImageButton").click()
        return setting_element
"""