

from base.base_util import BaseUtil
from page.login_page import LoginPage
from page.uesr_manage_page import UserManagePage


class TestUserManage(BaseUtil):

    def test_001_add_user(self):
        um = UserManagePage(self.driver)
        um.add_user()
        self.assertIn("新增完成",um.assert_add())

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

    def test_005_invite_user(self):
        um = UserManagePage(self.driver)
        um.invite_user()
        # self.assertEqual("邀请发起成功",um.assert_invite())

    def test_006_invite_users(self):
        um = UserManagePage(self.driver)
        um.invite_users()

    def test_007_add_user_group(self):
        um = UserManagePage(self.driver)
        um.add_user_group()
        # self.assertEqual(um.assert_group_save(),"用户群组已新增")

    def test_008_modify_group(self):
        um = UserManagePage(self.driver)
        um.modify_group()
        # self.assertEqual(um.assert_modify_group("用户群组已修改",um.assert_modify_group_loc),)




