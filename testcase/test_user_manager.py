import pytest

from base.base_util import BaseUtil
from decorators import log_exceptions
from pages.login_page import LoginPage
from pages.uesr_manage_page import UserManagePage


class TestUserManage(BaseUtil):
    @log_exceptions
    def test_001_add_user(self):
        um = UserManagePage(self.driver)
        um.add_user()
        result = um.assert_add()
        assert "新增成功" == result,f"期望 ‘新增成功’，实际{result}"

    @log_exceptions
    def test_002_modify_user(self):
        um = UserManagePage(self.driver)
        um.modify_save()
        result = um.asert_modify()
        assert "修改成功" in result, f"期望 ‘修改成功’，实际{result}"

    @log_exceptions
    def test_003_stop(self):
        um = UserManagePage(self.driver)
        um.user_stop()
        result = um.assert_stop()
        assert "停用成功" in result, f"期望 ‘停用成功’，实际{result}"

    @log_exceptions
    def test_004_del(self):
        um = UserManagePage(self.driver)
        um.del_user()
        result = um.assert_del()
        assert "用户已删除" == result, f"期望 ‘用户已删除’，实际{result}"

    @log_exceptions
    def test_005_invite_user(self):
        um = UserManagePage(self.driver)
        um.invite_user()
        result = um.assert_invite()
        assert "邀请发起成功" in result, f"期望 ‘邀请发起成功’，实际{result}"

    @log_exceptions
    def test_006_invite_users(self):
        um = UserManagePage(self.driver)
        um.invite_users()

    @log_exceptions
    def test_007_add_user_group(self):
        um = UserManagePage(self.driver)
        um.add_user_group()
        result = um.assert_group_save()
        assert "用户群组已新增" == result, f"期望 ‘用户群组已新增’，实际{result}"

    @log_exceptions
    def test_008_modify_group(self):
        um = UserManagePage(self.driver)
        um.modify_group()
        result = um.assert_modify_group()
        assert "用户群组已修改" == result, f"期望 ‘用户群组已修改’，实际{result}"

    @log_exceptions
    def test_009_delete_group(self):
        um = UserManagePage(self.driver)
        um.delete_user_group()
        result = um.assert_del_user()
        assert "用户群组已删除" == result, f"期望 ‘用户群组已删除’，实际{result}"



