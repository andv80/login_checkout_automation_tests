import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverview


@pytest.mark.usefixtures("browser")
class TestProducts:
    @pytest.mark.usefixtures("login_as_standard_user")
    def test_add_some_items_to_cart(self):
        """this test validates that some items can be added to the cart
        cart badge shows valid number of added items
        added items are displayed on the cart page shows and their price, names, description are valid"""
        products_page = self.post_login_page
        assert products_page.is_product_page()
        # find first item to add to card
        first_item = products_page.item_to_add_to_cart()
        products_page.add_item_to_cart(first_item)
        assert products_page.header.get_number_of_items_on_badge() == 1
        # find second item to add to card
        second_item = products_page.item_to_add_to_cart()
        products_page.add_item_to_cart(second_item)
        assert products_page.header.get_number_of_items_on_badge() == 2
        # save items price, name, description in item_details var
        item_details = products_page.get_item_details(first_item, second_item)
        products_page.header.go_to_cart_page()
        cart_page = CartPage(self.browser)
        assert cart_page.is_cart_page()
        assert cart_page.get_number_of_items() == 2
        # get items on the cart page
        items_on_cart = cart_page.get_items_on_cart()
        # validate items price, name, description on cart_page corresponds to items selected
        assert item_details == cart_page.get_item_details(*items_on_cart)
        # make sure user can submit cart_page
        cart_page.submit_cart_page()
        assert cart_page.cart_page_is_submitted()

    @pytest.mark.depends(on=['test_add_some_items_to_cart'])
    def test_fill_in_checkout_form(self):
        """this test validates checkout form is presented
        user can fill in submission form and proceed to the checkout overview page"""
        checkout_page = CheckoutPage(self.browser)
        assert checkout_page.is_checkout_page()
        assert checkout_page.checkout_form_exists()
        checkout_page.submit_checkout_form()
        assert checkout_page.checkout_page_is_submitted()

    @pytest.mark.depends(on=['test_fill_in_checkout_form'])
    def test_complete_checkout(self):
        """this test validates that total amount is valid
        that page can be submitted successfully"""
        successful_banner_message = 'Thank you for your order!'

        overview_page = CheckoutOverview(self.browser)
        assert overview_page.is_overview_page()
        # check that subtotal amount is a sum of price of all the items
        assert overview_page.get_subtotal_amount() == overview_page.get_price_of_all_items_on_page()
        # check that total amount is a sum of tax and subtotal amounts
        assert overview_page.get_tax_amount() + overview_page.get_subtotal_amount() == overview_page.get_total_amount()
        # submit overview page and validate successful message is displayed on a banner
        overview_page.submit_overview_page()
        assert overview_page.overview_page_is_submitted()
        checkout_complete_page = CheckoutCompletePage(self.browser)
        assert checkout_complete_page.is_checkout_complete_page()
        assert checkout_complete_page.successful_banner_is_displayed()
        assert checkout_complete_page.get_successful_banner_message() == successful_banner_message



