import os
import random
from time import sleep

import pyautogui
from selenium import webdriver
import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging.config


current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = os.path.join(current_dir,'logging.conf')
logging.config.fileConfig(log)


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger('fileAndConsole')

    def loctor(self,loc,timeout=5):
        """
        定位元素的方法，加入显示等待和try异常返回，一般用来定位到元素来进行下一步操作
        :param loc: 元素定位
        :param timeout: 显示等待时间
        :return: 返回定位到的元素
        """
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.element_to_be_clickable(loc)
            )

            return element
        except TimeoutException:
            self.logger.error(f"元素定位超时了，是这个{loc}")
            return None

        except Exception as e:
            self.logger.error(f"元素可能不可交互或未加载出，是这个{loc}")
            self.logger.error(e)
            return None

    def waite_ele(self,loc,timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(loc)
        )

    def send_keys(self,loc,value,timeout=10):
        element = self.loctor(loc,timeout)
        element.send_keys(value)

    def clear_input(self,loc,value,timeout=5):
        sleep(1)
        self.clear(loc)
        sleep(1)
        element = self.loctor(loc, timeout)
        element.send_keys(value)

    def click(self,loc,timeout=10):
        element = self.loctor(loc,timeout)
        element.click()

    def get_value(self,loc,timeout=10):
        """
        获取元素文本值，一般用来断言
        :param loc: 元素定位
        :param timeout: 显示等待时间
        :return:返回获取文本
        """
        element = self.loctor(loc,timeout)
        return element.text

    def clear(self,loc):
        """
        使用Keys库类模拟键盘操作，CONTROL+a全选并删除
        :param loc: 元素定位，文本框
        :return:
        # """
        # self.loctor(loc).clear()
        ele = self.loctor(loc)
        ele.send_keys(Keys.CONTROL + "a")
        ele.send_keys(Keys.DELETE)

    def get_url(self):
        """
        获取当前页面url,一般用来判断是否跳转到预期页面，来进行下一步操作
        :return: 返回当前页面url
        """
        return self.driver.current_url

    def perform_action(self, action):
        action.perform()

    def action_click(self, loc,timeout=10):
        """
        模拟用户点击操作
        :param loc: 元素定位
        :param timeout: 显示等待超时时间
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(loc))
        action = ActionChains(self.driver)
        action.click(element)
        self.perform_action(action)

    def action_send_keys(self, locator, value,timeout=10):
        """
        模拟用户输入文本
        :param locator: 元素定位
        :param value: 输入值
        :param timeout: 显示等待时间
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().send_keys(value)
        self.perform_action(action)

    def random(self):
        """
        获取随机数，首位为大写A，中间随机一位英文小写，后面7位随机数字
        一般用来作创建账号测试数据
        :return: 返回一个字符串比如：Ab6778567
        """
        ele = str(random.randrange(1000000, 9999999))
        lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        A = random.choice(lis)
        ran = "A" + A + ele
        return ran

    def get_file_path(self,filename):
        """
        获取文件路径，默认获取data里的文件
        :param filename:完整的文件名，比如：account_invite.xlsx
        :return:返回文件完整的绝对路径
        """
        current_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dir = os.path.join(current_file_dir, "data")
        filePath = os.path.join(dir, filename)
        return filePath

    def upload_file(self,filename):

        try:
            # self.logger.info("开始上传文件: %s", filename)
            file_path = self.get_file_path(filename)
            # self.logger.info("文件路径: %s", file_path)
            # self.logger.info("输入文件路径到系统文件选择窗口")
            pyautogui.typewrite(file_path, interval=0.05)
            # self.logger.info("文件路径已输入")
            sleep(1)
            # self.logger.info("按下回车键确认上传")
            pyautogui.press('enter',2)
            # self.logger.info("文件上传完成")
        except Exception as e:
            self.logger.exception("文件上传过程中发生错误: %s", str(e))
        # 确保文件上传完成，必要时可以增加一些等待时间

    def refresh(self):
        pyautogui.press('f5')
        sleep(3)

    def get_screenshot(self,picture):
        self.driver.save_screenshot(f"D:\\pythonProject_baili\\screenshot\\{picture}.png")

    def refresh_url(self,url):
        self.driver.get(url)

    def scroll_into_view(self, loc):
        """
        滚动到元素可见
        :param loc:
        :return:
        """
        element = self.loctor(loc)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)


    def get_title(self):
        """
        获取页面标题
        :return:
        """
        return self.driver.execute_script("return document.title;")

    def lose_point(self, loc=None):
        if loc:
            element = self.loctor(loc)
        else:
            element = self.driver.find_element(By.TAG_NAME, 'body')
        self.driver.execute_script("arguments[0].blur();", element)

    def remove_element_attribute(self, loc, attribute="readonly"):
        """
        移除元素属性
        :param loc:
        :param attribute:
        :return:
        """
        element = self.loctor(loc)
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", element, attribute)

    def highlight_element(self, loc):
        """
        元素高亮
        :param loc: 元素定位
        :return:
        """
        element = self.loctor(loc)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

    def click_element_by_js(self, loc):
        """
        execute_script方法点击元素
        :param loc: 元素定位
        :return:
        """
        element = self.loctor(loc)
        self.driver.execute_script("arguments[0].click();", element)











