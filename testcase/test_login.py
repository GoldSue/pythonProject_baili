import time
import unittest
import chromedriver_autoinstaller
from selenium import webdriver
from ddt import ddt, data
from common.excel_util import ExcelUtil
from page.login_page import LoginPage
chromedriver_autoinstaller.install()
from ddt import ddt, data,unpack

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://console-paas.digiwincloud.com.cn/login")

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    @data(*ExcelUtil().read_excel())
    @unpack
    def test_001_login(self,index,username,password):
        print(index,username,password)
        # username, password = login_data
        lp = LoginPage(self.driver)
        lp.login(username,password)
        if index==1:
            self.assertEqual(lp.assert_right(), "资讯主页")
        # elif index==2:
        #     self.assertIn("账户或密码错误",lp.assert_wrong_password())
        else:
            self.assertIn("账户或密码错误",lp.assert_wrong_username())
        time.sleep(6)




        # time.sleep(50)
        #


