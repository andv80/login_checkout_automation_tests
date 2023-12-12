from pages.main_page import MainPage
from constants.locators import CheckoutOverviewLocators, HeaderLocators
from constants import page_names


class CheckoutOverview(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_overview_page(self):
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.CHECKOUT_OVERVIEW_PAGE:
            return True
        return False

    def get_items_on_page(self):
        items = self.browser.find_elements(*CheckoutOverviewLocators.CART_ITEM)
        return list(item for item in items)

    def submit_overview_page(self):
        self.click(CheckoutOverviewLocators.FINISH_BUTTON)

    def overview_page_is_submitted(self):
        if not self.is_overview_page():
            return True
        return False

    def get_tax_amount(self):
        tax = self.get_element_text(CheckoutOverviewLocators.TAX_AMOUNT)
        return float(self.format_price(tax))

    def get_subtotal_amount(self):
        subtotal = self.get_element_text(CheckoutOverviewLocators.SUMMARY_SUBTOTAL_AMOUNT)
        return self.format_price(subtotal)

    def get_total_amount(self):
        total = self.get_element_text(CheckoutOverviewLocators.TOTAL_AMOUNT)
        return self.format_price(total)

    def get_price_of_all_items_on_page(self):
        amount = 0
        items = self.get_items_on_page()
        for item in items:
            amount += self.format_price(item.find_element(*HeaderLocators.ITEM_PRICE).text)
        return amount






