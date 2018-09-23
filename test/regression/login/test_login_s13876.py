import unittest
import json
from lib.ui.login_page import LoginPage
from lib.util import create_driver
class TestLoginS13876(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=LoginPage(self.driver)
        self.data=json.load(open('./test/regression/login/s13876.json'))
    def tearDown(self):
        self.driver.close()
    def test_login_invalid_tc156789(self):
        self.login.wait_for_login_page_to_load()
        actual_title=self.driver.title
        expected_title='Facebook – log in or sign up'
        assert actual_title==expected_title
        self.login.get_username_textbox().send_keys(self.data['username'])
        self.login.get_password_textbox().send_keys(self.data['invalid-pwd'])
        self.login.get_login_button().click()
        actual_err_msg=self.login.get_login_error_msg().text
        expected_err_msg="The password that you've entered is incorrect. " + "Forgotten password?"
        assert actual_err_msg==expected_err_msg