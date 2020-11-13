from Test.Method import Actions

elements = Actions.find_elements()
class setting:
    def filter_record(self):
        filter_element = elements.find_element("id","org.ecomo.tap:id/tvFilterLife").click()
        return filter_element

    def history(self):
        history_element = elements.find_element("id","org.ecomo.tap:id/tvHistoryRecord").clikc()
        return history_element

    def map(self):
        map_element = elements.find_element("id","org.ecomo.tap:id/tvMap").click()
        return map_element

    def more(self):
        more_element = elements.find_element("id","org.ecomo.tap:id/tvSettings").click()
        return more_element

