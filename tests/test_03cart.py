from conftest import logged_in_session_page
from lib.models.cart_page import CartPage
from config import constants
from lib.models.checkout_page import CheckoutPage

from pytest_bdd import given,when, then, scenario


@scenario('../features/cart.feature', 'Successful Navigation to Checkout Page')
def test_successful_checkout():
     pass

@given('I am on the cart page')
def step_user_is_oncart_page(logged_in_session_page):
    expected_dashboard_url_part = "/cart.html"
    if expected_dashboard_url_part not in logged_in_session_page.page.url:
        logged_in_session_page.go_to_cart()
    assert "Your Cart" in logged_in_session_page.page.locator("data-test=title").inner_text()
    print(f"\n--- Cart page is loaded")

@when('I click on checkout button')
def step_user_clicks_on_checkout(logged_in_session_page):
    cart_page_instance = CartPage(logged_in_session_page.page)
    cart_page_instance.click_checkout()


@then('I am on checkout page')
def step_user_is_on_checkout_page(logged_in_session_page):
    checkout_page_instance=CheckoutPage(logged_in_session_page.page)
    checkout_page_instance.is_your_information_page_loaded()

@scenario('../features/cart.feature', 'Continue shopping from cart page')
def test_continue_shopping():
    pass

@when('I click on continue shopping button')
def step_click_continue_shopping_button(logged_in_session_page):
      #Assuming I am on the cart page
     cart_page_instance = CartPage(logged_in_session_page.page)
     cart_page_instance.click_continue_shopping()
     assert constants.PRODUCTS_PAGE_TITLE == logged_in_session_page.page.title()

@then("I am back on products page")
def step_user_is_on_products_page(logged_in_session_page):
    logged_in_session_page.is_loaded()


@scenario('../features/cart.feature', 'Removal of item from cart')
def test_remove_item():
    pass

@when('I select existing item to remove')
def step_user_selects_item_to_remove(logged_in_session_page):
    cart_page_instance = CartPage(logged_in_session_page.page)
    # First need to add the item to remove it
    cart_page_instance.click_continue_shopping()
    logged_in_session_page.add_product_to_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)
    logged_in_session_page.go_to_cart()
    cart_page_instance.remove_item_from_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)


@then("item is successfully removed")
def step_item_is_removed(logged_in_session_page):
    cart_page_instance = CartPage(logged_in_session_page.page)
    assert not cart_page_instance.is_item_in_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)
