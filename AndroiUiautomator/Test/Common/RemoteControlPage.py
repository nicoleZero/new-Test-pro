from Test.Method import Actions

elements = Actions.find_elements()

class RemoteControl:
    def wator_monitor(self,way="ֱ�ӵ��"):
        last_monitor = elements.find_element("id","org.ecomo.tap:id/tvMonitorTip")
        if way == "ֱ�ӵ��":
            water_element = elements.find_element("id","org.ecomo.tap:id/llMonitor").click()
        elif way == "����������":
            water_element = elements.find_element("id","org.ecomo.tap:id/btnMonitor").click()
        return last_monitor,water_element

    def dailyfresh(self,way="ֱ�ӵ��"):
        last_fresh = elements.find_element("id", "org.ecomo.tap:id/tvFreshTip")
        if way == "ֱ�ӵ��":
            fresh_element = elements.find_element("id","org.ecomo.tap:id/llFresh").click()
        elif way == "�����������":
            fresh_element = elements.find_element("id","org.ecomo.tap:id/btnFresh").click()
        return last_fresh,fresh_element

    def UV(self,way="ֱ�ӵ��"):
        UV_time = elements.find_element("id", "org.ecomo.tap:id/tvUvTip")
        if way == "ֱ�ӵ��":
            UV_element = elements.find_element("id","org.ecomo.tap:id/llSterilize").click()
        elif way == "�������ɱ��":
            UV_element = elements.find_element("id","org.ecomo.tap:id/btnUv").click()
        return UV_time,UV_element

    def temper(self,way="ֱ�ӵ��"):
        temperature = elements.find_element("id","org.ecomo.tap:id/tvFavoriteTip")
        if way == "ֱ�ӵ��":
            temper_element = elements.find_element("id","org.ecomo.tap:id/llFavorite").click()
        elif way == "�¶�":
            temper_element = elements.find_element("id","org.ecomo.tap:id/btnFavorite").click()
        return temperature,temper_element

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