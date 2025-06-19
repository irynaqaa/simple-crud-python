import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.enter_username('valid_user')
        login_page.enter_password('valid_password')
        login_page.click_login()
        assert browser.current_url == 'expected_url_after_login'

    def test_unsuccessful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.enter_username('invalid_user')
        login_page.enter_password('invalid_password')
        login_page.click_login()
        assert login_page.get_error_message() == 'Expected error message'
