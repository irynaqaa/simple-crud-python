import pytest
from utils.data_reader import DataReader

@pytest.mark.parametrize('username,password', DataReader.read_csv('path_to_csv_file'))
def test_login_with_data(browser, username, password):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    assert browser.current_url == 'expected_url_after_login'
