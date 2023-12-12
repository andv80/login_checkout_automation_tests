from selenium.webdriver.common.by import By


class HeaderLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, '.header_container .title')
    CART = (By.CSS_SELECTOR, '.primary_header .shopping_cart_link')
    CART_BADGE = (By.CSS_SELECTOR, '.primary_header .shopping_cart_badge')
    ITEM_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    ITEM_DESC = (By.CSS_SELECTOR, '.inventory_item_desc')
    ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price ')
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn_primary')
    NUMBER_OF_ITEMS_ON_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')


class BurgerMenuLocators:
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message-container.error')
    ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, 'div.error-message-container.error h3')


class ProductPageLocators:
    INVENTORY_LIST = (By.CSS_SELECTOR, '.inventory_list')
    INVENTORY_ITEM = (By.CSS_SELECTOR, '.inventory_item')
    REMOVE = (By.CSS_SELECTOR, '.btn_secondary')


class YourCartLocators:
    REMOVE = (By.CSS_SELECTOR, '.btn_secondary')
    CART_LIST = (By.CSS_SELECTOR, '.cart_list')
    CART_ITEM = (By.CSS_SELECTOR, '.cart_item')
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, '.back.btn_medium')
    CHECKOUT = (By.CSS_SELECTOR, '.btn_medium.checkout_button')


class CheckoutLocators:
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_FIELD = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, 'cancel')
    CONTINUE_BUTTON = (By.ID, "continue")


class CheckoutOverviewLocators:
    CART_LIST = (By.CSS_SELECTOR, '.cart_list')
    CART_ITEM = (By.CSS_SELECTOR, '.cart_item')
    CANCEL_BUTTON = (By.ID, 'cancel')
    FINISH_BUTTON = (By.ID, 'finish')
    SUMMARY_SUBTOTAL_AMOUNT = (By.CSS_SELECTOR, '.summary_subtotal_label')
    TAX_AMOUNT = (By.CSS_SELECTOR, '.summary_tax_label')
    TOTAL_AMOUNT = (By.CSS_SELECTOR, '.summary_info_label.summary_total_label')


class CheckoutCompleteLocators:
    COMPLETE_MESSAGE = (By.CSS_SELECTOR, '.complete-header')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')





