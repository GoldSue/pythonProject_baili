


# import random
#
# ele = str(random.randrange(1000000,9999999))
# lis = ['a','b','c','d','e','f','g','h','i','j']
# A = random.choice(lis)
# print("A" + A + ele)
import os
import random

import selenium
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# chromedriver_autoinstaller.install()

import configparser
import os
import platform


    # __file__获取当前这个文件的文件名
    # os.path.abspath(__file__)获取当前文件的绝对路径，路径包含文件名
    # os.path.dirname(os.path.abspath(__file__))获取当前文件的绝对路径，不包含文件名
    # 然后拼接上db.ini文件名，即可获得db.ini的绝对路径
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
















