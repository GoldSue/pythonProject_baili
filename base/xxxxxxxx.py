


# import random
#
# ele = str(random.randrange(1000000,9999999))
# lis = ['a','b','c','d','e','f','g','h','i','j']
# A = random.choice(lis)
# print("A" + A + ele)


import random

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_autoinstaller.install()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
url = driver.current_url
print(url)




