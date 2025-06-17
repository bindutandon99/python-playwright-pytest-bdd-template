from lib.models.cart_page import CartPage
from lib.utils.helpers import helpers
from config import constants

from pytest_bdd import given, scenario, then, when
from playwright.sync_api import expect

from conftest import logged_in_session_page


@scenario('../features/addition_cart.feature', 'Addition of items to cart')
def test_addition_cart():
    pass


@given('I am on the Dashboard')
def step_user_is_on_dashboard(logged_in_session_page):
    # expected_dashboard_url_part = "/inventory.html"
    if constants.DASHBOARD_URL_PART not in logged_in_session_page.page.url:
        logged_in_session_page.page.goto(logged_in_session_page.get_url())

    logged_in_session_page.is_loaded()
    assert constants.PRODUCTS_PAGE_TITLE == logged_in_session_page.page.title()
    print(f"\n--- I am on the right page displaying products")


@when('I select an item')
def step_when_user_selects_item(logged_in_session_page):
    logged_in_session_page.add_product_to_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)

@when('navigate to cart')
def step_click_addtocart(logged_in_session_page):
    logged_in_session_page.go_to_cart()


@then('item is added to cart')
def step_then_item_added_to_cart(logged_in_session_page):
    cart_page_instance = CartPage(logged_in_session_page.page)

    expect(cart_page_instance.cart_title).to_have_text("Your Cart")

    cart_page_instance.check_item_quantity(constants.PRODUCT_SAUCE_LABS_BACKPACK, 1)

    print("item added to cart")
    

 
@scenario('../features/addition_cart.feature', 'Sorting of objects on Products Page')
def test_sort_products():
    pass

@when('I click on the sorting by price in ascending order')
def step_when_user_sorts_items_on_price(logged_in_session_page):
    logged_in_session_page.sort_products_by("lohi")
    logged_in_session_page.page.wait_for_timeout(500)

@then('Items are sorted in ascending order')
def step_then_items_sorted_in_asc(logged_in_session_page):
    item_prices =logged_in_session_page.get_product_prices()
    print(f"--- Product prices after sort: {item_prices}")
    assert helpers.is_sorted_numerically_asc(item_prices),"Prices are not in ascending order"


@scenario('../features/addition_cart.feature', 'Removal of objects from cart')
def test_remove_product():
    pass

@when('I select an item for removal')
def step_when_user_selects_item_for_removal(logged_in_session_page):
    if not logged_in_session_page.get_remove_button_locator(constants.PRODUCT_SAUCE_LABS_BACKPACK):
        logged_in_session_page.add_product_to_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)
    logged_in_session_page.remove_product_from_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK)

@when('navigate to cart')
def step_click_addtocart(logged_in_session_page):
    logged_in_session_page.go_to_cart()


@then('Item is removed from cart')
def step_then_item_removed_from_cart(logged_in_session_page):
    cart_page_instance = CartPage(logged_in_session_page.page)

    expect(cart_page_instance.cart_title).to_have_text("Your Cart")

    assert not cart_page_instance.is_item_in_cart(constants.PRODUCT_SAUCE_LABS_BACKPACK), "Item still exists"
                                                                                              
    print("item removed from cart")




