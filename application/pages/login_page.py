from .base_page import BasePage

class LoginPage(BasePage):
    def enter_username(self, username):
        self.input_text('username_field_locator', text=username)

    def enter_password(self, password):
        self.input_text('password_field_locator', text=password)

    def click_login(self):
        self.click('login_button_locator')

    def get_error_message(self):
        return self.find_element('error_message_locator').text
