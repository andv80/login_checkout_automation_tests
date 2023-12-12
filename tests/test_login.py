import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from constants import login_data as LD


@pytest.mark.usefixtures("browser")
class TestLogin:
    @pytest.mark.parametrize("username", [LD.STANDARD_USER, LD.PROBLEM_USER, LD.ERROR_USER,
                                          LD.PERFORMANCE_GLITCH_USER, LD.VISUAL_USER])
    @pytest.mark.parametrize("password", [LD.STANDARD_PASSWORD])
    def test_login_with_valid_credentials(self, username, password):
        login_page = LoginPage(self.browser)
        assert login_page.is_login_page()
        assert login_page.is_login_forms_exists()
        login_page.login(username=username, password=password)
        assert not login_page.error_message_exists()
        products_page = ProductsPage(self.browser)
        assert products_page.is_product_page()
        products_page.burger_menu.make_logout()

    @pytest.mark.parametrize("username, password, error", [
        (LD.EMPTY_USERNAME, LD.EMPTY_PASSWORD, LD.EMPTY_PASSWORD_AND_USERNAME_ERROR),
        (LD.EMPTY_USERNAME, LD.STANDARD_PASSWORD, LD.EMPTY_USERNAME_ERROR),
        (LD.STANDARD_USER, LD.EMPTY_PASSWORD, LD.EMPTY_PASSWORD_ERROR),
        (LD.STANDARD_USER, LD.NON_EXISTING_PASSWORD, LD.NON_VALID_CREDENTIALS_ERROR),
        (LD.NON_EXISTING_USER, LD.STANDARD_PASSWORD, LD.NON_VALID_CREDENTIALS_ERROR),
        (LD.NON_EXISTING_USER, LD.NON_EXISTING_PASSWORD, LD.NON_VALID_CREDENTIALS_ERROR)])
    def test_login_with_invalid_credentials(self, username, password, error):
        login_page = LoginPage(self.browser)
        login_page.login(username=username, password=password)
        assert login_page.error_message_exists()
        assert login_page.get_error_message_text() == error
        assert login_page.is_login_page()
        login_page.clear_login_form()

    def test_login_as_locked_out_user(self):
        login_page = LoginPage(self.browser)
        login_page.login(username=LD.LOCKED_OUT_USER, password=LD.STANDARD_PASSWORD)
        assert login_page.error_message_exists()
        assert login_page.get_error_message_text() == LD.LOCKED_OUT_ERROR
        assert login_page.is_login_page()
        login_page.clear_login_form()
