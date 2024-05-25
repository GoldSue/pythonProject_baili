#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/25 8:00
# @Author  : libaojin
# @File    : decorators.py

import logging
import logging
import logging.config
from functools import wraps

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
