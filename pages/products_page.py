from pages.main_page import MainPage
from constants.locators import ProductPageLocators, HeaderLocators
from constants import page_names


class ProductsPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_product_page(self):
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.PRODUCTS_PAGE:
            return True
        return False

    def item_to_add_to_cart(self):
        items = self.browser.find_elements(*ProductPageLocators.INVENTORY_ITEM)
        for element in items:
            if self.is_child_element_exists(element, HeaderLocators.ADD_TO_CART):
                return element
        return False


