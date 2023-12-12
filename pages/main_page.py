from pages.base_page import BasePage
from constants.locators import LoginPageLocators, HeaderLocators, BurgerMenuLocators
from constants import page_names


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.header = Header(browser)
        self.burger_menu = BurgerMenu(browser)

    @staticmethod
    def add_item_to_cart(item):
        button = item.find_element(*HeaderLocators.ADD_TO_CART)
        button.click()

    @staticmethod
    def format_price(price):
        sep = '$'
        stripped = price.split(sep, 1)[1]
        return float(stripped)

    def get_item_details(self, *items):
        details_list = []
        for item in items:
            name = item.find_element(*HeaderLocators.ITEM_NAME).text
            description = item.find_element(*HeaderLocators.ITEM_DESC).text
            price = self.format_price(item.find_element(*HeaderLocators.ITEM_PRICE).text)
            details_list.append([name, description, price])
        return details_list


class Header(BasePage):
    def is_cart_bage_exists(self):
        if self.is_element_presented(HeaderLocators.CART_BADGE):
            return True
        return False

    def get_number_of_items_on_badge(self):
        if self.is_cart_bage_exists():
            return int(self.get_element_text(HeaderLocators.NUMBER_OF_ITEMS_ON_BADGE))
        return 0

    def go_to_cart_page(self):
        self.click(HeaderLocators.CART)
        if self.get_element_text(HeaderLocators.PAGE_TITLE) == page_names.YOUR_CART_PAGE:
            return True
        return False


class BurgerMenu(BasePage):
    def make_logout(self):
        self.click(BurgerMenuLocators.BURGER_MENU)
        self.click(BurgerMenuLocators.LOGOUT_BUTTON)
