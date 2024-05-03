import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.login_page import LoginPage


class UserManagePage(BasePage):
    #元素定位
    #新增用户
    user_manage_loc = (By.XPATH,'//span[text()="用户管理"]')
    add_cop_user_loc = (By.XPATH,'//span[text()="添加企业用户"]')
    add_add_cop_user_loc = (By.CSS_SELECTOR,'[class="user-new-add"]')
    add_new_loc = (By.XPATH,'//button[contains(@class,"ghost")]')
    user_id_loc = (By.XPATH,'//input[@class="ant-input ng-tns-c73-28 ng-untouched ng-pristine ng-invalid"]')
    user_name_loc = (By.XPATH,'//div[@class="ant-form-item-control-input-content ng-tns-c73-29"]/input')
    password_loc = (By.XPATH,'//input[@class="ant-input ng-tns-c73-30 ng-untouched ng-pristine ng-invalid"]')
    save_loc = (By.XPATH,'//span[text()="储存"]/parent::*')
    add_done = (By.XPATH,'//span[contains(text(),"新增完成")]')
    stop_use = (By.XPATH,'(//a[contains(text(),"停用")])[last()]')
    #编辑操作
    modify_user_loc = (By.XPATH,'(//a[text()="编辑"])[last()]')
    modify_user_name_loc = (By.CSS_SELECTOR,'input[formcontrolname="userName"]')
    modify_phone_loc = (By.CSS_SELECTOR,'input[formcontrolname="telephone"]')
    modify_save_loc = (By.CSS_SELECTOR,'button[class="ant-btn ant-btn-primary"]')
    assert_modify_loc = (By.XPATH,'//span[contains(text(),"修改成功")]')
    #用户停用删除
    close_user_loc =(By.CSS_SELECTOR,'[aria-label="Close"]')
    stop_use_loc = (By.XPATH, '(//a[contains(text(),"停用")])[last()]')
    stop_confirm_loc = (By.XPATH, '//span[text()=" 确定 "]')
    assert_stop_loc = (By.XPATH, '//span[contains(text(),"停用成功")]')
    delet_loc = (By.XPATH, '(//a[contains(text(),"删除")])[last()]')
    delet_confirm_loc = (By.XPATH, '//button[@class="ant-btn ng-tns-c34-68 ant-btn-primary ng-star-inserted"]')
    assert_delet_loc = (By.XPATH, '//span[contains(text(),"用户已删除")]')
    url = "https://console-paas.digiwincloud.com.cn/mang-user"

    #页面操作
    def add_user(self, username="hahk456g87", password="5kgA65ddpJ"):
        if self.get_url() != UserManagePage.url:
            self.click(UserManagePage.user_manage_loc)
        self.click(UserManagePage.user_manage_loc,50)
        self.click(UserManagePage.add_cop_user_loc,20)
        self.click(UserManagePage.add_add_cop_user_loc)
        self.click(UserManagePage.add_new_loc)
        self.send_keys(UserManagePage.user_id_loc,self.random())
        self.action_send_keys(UserManagePage.user_name_loc,username,20)
        self.send_keys(UserManagePage.password_loc,password,20)
        self.click(UserManagePage.save_loc)
        time.sleep(2)
        self.click(UserManagePage.close_user_loc)

    def assert_complet(self):
        return self.get_value(UserManagePage.add_done)

    def modify_save(self,username="jihi43h",phone=1387766422):

        if self.get_url() != UserManagePage.url:
            self.click(UserManagePage.user_manage_loc)
        self.click(UserManagePage.modify_user_loc,20)
        time.sleep(5)
        self.clear(UserManagePage.modify_user_name_loc)
        time.sleep(2)
        self.send_keys(UserManagePage.modify_user_name_loc,username,20)
        self.clear(UserManagePage.modify_phone_loc)
        self.send_keys(UserManagePage.modify_phone_loc,phone)
        self.click(UserManagePage.modify_save_loc)

    def asert_modify(self):
        return self.get_value(UserManagePage.assert_modify_loc)

    def user_stop(self):
        if self.get_url() != UserManagePage.url:
            self.click(UserManagePage.user_manage_loc)
        self.click(UserManagePage.stop_use_loc,20)
        self.click(UserManagePage.stop_confirm_loc,20)

    def assert_stop(self):
        return self.get_value(UserManagePage.assert_stop_loc)

    def del_user(self):
        time.sleep(5)
        if self.get_url() != UserManagePage.url:
            self.click(UserManagePage.user_manage_loc)

        self.click(UserManagePage.delet_loc,20)
        time.sleep(3)
        self.click(UserManagePage.delet_confirm_loc,20)

    def assert_del(self):
        return self.get_value(UserManagePage.assert_delet_loc)