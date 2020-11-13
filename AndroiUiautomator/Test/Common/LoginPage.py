#登录前和登录页面
#可以选择邮箱登录，手机登录和微信登陆,登录页面
from Test.Method import Actions
elements = Actions.find_elements()
class Login:
    def click_protocol(self,input="yes"):
        if input == "yes":
            elements.find_element("id","org.ecomo.tap:id/iv_protocol").click()

    def beforelogin(self):
        loginelements = elements.find_element("id","org.ecomo.tap:id/btn_login").click()
        return loginelements

    def user_register(self):
        registerelements = elements.find_element("id","org.ecomo.tap:id/btn_sign_up").click()
        return registerelements

    def wx_login(self):
        wxelements = elements.find_element("id","org.ecomo.tap:id/btn_webhcat").click()
        return wxelements

    def afterlogin(self,user,pwd):
        et_user = elements.find_element("id","org.ecomo.tap:id/et_user").send_keys(user)
        et_pwd = elements.find_element("id","org.ecomo.tap:id/et_password").send_keys(pwd)
        click_button = elements.find_element("class","android.widget.Button").click()
        return click_button

    def resetPwd(self):
        resetpwd = elements.find_element("id","org.ecomo.tap:id/tv_forget").click()
        return resetpwd

