from pages.main_page import MainPage
from constants.locators import YourCartLocators, HeaderLocators
from constants import page_names


class CartPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_cart_page(self):
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.YOUR_CART_PAGE:
            return True
        return False

    def get_number_of_items(self):
        items = self.browser.find_elements(*YourCartLocators.CART_ITEM)
        return len(items)

    def get_items_on_cart(self):
        items = self.browser.find_elements(*YourCartLocators.CART_ITEM)
        return list(item for item in items)

    def submit_cart_page(self):
        self.click(YourCartLocators.CHECKOUT)

    def cart_page_is_submitted(self):
        if not self.is_cart_page():
            return True
        return False






