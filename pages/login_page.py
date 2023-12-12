from pages.main_page import MainPage
from constants.locators import LoginPageLocators, HeaderLocators
from constants import login_data, page_names


class LoginPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.open_page(login_data.LOGIN_PAGE_URL)

    def is_login_page(self):
        if self.browser.current_url == login_data.LOGIN_PAGE_URL:
            return True
        return False

    def is_login_forms_exists(self):
        if all([self.is_element_presented(LoginPageLocators.USERNAME_FIELD),
                self.is_element_presented(LoginPageLocators.PASSWORD_FIELD),
                self.is_element_presented(LoginPageLocators.LOGIN_BUTTON)]):
            return True
        return False

    def login(self, username, password):
        self.enter_text(LoginPageLocators.USERNAME_FIELD, username)
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def landing_page_name(self):
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.PRODUCTS_PAGE:
            return True
        return False

    def error_message_exists(self):
        if self.is_element_presented(LoginPageLocators.ERROR_MESSAGE):
            return True
        return False

    def get_error_message_text(self):
        if self.error_message_exists():
            return self.get_element_text(LoginPageLocators.ERROR_MESSAGE)
        return None

    def login_as_standard_user(self):
        self.login(username=login_data.STANDARD_USER, password=login_data.STANDARD_PASSWORD)

    def clear_login_form(self):
        self.find_element(LoginPageLocators.USERNAME_FIELD).clear()
        self.find_element(LoginPageLocators.PASSWORD_FIELD).clear()
        self.login_form_is_cleared()

    def login_form_is_cleared(self):
        assert self.input_box_is_empty(LoginPageLocators.USERNAME_FIELD)
        assert self.input_box_is_empty(LoginPageLocators.PASSWORD_FIELD)