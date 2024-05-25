from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def loctor(self, loc):
        """
        定位元素的方法
        :param loc: 元素定位器，例如 (By.ID, "element_id")
        :return: Web 元素
        """
        return self.driver.find_element(*loc)

    def scroll_into_view(self, loc):
        """
        滚动到元素可见
        :param loc: 元素定位器
        :return: None
        """
        try:
            element = self.loctor(loc)
            if element:
                print(f"Scrolling into view: {element.text if element.text else 'element with locator ' + str(loc)}")  # 调试日志
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                print("Executed scrollIntoView script")  # 调试日志
            else:
                print("Element not found")  # 调试日志
        except Exception as e:
            print(f"Exception occurred: {e}")
