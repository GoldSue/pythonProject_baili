from time import sleep
import unittest
import chromedriver_autoinstaller
from selenium import webdriver
from ddt import ddt, data
from common.excel_util import ExcelUtil
from decorators import log_exceptions
from pages.login_page import LoginPage
chromedriver_autoinstaller.install()
from ddt import ddt, data,unpack
import os

import logging.config
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = os.path.join(current_dir,'logging.conf')

@ddt
class TestLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://console-paas.digiwincloud.com.cn/login")
        self.logger = logging.getLogger('fileAndConsole')
        self.logger.info("测试登录前置操作")


    @data(*ExcelUtil().read_excel())
    @unpack
    def test_login(self,index,username,password):
        lp = LoginPage(self.driver)
        lp.login(username, password)

        self.logger.info(f"用户名:{username} 密码:{password}")
        if index == 1:
            self.assertEqual(lp.assert_right(), "我的首页")
        elif index == 2:
            self.assertIn("账户或密码错误",lp.assert_wrong_password())
        else :
            self.assertIn("账户或密码错误",lp.assert_wrong_username())

    def tearDown(self):
        sleep(2)
        self.driver.quit()





        # time.sleep(50)
        #


