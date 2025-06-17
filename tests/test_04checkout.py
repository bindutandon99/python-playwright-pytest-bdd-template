from conftest import logged_in_session_page
from config import constants
from lib.models.cart_page import CartPage

from lib.models.checkout_page import CheckoutPage

from pytest_bdd import given,when, then, scenario



@scenario('../features/checkout.feature', 'Enter information on checkout overview page')
def test_checkout_overview_page():
     pass

@given('I am on the checkout page')
def step_user_is_checkout_page(logged_in_session_page):
    global cart_page_instance
    global checkout_overview_page_instance

    if constants.CHECKOUT_URL_PART not in logged_in_session_page.page.url:
        logged_in_session_page.go_to_cart()
        cart_page_instance = CartPage(logged_in_session_page.page)
        cart_page_instance.click_checkout()
    checkout_overview_page_instance=CheckoutPage(cart_page_instance.page)
    checkout_overview_page_instance.is_your_information_page_loaded()


@when('I enter my personal information')
def step_user_enters_personal_info(logged_in_session_page):

    checkout_overview_page_instance.fill_your_information(constants.FIRST_NAME,constants.LAST_NAME,constants.POSTAL_CODE)

@when('I click continue button')
def step_user_clicks_on_checkout(logged_in_session_page):
    checkout_overview_page_instance.click_continue()

@then('I am on checkout overview page')
def step_user_is_on_checkout_page(logged_in_session_page):
    checkout_overview_page_instance.is_overview_page_loaded()


@scenario('../features/checkout.feature', 'Verify order details')
def test_verify_order_details():
    pass

@given('I have added item,entered personal details,I am on checkout overview page')
def step_user_is_checkout_page(logged_in_session_page):
    global cart_page_instance
    global checkout_overview_page_instance

    if constants.CHECKOUT_OVERVIEW_URL_PART in logged_in_session_page.page.url :
       checkout_overview_page_instance.click_cancel_from_overview_page()
    logged_in_session_page.add_product_to_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)
    logged_in_session_page.go_to_cart()
    cart_page_instance = CartPage(logged_in_session_page.page)
    cart_page_instance.click_checkout()
    checkout_overview_page_instance = CheckoutPage(cart_page_instance.page)
    checkout_overview_page_instance.is_your_information_page_loaded()
    checkout_overview_page_instance.fill_your_information(constants.FIRST_NAME,constants.LAST_NAME,constants.POSTAL_CODE)
    checkout_overview_page_instance.click_continue()



@when('I see the \'Sauce labs Backpack\' in cart')
def step_item_in_cart():
    checkout_overview_page_instance.is_item_for_checkout(constants.PRODUCT_SAUCE_LABS_BACKPACK)


@then('I should see its correct quantity and price')
def step_user_clicks_on_checkout():
    price = checkout_overview_page_instance.get_displayed_total_price()
    assert price==32.39
    print('aim here')
    # qu=checkout_overview_page_instance.page_item_quantity
    assert ("1"==checkout_overview_page_instance.page_item_quantity.text_content())





@scenario('../features/checkout.feature', 'Successful Checkout and Order completion')
def test_order_completion():
    pass

@given('I am on the checkout overview page')
def step_user_is_checkout_page(logged_in_session_page):
    global cart_page_instance
    global checkout_overview_page_instance

    if constants.CHECKOUT_OVERVIEW_URL_PART not in logged_in_session_page.page.url :
        logged_in_session_page.go_to_cart()
        cart_page_instance = CartPage(logged_in_session_page.page)
        cart_page_instance.click_checkout()
        checkout_overview_page_instance = CheckoutPage(cart_page_instance.page)
        checkout_overview_page_instance.fill_your_information(constants.FIRST_NAME,constants.LAST_NAME,constants.POSTAL_CODE)
        checkout_overview_page_instance.click_continue()
    checkout_overview_page_instance.is_overview_page_loaded()


@when('I click on finish button')
def step_user_clicks_finish_button():
    checkout_overview_page_instance.click_finish()


@then('I see the checkout complete page')
def step_checkout_is_complete():
    checkout_overview_page_instance.is_checkout_complete_page_loaded()


@then('I see the order has been dispatched')
def order_dispatched():
    assert "Thank you for your order!"==checkout_overview_page_instance.get_confirmation_message()