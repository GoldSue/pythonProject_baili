import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage



class LoginPage(BasePage):
    #元素定位

    user_loc = (By.XPATH,'//input[@formcontrolname="userId"]')
    password_loc = (By.XPATH,'//input[@placeholder="请输入密码"]')
    login_button_loc = (By.XPATH,'//button[@class="login-form-button ant-btn ant-btn-primary"]')
    my_home = (By.XPATH,'//span[text()="我的首页"]')
    assert_wrong_password_loc = (By.XPATH,'//span[contains(text(),"您还能尝试")]')
    assert_wrong_username_loc = (By.XPATH,'//span[contains(text(),"若您是采用微信注册")]')
    assert_login_url = "https://console-paas.digiwincloud.com.cn/"
    #页面操作

    def login(self,username = "18538231111",password = "Gold7789"):
        self.send_keys(LoginPage.user_loc,username,20)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.login_button_loc)
        self.get_screenshot("登录成功")

    def assert_right(self):
        # self.waite_ele(LoginPage.my_home,20)
        return self.get_value(LoginPage.my_home,25)

    def assert_wrong_password(self):
        self.get_screenshot("密码错误")
        return self.get_value(LoginPage.assert_wrong_password_loc)


    def assert_wrong_username(self):
        self.get_screenshot("账号错误")
        return self.get_value(LoginPage.assert_wrong_username_loc)


