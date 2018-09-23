from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_id('email')
        except:
            return  None
    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_id('pass')
        except:
            return None
    def get_login_button(self):
        try:
            return  self.driver.find_element_by_id('u_0_8')
        except:
            return None
    def wait_for_login_page_to_load(self):
        wait=WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_css_selector('.clearfix.loggedout_menubar')))