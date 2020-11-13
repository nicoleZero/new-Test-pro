
from Test.Method import Actions
elements = Actions.find_elements
class Register:
    def register(self,newuser,pwd):
        regi_user = elements.find_element("id","org.ecomo.tap:id/et_phone").send_keys(newuser)
        regi_pwd = elements.find_element("id","org.ecomo.tap:id/et_password").send_keys(pwd)
        code = elements.find_element("id","org.ecomo.tap:id/tv_code").click()
        regist = elements.find_element("class","android.widget.Button").click()
        return regist


