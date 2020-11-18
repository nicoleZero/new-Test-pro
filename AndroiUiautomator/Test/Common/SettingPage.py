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

    def settings(self):
        pass

    def show_history(self):
        month_element = elements.find_element("id","org.ecomo.tap:id/ll_month")
        daily_date_element = elements.find_element("id","org.ecomo.tap:id/tv_detail")
        return month_element,daily_date_element

    def show_map(self):
        pass

    def choose_month(self):
        choose_element = elements.find_element("id","")

        return choose_element

    def back(self):
        back_element = elements.find_element("id","android.widget.ImageButton").click()
        return back_element