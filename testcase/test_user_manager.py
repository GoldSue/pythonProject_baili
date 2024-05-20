

from base.base_util import BaseUtil
from pages.login_page import LoginPage
from pages.uesr_manage_page import UserManagePage


class TestUserManage(BaseUtil):

    def test_001_add_user(self):
        self.logger.info("执行用例>> 新增用户")
        um = UserManagePage(self.driver)
        um.add_user()
        # self.assertIn("新增完成",um.assert_add())
        self.logger.info("执行成功")

    def test_002_modify_user(self):
        self.logger.info("执行用例>> 修改用户")
        um = UserManagePage(self.driver)
        um.modify_save()
        self.assertIn("修改成功",um.asert_modify())
        self.logger.info("执行成功")

    def test_003_stop(self):
        self.logger.info("执行用例>> 停用用户")
        um = UserManagePage(self.driver)
        um.user_stop()
        self.assertIn("停用成功",um.assert_stop())
        self.logger.info("执行成功")

    def test_004_del(self):
        self.logger.info("执行用例>> 删除用户")
        um = UserManagePage(self.driver)
        um.del_user()
        self.assertIn("用户已删除",um.assert_del())
        self.logger.info("执行成功")

    def test_005_invite_user(self):
        self.logger.info("执行用例>> 邀请用户")
        um = UserManagePage(self.driver)
        um.invite_user()
        # self.assertEqual("邀请发起成功",um.assert_invite())
        self.logger.info("执行成功")

    def test_006_invite_users(self):
        self.logger.info("执行用例>> 批量邀请用户")
        um = UserManagePage(self.driver)
        um.invite_users()
        self.logger.info("执行成功")

    def test_007_add_user_group(self):
        self.logger.info("执行用例>> 新增用户群组")
        um = UserManagePage(self.driver)
        um.add_user_group()
        # self.assertEqual(um.assert_group_save(),"用户群组已新增")
        self.logger.info("执行成功")

    def test_008_modify_group(self):
        self.logger.info("执行用例>> 修改用户群组")
        um = UserManagePage(self.driver)
        um.modify_group()
        # self.assertEqual(um.assert_modify_group("用户群组已修改",um.assert_modify_group_loc),)
        self.logger.info("执行成功")
    def test_009_delete_group(self):
        self.logger.info("执行用例>> 删除用户群组")
        um = UserManagePage(self.driver)
        um.delete_user_group()
        # self.assertEqual(um.assert_delete_user_loc,"用户群组已删除")
        self.logger.info("执行成功")

