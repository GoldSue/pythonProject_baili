



import unittest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep





class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def test_window(self):
        # ele = self.driver.find_element(By.ID, 'kw')


        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.ID,'su').click()
        sleep(2)
        js3 = "window.scrollTo(0,1000)"
        self.driver.execute_script(js3)

        # self.driver.execute_script("window.scrollBy(0,3000;")
        sleep(5)

        # ele.send_keys(Keys.CONTROL,"x")
        # sleep(1)
        # ele.send_keys(Keys.CONTROL,"v")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





