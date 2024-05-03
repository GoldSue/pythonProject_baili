import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage



class LoginPage(BasePage):
    #元素定位

    user_loc = (By.XPATH,'//input[@formcontrolname="userId"]')
    password_loc = (By.XPATH,'//input[@placeholder="请输入密码"]')
    login_button_loc = (By.XPATH,'//button[@class="login-form-button ant-btn ant-btn-primary"]')
    nsws_home = (By.XPATH,'//div[@class="ant-tabs-tab-btn"]')
    assert_wrong_password_loc = (By.XPATH,'//span[@class="ng-tns-c62-63 ng-star-inserted"]')
    assert_wrong_username_loc = (By.XPATH,'//span[contains(text(),"若您是采用微信注册")]')
    assert_login_url = "https://console-paas.digiwincloud.com.cn/"
    #页面操作

    def login(self,username = "18538231111",password = "Gold7789"):
        self.send_keys(LoginPage.user_loc,username,50)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.login_button_loc)

    def assert_right(self):
        time.sleep(20)
        return self.get_value(LoginPage.nsws_home,40)

    # def assert_wrong_password(self):
    #     return self.get_value(LoginPage.assert_wrong_password_loc,25)

    def assert_wrong_username(self):
        return self.get_value(LoginPage.assert_wrong_username_loc,20)


