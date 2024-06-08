import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import os
import logging.config

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = os.path.join(current_dir,'logging.conf')


# # 读取日志配置文件
logging.config.fileConfig(log)


class BaseUtil:
    driver = None
    logger = logging.getLogger('fileAndConsole')

    @classmethod
    def setup_class(cls):
        cls.logger = BaseUtil.logger
        cls.driver = webdriver.Chrome()
        cls.logger.info("开始执行前置操作")
        cls.driver.maximize_window()
        cls.driver.get("https://console-paas.digiwincloud.com.cn/login")
        cls.driver.implicitly_wait(10)
        lp = LoginPage(cls.driver)
        lp.login()
        WebDriverWait(cls.driver, 20).until(EC.url_to_be("https://console-paas.digiwincloud.com.cn/"))

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        cls.driver.quit()