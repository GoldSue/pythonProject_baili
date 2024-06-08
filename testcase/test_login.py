import os
import logging.config
import pytest
from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller
from common.excel_util import ExcelUtil
from pages.login_page import LoginPage

# 安装 ChromeDriver
chromedriver_autoinstaller.install()

# 获取当前目录并配置日志
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_config_path = os.path.join(current_dir, 'logging.conf')

# 配置日志
if os.path.exists(log_config_path):
    logging.config.fileConfig(log_config_path)
else:
    logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('fileAndConsole')


@pytest.fixture(scope="function")
def setup_teardown():
    logger.info("测试登录前置操作")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://console-paas.digiwincloud.com.cn/login")
    yield driver
    sleep(2)
    driver.quit()


@pytest.mark.parametrize("index,username,password", ExcelUtil().read_excel())
def test_login(setup_teardown, index, username, password):
    driver = setup_teardown
    logger.info(f"用户名: {username} 密码: {password}")
    lp = LoginPage(driver)
    lp.login(username, password)

    if index == 1:
        assert lp.assert_right() == "我的首页", f"断言失败：期望 '我的首页'，实际 '{lp.assert_right()}'"
    elif index == 2:
        assert "账户或密码错误" in lp.assert_wrong_password(), f"断言失败：期望包含 '账户或密码错误'，实际 '{lp.assert_wrong_password()}'"
    else:
        assert "账户或密码错误" in lp.assert_wrong_username(), f"断言失败：期望包含 '账户或密码错误'，实际 '{lp.assert_wrong_username()}'"
