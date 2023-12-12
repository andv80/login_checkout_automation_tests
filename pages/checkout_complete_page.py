from pages.main_page import MainPage
from constants.locators import CheckoutCompleteLocators, HeaderLocators
from constants import page_names


class CheckoutCompletePage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_checkout_complete_page(self):
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.CHECKOUT_COMPLETE:
            return True
        return False

    def successful_banner_is_displayed(self):
        return self.is_element_presented(CheckoutCompleteLocators.COMPLETE_MESSAGE)

    def get_successful_banner_message(self):
        return self.get_element_text(CheckoutCompleteLocators.COMPLETE_MESSAGE)
