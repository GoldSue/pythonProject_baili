#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/18 19:22
# @Author  : libaojin
# @File    : co_manage.py.py
from selenium.webdriver.common.by import By
from time import sleep
from base.base_page import BasePage


class CoOperation(BasePage):


    #元素定位
    #企业运营
    #1.运营单元
    co_operat_loc = (By.XPATH,'//span[text()="企业运营"]')
    #新增公司其他
    add_co_anaother_loc = (By.CSS_SELECTOR,'[class="btn-group"]>a:nth-child(1)')
    co_id_loc = (By.CSS_SELECTOR,'[placeholder="请输入ID"]')
    co_name_loc = (By.CSS_SELECTOR,'[placeholder="请输入公司别名称"]')
    select_loc = (By.XPATH,'//dw-select-item[@title="公司" or @title="法人" ]')
    select_opt1_loc = (By.XPATH,'(//div[@class="ant-select-item-option-content"])[1]')
    add_co_save = (By.XPATH,'(//div[@class="btn"]/button)[2]')
    assert_add_co_loc = (By.XPATH,'//span[contains(text(),"新增成功")]')
    #修改公司信息
    operate_url = "https://console-paas.digiwincloud.com.cn/mang-business-operations/group-mang"
    modify_co_loc = (By.XPATH,'(//a[text()=" 修改 "])[last()]')
    select_opt2_loc = (By.XPATH, '(//div[@class="ant-select-item-option-content"])[2]')
    assert_modiye_co_loc = (By.XPATH,'//span[contains(text(),"修改成功")]')
    #删除公司
    delete_co_loc = (By.XPATH,'(//a[text()=" 删除 "])[last()]')
    delete_confirm_loc = (By.XPATH,'//span[text()=" 确定 "]')

    #2.员工管理
    employee_management_loc = (By.XPATH,'(//div[@class="ant-tabs-tab-btn"])[2]')
    add_employee_loc = (By.XPATH,'//span[text()="新增员工"]')
    employee_id_loc = (By.CSS_SELECTOR,'[placeholder="请输入员工工号"]')
    employee_name_loc = (By.CSS_SELECTOR,'[placeholder="请输入员工姓名"]')
    employee_save_loc = (By.CLASS_NAME,'ant-btn ant-btn-primary')
    confirme_save_loc = (By.XPATH,'//span[text()=" 确定保存 "]')
    assert_add_employee_loc = (By.XPATH,'//span[contains(text(),"新增成功")]')
    #修改员工
    modyfi_employee_loc = (By.XPATH,'(//a[text()="停用"])[1]')
    assert_modify_employee_loc = (By.XPATH,'//span[contains(text(),"修改成功")]')
    #停用员工
    stop_employee_loc = (By.XPATH,'(//a[text()="停用"])[1]')
    assert_stop_employee_loc = (By.XPATH,'//span[contains(text(),"停用成功")]')
    #删除员工
    delete_employee_loc = (By.XPATH,'(//a[text()="删除"])[1]')
    delete_employee_confirm_loc = (By.CSS_SELECTOR,'[class="ant-btn ng-tns-c34-241 ant-btn-primary ng-star-inserted"]')
    assert_delete_employee_loc = (By.XPATH,'//span[contains(text(),"删除成功")]')
    #导入员工
    import_employee_loc = (By.XPATH,'//span[text()="导入"]')
    download_templat_loc = (By.XPATH,'//span[text()="下载模版 "]')
    upload_employee_loc = (By.XPATH,'//span[text()="上传档案"]')
    import_button_loc = (By.XPATH,'//span[text()="导入员工"]')
    assert_import_ok_loc = (By.XPATH,'//span[contains(text(),"导入成功")]')
    #导出员工
    export_employee_loc =(By.XPATH,'//span[text()="导出"]')
    export_list_loc =(By.XPATH,'//span[text()="导出清单"]')
    click_none_loc = (By.TAG_NAME,'body')
    #3.企业组织
    co_organize_loc = (By.XPATH,'(//div[@class="ant-tabs-tab-btn"])[3]')
    add_dep_loc = (By.XPATH,'//span[text()="新增部门"]')
    co_an_name_loc = (By.CSS_SELECTOR,'[class="ant-select-selection-search-input ng-pristine ng-valid ng-touched"]')
    co_name_first_loc = (By.XPATH,'(//div[@class="ant-select-item-option-content"])[1]')
    dept_id_loc = (By.CSS_SELECTOR,'[placeholder="请输入部门 ID"]')
    dept_name_loc = (By.CSS_SELECTOR,'[placeholder="请输入部门名称"]')
    chioce_dept_director_loc = (By.CSS_SELECTOR,'[placeholder="请选择部门主管"]')
    chioce_director_loc = (By.XPATH,'(//input[@class="ant-checkbox-input ng-untouched ng-pristine ng-valid"])[1]')
    chioce_sure_loc = (By.XPATH,'//span[text()="确定"]')
    add_dept_save_loc = (By.XPATH,'//span[text()=" 储存 "]')
    dept_decide_level_loc = (By.CSS_SELECTOR,'[title="4321(431)"]')
    chioce_dept_level_loc = (By.CSS_SELECTOR,'[class="ant-select-item-option-content"]')
    assert_add_dept_loc = (By.XPATH,'//span[contains(text(),"新增成功")]')

    #4.场域管理
    #新增场域
    site_manage_loc =(By.XPATH,'(//div[@class="ant-tabs-tab-btn"])[4]')
    add_site_loc = (By.XPATH,'(//div[@class="btn-group"]/a)[1]')
    site_nature_loc = (By.XPATH,'(//dw-select-search[@class="ant-select-selection-search ng-star-inserted"])[2]')
    site_id_loc = (By.CSS_SELECTOR,'[placeholder="请输入ID"]')
    site_name_loc = (By.CSS_SELECTOR,'[placeholder="请输入场域名称"]')
    site_save_loc = (By.XPATH,'//span[text()=" 储存 "]')
    assert_add_site = (By.XPATH,'//span[contains(text(),"新增成功")]')
    #修改场域
    modify_site_loc = (By.XPATH,'(//a[text()="修改"])[1]')
    assert_modify_site_loc = (By.XPATH,'//span[contains(text(),"修改成功")]')
    #s删除场域
    delete_site_loc = (By.XPATH,'(//a[text()="删除"])[1]')
    delete_site_confirm_loc = (By.XPATH,'//span[text()=" 确定 "]')
    assert_delete_site_loc = (By.XPATH,'//span[text()="删除成功"]')

    #页面操作
    def add_co(self,name = "123"):
        self.click(CoOperation.co_operat_loc)
        self.click(CoOperation.add_co_anaother_loc)
        self.send_keys(CoOperation.co_id_loc,self.random())
        self.send_keys(CoOperation.co_name_loc,name)
        self.click(CoOperation.select_loc)
        self.click(CoOperation.select_opt1_loc)
        self.click(CoOperation.add_co_save)

    def assert_add_co(self):
        return self.get_value(CoOperation.assert_add_co_loc)


    def modify_co(self):
        try:
            self.waite_ele(CoOperation.modify_co_loc,5)
        except:
            self.refresh_url(CoOperation.operate_url)
        finally:
            sleep(2)
            self.click(CoOperation.modify_co_loc)
            self.clear_input(CoOperation.co_id_loc,self.random())
            self.clear_input(CoOperation.co_name_loc,self.random())
            self.click(CoOperation.select_loc)
            self.click(CoOperation.select_opt2_loc)
            self.click(CoOperation.add_co_save)

    def assert_modify_co(self):
        return self.get_value(CoOperation.assert_modiye_co_loc)

    def delete_co(self):
        try:
            self.waite_ele(CoOperation.delete_co_loc)
        except:
            self.refresh_url(CoOperation.operate_url)
        finally:
            sleep(2)
            self.click(CoOperation.delete_co_loc)
            self.click(CoOperation.delete_confirm_loc)














    #页面操作