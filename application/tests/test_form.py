import pytest
from pages.form_page import FormPage

class TestForm:
    def test_valid_form_submission(self, browser):
        form_page = FormPage(browser)
        valid_data = {'name': 'Test User', 'email': 'test@example.com', 'message': 'Hello!'}
        form_page.fill_form(valid_data)
        form_page.submit_form()
        assert form_page.get_success_message() == 'Form submitted successfully!'

    def test_invalid_form_submission(self, browser):
        form_page = FormPage(browser)
        invalid_data = {'name': '', 'email': 'invalid_email', 'message': ''}
        form_page.fill_form(invalid_data)
        form_page.submit_form()
        assert form_page.get_error_message() == 'Please fill out this field.'
