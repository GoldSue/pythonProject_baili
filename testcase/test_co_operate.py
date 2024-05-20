#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/20 21:57
# @Author  : libaojin
# @File    : test_co_operate.py
import unittest

from base.base_util import BaseUtil
from pages.co_manage import CoOperation


class TestCoOperate(BaseUtil):

    def test_001_add_co(self):
        self.logger.info("执行用例>> 新增企业")
        co = CoOperation(self.driver)
        co.add_co()
        result = co.assert_add_co()
        try:
            self.assertEqual("新增成功", result, msg=f"断言失败：期望包含 '新增成功'，实际返回 '{result}'")
            self.logger.info("断言成功")
        except AssertionError as e:
            self.logger.error(e)
            raise

    def test_002_modify_co(self):
        self.logger.info("执行用例>> 修改企业")
        co = CoOperation(self.driver)
        co.modify_co()
        result = co.assert_modify_co()
        try:
            self.assertEqual("修改成功", result, msg=f"断言失败：期望包含 '修改成功'，实际返回 '{result}'")
            self.logger.info("断言成功")
        except AssertionError as e:
            self.logger.error(e)
            raise

    def test_003_delete_co(self):
        self.logger.info("执行用例>> 删除企业")
        co = CoOperation(self.driver)
        co.delete_co()
        self.logger.info("执行成功")
