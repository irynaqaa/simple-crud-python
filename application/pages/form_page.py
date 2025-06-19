from .base_page import BasePage

class FormPage(BasePage):
    def fill_form(self, data):
        self.input_text('name_field_locator', text=data['name'])
        self.input_text('email_field_locator', text=data['email'])
        self.input_text('message_field_locator', text=data['message'])

    def submit_form(self):
        self.click('submit_button_locator')

    def get_success_message(self):
        return self.find_element('success_message_locator').text

    def get_error_message(self):
        return self.find_element('error_message_locator').text
