import os
import random
import time

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


    def loctor(self,loc,timeout=10):
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
        """
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
        """
        上传文件，调用获取文件路径的方法
        :param filename: 需要上传的文件
        :return:
        """
        pyautogui.write(self.get_file_path(filename))
        time.sleep(1)
        pyautogui.press('enter')
        # pyautogui.press('enter')

    def refresh(self):
        pyautogui.press('f5')
        time.sleep(3)

    def get_screenshot(self,picture):
        self.driver.save_screenshot(f"D:\\pythonProject_baili\\screenshot\\{picture}.png")








