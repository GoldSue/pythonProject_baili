from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep


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
    save_loc = (By.XPATH,'//span[contains(text(),"储存")]')
    add_done = (By.XPATH,'//span[contains(text(),"新增完成")]')
    stop_use = (By.XPATH,'(//a[contains(text(),"停用")])[last()]')
    #编辑操作
    uaser_manage_url = "https://console-paas.digiwincloud.com.cn/mang-user"
    modify_user_loc = (By.XPATH,'(//a[text()="编辑"])[last()]')
    modify_user_name_loc = (By.CSS_SELECTOR,'input[formcontrolname="userName"]')
    modify_phone_loc = (By.CSS_SELECTOR,'input[formcontrolname="telephone"]')
    modify_save_loc = (By.CSS_SELECTOR,'button[class="ant-btn ant-btn-primary"]')
    assert_modify_loc = (By.XPATH,'//span[contains(text(),"修改成功")]')
    close_user_loc =(By.CSS_SELECTOR,'[aria-label="Close"]')
    # 用户停用删除

    stop_use_loc = (By.XPATH, '(//a[contains(text(),"停用")])[last()]')
    stop_confirm_loc = (By.XPATH, '//span[text()=" 确定 "]')
    assert_stop_loc = (By.XPATH, '//span[contains(text(),"停用成功")]')
    delet_loc = (By.XPATH, '(//a[contains(text(),"删除")])[last()]')
    delet_confirm_loc = (By.XPATH, '//span[text()=" 确定 "]')
    assert_delet_loc = (By.XPATH, '//span[contains(text(),"用户已删除")]')
    url = "https://console-paas.digiwincloud.com.cn/mang-user"
    #邀请用户
    invite_user_loc = (By.XPATH,'//span[text()="邀请用户"]')
    invite_user_manage_loc = (By.XPATH,'//a[@angularticscategory="用戶管理-邀請"]')
    input_invite_user_loc = (By.ID,'user')
    user_chartra_loc = (By.CSS_SELECTOR,'(//dw-select-item[contains(@title,"用户")])[2]')
    out_user_loc = (By.XPATH,'(//div[@class="ant-select-item-option-content"])[2]')
    button_send_message_loc = (By.CSS_SELECTOR,'[angularticslabel="送出用戶邀請訊息"]')
    assert_invite_success_loc = (By.CSS_SELECTOR,'[class="ant-message-custom-content ng-tns-c62-56 ant-message-success"]')
    #批量邀请
    invite_users_manage_loc = (By.CSS_SELECTOR,'[angularticscategory="用戶管理-批量邀請"]')
    upload_file_loc = (By.CSS_SELECTOR,'[angularticscategory="用戶管理-上傳批量檔案"]')
    # file_path_loc = "D:\pythonProject_baili\data\account_invite.xlsx"
    button_send_file_loc = (By.CSS_SELECTOR,'[angularticscategory="用戶管理-送出批量邀請訊息"]')
    #用户群组
    #新增用户群组
    user_group_url = "https://console-paas.digiwincloud.com.cn/mang-user/organization-mang/org-list"
    user_group_loc = (By.XPATH,'(//div[@class="ant-tabs-tab-btn"])[2]')
    add_user_group_loc = (By.CLASS_NAME,'user-new-add')
    input_group_id_loc = (By.CSS_SELECTOR,'[placeholder="请输入用户群组ID"]')
    input_group_name_loc = (By.CSS_SELECTOR,'[placeholder="请输入用户群组名称"]')
    button_save_loc = (By.CSS_SELECTOR,'[class="btn ant-btn ant-btn-primary"]')
    assert_save_loc = (By.XPATH,'//span[text()="用户群组已新增"]')
    close_add_window_loc = (By.XPATH, '[class="ant-modal-close-x"]')
    # 修改用户群组
    group_url = "/mang-user/organization-mang/org-list"
    modifu_group_loc = (By.XPATH,'(//a[text()=" 修改 "])[last()]')
    modify_group_name_loc = (By.CSS_SELECTOR,'[placeholder="请输入用户群组名称"]')
    modify_kenel_loc = (By.CSS_SELECTOR,'[class="ant-select-selection-item ng-star-inserted"]')
    modify_dep_loc = (By.XPATH,'(//div[@class="ant-select-item-option-content"])[2]')
    modify_group_save_loc = (By.CSS_SELECTOR,'[class="btn ant-btn ant-btn-primary"]')
    assert_modify_group_loc = (By.XPATH,'//font[text()="用户群组已修改"]')
    #删除用户群组
    delete_user_group_loc = (By.XPATH,'(//a[@angularticslabel="刪除用戶群組"])[last()]')
    delete_confirm_loc = (By.XPATH,'//span[text()=" 确定 "]')
    assert_delete_user_loc = (By.XPATH,'//span[text()="用户群组已删除"]')

    #页面操作
    #新增用户
    def add_user(self, username="hahk456g87", password="5kgA65ddpJ"):

        self.click(UserManagePage.user_manage_loc,10)
        self.click(UserManagePage.add_cop_user_loc,10)
        self.click(UserManagePage.add_add_cop_user_loc)
        self.click(UserManagePage.add_new_loc)
        self.send_keys(UserManagePage.user_id_loc,self.random())
        self.action_send_keys(UserManagePage.user_name_loc,username,10)
        self.send_keys(UserManagePage.password_loc,password,10)
        self.click(UserManagePage.save_loc)
        self.click(UserManagePage.close_user_loc)

    #新增用户断言
    def assert_add(self):
        return self.get_value(UserManagePage.add_done)

    #修改用户信息
    def modify_save(self,username="jihi43h",phone=1387766422):

        try:
            self.waite_ele(UserManagePage.modify_user_loc)
        except:
            self.driver.get(UserManagePage.uaser_manage_url)
        finally:
            self.click(UserManagePage.modify_user_loc,10)
            self.clear_input(UserManagePage.modify_user_name_loc,username)
            self.clear_input(UserManagePage.modify_phone_loc,phone)
            self.click(UserManagePage.modify_save_loc)


    #断言修改成功
    def asert_modify(self):
        return self.get_value(UserManagePage.assert_modify_loc)

    #停用用户
    def user_stop(self):

        try:
            self.waite_ele(UserManagePage.stop_use_loc)
        except:
            self.driver.get(UserManagePage.uaser_manage_url)
        finally:
            self.click(UserManagePage.stop_use_loc)
            self.click(UserManagePage.stop_confirm_loc)

    #断言停用成功
    def assert_stop(self):
        return self.get_value(UserManagePage.assert_stop_loc)

    #删除用户
    def del_user(self):

        try:
            self.waite_ele(UserManagePage.delet_loc)
        except:
            self.driver.get(UserManagePage.uaser_manage_url)
        finally:
            sleep(2)
            self.click(UserManagePage.delet_loc, 20)
            sleep(2)
            self.click(UserManagePage.delet_confirm_loc, 20)

    #断言删除成功
    def assert_del(self):
        return self.get_value(UserManagePage.assert_delet_loc)

    #邀请用户
    def invite_user(self,userid=123444344):
        try:
            self.waite_ele(UserManagePage.delet_loc)
        except:
            self.driver.get(UserManagePage.uaser_manage_url)
        finally:
            self.click(UserManagePage.invite_user_loc)
            sleep(1)
            self.click(UserManagePage.invite_user_manage_loc)
            self.send_keys(UserManagePage.input_invite_user_loc,userid)
            sleep(2)
            self.click(UserManagePage.button_send_message_loc)
            sleep(2)

    #断言邀请成功
    def assert_invite(self):
        return self.get_value(UserManagePage.assert_invite_success_loc,15)

    #批量邀请用户
    def invite_users(self,filename="account_invite.xlsx"):

        try:
            self.waite_ele(UserManagePage.delet_loc)
        except:
            self.driver.get(UserManagePage.uaser_manage_url)
        finally:
            self.click(UserManagePage.invite_user_loc)
            self.click(UserManagePage.invite_users_manage_loc)
            sleep(2)
            self.click(UserManagePage.upload_file_loc)
            sleep(2)
            self.upload_file(filename)
            # time.sleep(1)
            self.click(UserManagePage.button_send_file_loc)

    def add_user_group(self):
        self.click(UserManagePage.user_group_loc)

        try:
            self.waite_ele(UserManagePage.add_user_group_loc)
        except:
            self.driver.get(UserManagePage.user_group_url)
        finally:
            sleep(3)
            self.click(UserManagePage.add_user_group_loc)
            self.send_keys(UserManagePage.input_group_id_loc,self.random())
            sleep(1)
            self.send_keys(UserManagePage.input_group_name_loc,self.random())
            sleep(1)
            self.click(UserManagePage.button_save_loc)
            sleep(2)

    def assert_group_save(self):
        return self.get_value(UserManagePage.assert_save_loc)

    def modify_group(self,group="132erw"):

        try:
            self.waite_ele(UserManagePage.user_group_loc)
        except:
            self.driver.get(UserManagePage.user_group_url)
        finally:
            self.click(UserManagePage.modifu_group_loc)
            self.clear(UserManagePage.modify_group_name_loc)
            self.send_keys(UserManagePage.modify_group_name_loc,group)
            self.click(UserManagePage.modify_kenel_loc)
            self.click(UserManagePage.modify_dep_loc)
            self.click(UserManagePage.modify_group_save_loc)
            sleep(2)
    def assert_modify_group(self):
        return self.get_value(UserManagePage.assert_modify_group_loc)

    #删除用户群组
    def delete_user_group(self):

        try:
            self.waite_ele(UserManagePage.user_group_loc)
        except:
            self.driver.get(UserManagePage.user_group_url)
        finally:
            self.click(UserManagePage.delete_user_group_loc)
            sleep(2)
            self.click(UserManagePage.delete_confirm_loc)

    def assert_del_user(self):
        return self.get_value(UserManagePage.assert_delete_user_loc)









