from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def open_page(self, url):
        self.browser.get(url)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return self.browser.find_element(*by_locator).text

    def is_element_presented(self, by_locator):
        try:
            self.browser.find_element(*by_locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def find_element(self, by_locator):
        if self.is_element_presented(by_locator):
            return self.browser.find_element(*by_locator)

    def is_child_element_exists(self, parent, child_locator):
        try:
            parent.find_element(*child_locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def input_box_is_empty(self, by_locator):
        element = self.find_element(by_locator)
        value = element.get_attribute('value')
        if value == '':
            return True
        return False
