#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/25 8:00
# @Author  : libaojin
# @File    : decorators.py


import logging.config
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functools import wraps
from selenium.webdriver.support.wait import WebDriverWait

# 加载日志配置文件
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def log_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0] if args else None
        if self and hasattr(self, 'logger'):
            self.logger.info(f"开始执行测试用例 {func.__name__}")
        else:
            logger.info(f"开始执行测试用例 of {func.__name__}")

        try:
            return func(*args, **kwargs)
        except Exception as e:
            if self and hasattr(self, 'logger'):
                self.logger.exception(f"发生异常 {func.__name__}")
            else:
                logger.exception(f"发生异常 {func.__name__}")
            raise

    return wrapper


def ensure_page_loaded(element_locator, start_url, timeout=5):
    """
    装饰器：确保页面加载，等待指定元素出现。如果元素未出现，则导航到起始页面。
    :param element_locator: 定位元素的定位器
    :param start_url: 起始页面的URL
    :param timeout: 等待时间（默认5秒）
    """
    def decorator(func):
        @wraps(func)
        def wrapper(page, *args, **kwargs):
            try:
                WebDriverWait(page.driver, timeout).until(
                    EC.presence_of_element_located(element_locator)
                )
                print(f"Element {element_locator} found on the page.")
            except TimeoutException:
                print(f"Element {element_locator} not found, navigating to {start_url}.")
                page.driver.get(start_url)
                try:
                    WebDriverWait(page.driver, timeout).until(
                        EC.presence_of_element_located(element_locator)
                    )
                    print(f"Element {element_locator} found on the start URL page.")
                except TimeoutException:
                    print(f"Element {element_locator} still not found after navigating to start URL.")
            return func(page, *args, **kwargs)
        return wrapper
    return decorator

