import random

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_autoinstaller.install()


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def loctor(self,loc,timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(
                EC.element_to_be_clickable(loc)
            )
            return element
        except TimeoutException:
            print(f"元素定位超时了，是这个{loc}")
            return None
        except Exception as e:
            print(f"元素可能不可交互或者页面未刷新出来，是这个{loc}")
            print(e)
            return None

    def send_keys(self,loc,value,timeout=10):
        element = self.loctor(loc,timeout)
        element.send_keys(value)

    def click(self,loc,timeout=10):
        element = self.loctor(loc,timeout)
        element.click()

    def get_value(self,loc,timeout=10):
        element = self.loctor(loc,timeout)
        return element.text

    def clear(self,loc):
        ele = self.loctor(loc)
        ele.send_keys(Keys.CONTROL + "a")
        ele.send_keys(Keys.DELETE)

    def get_url(self):
        return self.driver.current_url

    def perform_action(self, action):
        action.perform()

    def action_click(self, loc,timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(loc))
        action = ActionChains(self.driver)
        action.click(element)
        self.perform_action(action)

    def action_send_keys(self, locator, value,timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).click().send_keys(value)
        self.perform_action(action)

    def random(self):
        ele = str(random.randrange(1000000, 9999999))
        lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        A = random.choice(lis)
        ran = "A" + A + ele
        return ran





