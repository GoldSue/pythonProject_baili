import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from templat import Base

# 初始化 WebDriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(5)

# 实例化 Base 类
bp = Base(driver)

# 查找并点击新闻链接
news_link_locator = (By.LINK_TEXT, '新闻')
news_link = driver.find_element(*news_link_locator)
news_link.click()
time.sleep(10)

# 查找并滚动到视野链接
vision_link_locator = driver.find_element(By.LINK_TEXT, '视野')
# bp.scroll_into_view(vision_link_locator)  # 确保视野链接可见
time.sleep(1)  # 等待滚动完成

# 再次查找视野链接，确保它现在是可见的


# 检查元素是否可见并点击
if vision_link_locator.is_displayed():
    print(f"Clicking on element: {vision_link_locator.text}")
    vision_link_locator.click()
else:
    print("Element not visible")

# 关闭浏览器
driver.quit()
