#设备管理页面
from Test.Method import Actions
elements = Actions.find_elements()
class DeviceControl:
    '''
    获得设备个数
    '''
    def add_devices(self):
        add_element = elements.find_element("id","org.ecomo.tap:id/fbAdd").click()
        return add_element

    def remove_devices(self):
        pass

    def rename_devices(self):
        rename_element = elements.find_element()
        return rename_element

    def swipePage(self):
        pass

    def water_monitor(self):
        water_element = elements.find_element("id","org.ecomo.tap:id/menuRefresh").click()
        return water_element

    def share_data(self):
        share_element = elements.find_element("id","org.ecomo.tap:id/menuShare").click()
        return share_element

    def home(self):
        elements.tap([414,1480][486,1552])
        elements.find_element('id',"org.ecomo.tap:id/fbAdd")
        return elements

    def setting(self):
        setting_element = elements.find_element("class","android.widget.ImageButton").click()
        return setting_element


