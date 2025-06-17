from lib.models import cart_page

from pytest_bdd import given, scenario, then, when
from playwright.sync_api import expect


@scenario('../features/addition_cart.feature', 'shopping cart functions')
def test_addition_cart():
    pass

@given('I am on the Dashboard')
def step_user_is_on_dashboard(logged_in_session_page):
    products_page_instance = ProductsPage(logged_in_session_page)
    products_page_instance.is_loaded()
    assert "Swag Labs" == logged_in_session_page.title()
    print(f"\n--- I am on the right page displaying products")



@when('I select an item')
def step_when_user_selects_item(logged_in_session_page):
    products_page_instance.add_product_to_cart("Sauce Labs Backpack")
    # logged_in_session_page.get_by_text("Products").click()
    # logged_in_session_page.get_by_text("Sauce Labs Backpack").click()
    # assert (logged_in_session_page.locator('[id="back-to-products"]')).is_visible()


@when('click on the bag icon')
def step_click_addtocart(logged_in_session_page):
    logged_in_session_page.locator("[data-test=\"add-to-cart\"]").click()

@then('Item is added to cart')
def step_then_item_added_to_cart(logged_in_session_page):

    logged_in_session_page.locator("[data-test=\"shopping-cart-link\"]").click()

    expect(logged_in_session_page.locator("[data-test=\"title\"]")).to_have_text("Your Cart")

    cart_page.check_item_quantity(logged_in_session_page, "Sauce Labs Backpack", 1)

    print("item added to cart")



#####to compare
# tests/test_addition_cart.py




@when('I select an item')
def step_when_user_selects_item(logged_in_session_page):
    products_page_instance = ProductsPage(logged_in_session_page)
    # This step now directly adds the product to cart from the products page
    # without navigating to the product detail page first, which simplifies the flow.
    # If you *need* to go to the detail page, use products_page_instance.view_product_details("Sauce Labs Backpack")
    # and then add to cart from the detail page (which would need its own Page Object).


    # The following assertions are now handled within add_product_to_cart method
    # logged_in_session_page.get_by_text("Products").click() # Likely redundant
    # logged_in_session_page.get_by_text("Sauce Labs Backpack").click() # This was for detail page
    # assert (logged_in_session_page.locator('[id="back-to-products"]')).is_visible() # This was for detail page

@when('click on the bag icon')
def step_click_addtocart(logged_in_session_page):
    # This step is now redundant if 'I select an item' already adds to cart.
    # If the feature means "I select an item (which adds it to cart), AND THEN I click the bag icon",
    # then this step should only navigate to the cart.
    # Let's assume the previous step already added to cart, and this step is about navigation.
    products_page_instance = ProductsPage(logged_in_session_page)
    products_page_instance.go_to_cart()

    # The previous line: logged_in_session_page.locator("[data-test=\"add-to-cart\"]").click()
    # is now handled by products_page_instance.add_product_to_cart() in the previous step.

@then('Item is added to cart')
def step_then_item_added_to_cart(logged_in_session_page):
    # Instantiate the CartPage object
    cart_page_instance = CartPage(logged_in_session_page)

    # Use the CartPage method to check the cart title and item quantity
    # The navigation to cart is now handled in the 'click on the bag icon' step,
    # or you could put cart_page_instance.navigate_to_cart() here if that step is removed.
    expect(cart_page_instance.cart_title).to_have_text("Your Cart") # Still good to have this assertion

    cart_page_instance.check_item_quantity("Sauce Labs Backpack", 1)

    print("item added to cart")