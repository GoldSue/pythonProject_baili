import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage


class BaseUtil(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://console-paas.digiwincloud.com.cn/login")
        cls.driver.implicitly_wait(20)
        lp = LoginPage(cls.driver)
        lp.login()
        WebDriverWait(cls.driver, 50).until(EC.url_to_be("https://console-paas.digiwincloud.com.cn/"))



    @classmethod
    def tearDownClass(cls):
        pass