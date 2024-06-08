#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/20 21:57
# @Author  : libaojin
# @File    : test_co_operate.py
import unittest

import pytest

from base.base_util import BaseUtil
from decorators import log_exceptions
from pages.co_manage import CoOperation


class TestCoOperate(BaseUtil):
    @log_exceptions
    def test_001_add_co(self):
        co = CoOperation(self.driver)
        co.add_co()
        result = co.assert_add_co()
        assert "新增成功" == result, f"断言失败：期望包含 '新增成功'，实际返回 '{result}'"

    @log_exceptions
    def test_002_modify_co(self):
        co = CoOperation(self.driver)
        co.modify_co()
        result = co.assert_modify_co()
        assert"修改成功" == result, f"断言失败：期望包含 '修改成功'，实际返回 '{result}'"

    @log_exceptions
    def test_003_delete_co(self):
        co = CoOperation(self.driver)
        co.delete_co()

    @log_exceptions
    def test_004_add_employee(self):
        co = CoOperation(self.driver)
        co.add_employee()
        result = co.assert_add_employee()
        assert "新增成功"  == result, f"断言失败：期望包含 '新增成功'，实际返回 '{result}'"

    @log_exceptions
    def test_005_modify_employee(self):
        co = CoOperation(self.driver)
        co.midify_employee()
        result = co.assert_modify_employee()
        assert "修改成功" in result, f"断言失败：期望包含 '修改成功'，实际返回 '{result}'"

    @log_exceptions
    def test_006_stop_employee(self):
        co = CoOperation(self.driver)
        co.stop_employee()
        result = co.assert_stop_employee()
        assert "停用成功" in result, f"断言失败：期望包含 '停用成功'，实际返回 '{result}'"

    @log_exceptions
    def test_007_delete_employee(self):
        co = CoOperation(self.driver)
        co.delete_employee()
        result = co.assert_delete_employee()
        assert "删除成功" in result, f"断言失败：期望包含 '删除成功'，实际返回 '{result}'"

    @log_exceptions
    def test_008_export_employ(self):
        co = CoOperation(self.driver)
        co.export_employee()
        result = co.assert_export()
        assert  "导入成功"  in result, f"断言失败：期望包含 '导入成功'，实际返回 '{result}'"

    @log_exceptions
    def test_008_import_employee(self):
        co = CoOperation(self.driver)
        co.import_employee()

    # @log_exceptions
    # def test_009_add_dep(self):
    #     co = CoOperation(self.driver)
    #     co.add_dep()
        # result = co.assert_add_dep()
        # self.assertIn("新增成功", result, msg=f"断言失败：期望包含 '新增成功'，实际返回 '{result}'")

    @log_exceptions
    def test_010_add_site(self):
        co = CoOperation(self.driver)
        co.add_sit()
        result = co.assert_site()
        assert "新增成功" in result,f"断言失败：期望包含 '新增成功'，实际返回 '{result}'"

    @log_exceptions
    def test_011_modify_site(self):
        co = CoOperation(self.driver)
        co.modify_site()
        result = co.assert_modify()
        assert "修改成功" in result, f"断言失败：期望包含 '修改成功'，实际返回 '{result}'"

    @log_exceptions
    def test_012_delete_site(self):
        co = CoOperation(self.driver)
        co.delete_site()
        result = co.assert_delet()
        assert "删除成功" in result, f"断言失败：期望包含 '删除成功'，实际返回 '{result}'"

