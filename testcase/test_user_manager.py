

from base.base_util import BaseUtil
from page.login_page import LoginPage
from page.uesr_manage_page import UserManagePage


class TestUserManage(BaseUtil):

    def test_001_add_user(self):
        um = UserManagePage(self.driver)
        um.add_user()
        self.assertIn("新增完成",um.assert_complet())

    def test_002_modify_user(self):
        um = UserManagePage(self.driver)
        um.modify_save()
        self.assertIn("修改成功",um.asert_modify())

    def test_003_stop(self):
        um = UserManagePage(self.driver)
        um.user_stop()
        self.assertIn("停用成功",um.assert_stop())

    def test_004_del(self):
        um = UserManagePage(self.driver)
        um.del_user()
        self.assertIn("用户已删除",um.assert_del())
