from selenium import webdriver
import pytest
from Utilities.readproperties import Readconfig

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_scenarios(BaseTest):
    @pytest.mark.parametrize("username, password",
                             [
                                 ("standard_user", "secret_sauce"),
                                 ("problem_user", "secret_sauce"),
                                 ("performance_glitch_user", "secret_sauce")
                             ]
                             )
    def test_login_parametrize(self, username, password):
        assert self.driver.title == "Swag Labs"
        self.driver.find_element_by_id("user-name").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login-button").click()
        self.driver.find_element_by_xpath("//*[@id='react-burger-menu-btn']").click()
        self.driver.find_element_by_xpath("//*[@id='logout_sidebar_link']").click()

    def test_login_data(self):
        self.driver.find_element_by_id("user-name").send_keys('username')
        self.driver.find_element_by_id("password").send_keys('password')
        self.driver.find_element_by_id("login-button").click()
        # return homepage(self.driver)

    def test_home_data(self):
        pass
