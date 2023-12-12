from pages.main_page import MainPage
from constants.locators import CheckoutLocators, HeaderLocators
from constants import page_names


class CheckoutPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_checkout_page(self):
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.CHECKOUT_PAGE:
            return True
        return False

    def checkout_form_exists(self):
        if all([self.is_element_presented(CheckoutLocators.FIRST_NAME_FIELD),
                self.is_element_presented(CheckoutLocators.LAST_NAME_FIELD),
                self.is_element_presented(CheckoutLocators.ZIP_FIELD)]):
            return True
        return False

    def submit_checkout_form(self):
        if self.checkout_form_exists():
            self.enter_text(CheckoutLocators.FIRST_NAME_FIELD, 'FirstName')
            self.enter_text(CheckoutLocators.LAST_NAME_FIELD, 'LastName')
            self.enter_text(CheckoutLocators.ZIP_FIELD, '12345')
            self.click(CheckoutLocators.CONTINUE_BUTTON)

    def checkout_page_is_submitted(self):
        if not self.is_checkout_page():
            return True
        return False

