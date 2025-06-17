from playwright.sync_api import Page, expect, Locator


class CartPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = "https://www.saucedemo.com/cart.html"
        self.cart_title = page.locator("[data-test=\"title\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.continue_shopping_button = page.locator("[data-test=\"continue-shopping\"]")

    def navigate_to_cart(self):
        self.shopping_cart_link.click()
        expect(self.cart_title).to_have_text("Your Cart")

    def get_cart_locator(page: Page, item_name: str):
        cart_locator = page.locator(f".cart_list:has-text('{item_name}')")
        cart_row_locator = cart_locator.locator(f".cart_item:has-text('{item_name}')")
        try:
            expect(cart_row_locator).to_be_visible(timeout=2000)
        except Exception as e:
            raise Exception(f"Failed to find object'{cart_row_locator}': {e}")
        return cart_row_locator

    def get_cart_item_locator(self, item_name: str) -> Locator:

        return self.page.locator(f".cart_list .cart_item:has-text('{item_name}')")


    def get_item_locator(cart_row_locator):

        try:
            quantity_locator = cart_row_locator.locator(".cart_quantity")
            # print(f"it is the quantity locator : '{quantity_locator}' ")
            expect(quantity_locator).to_be_visible(timeout=2000)
        except Exception as e:
            raise AssertionError(f"Failed to find object'{quantity_locator}': {e}")
        return quantity_locator

    def check_item_quantity(self, item_name: str, expected_quantity: int):

        item_locator = self.get_cart_item_locator(item_name)


        expect(item_locator).to_be_visible()

        try:
            quantity_locator = item_locator.locator(".cart_quantity")
            expect(quantity_locator).to_have_text(str(expected_quantity), timeout=5000)  # Add a timeout for robustness

            print(f"Checked: '{item_name}' has quantity {expected_quantity} in cart.")
            actual_quantity = int(quantity_locator.text_content().strip())

            print(f"Extracted quantity for '{item_name}': {actual_quantity}")

            assert actual_quantity == expected_quantity, \
                f"Quantity mismatch for '{item_name}': Expected {expected_quantity}, but found {actual_quantity}"
            print(f"SUCCESS: Quantity for '{item_name}' is correct: {actual_quantity}.")

        except Exception as e:
            raise AssertionError(f"Failed to check quantity for '{item_name}': {e}")

    def is_item_in_cart(self, item_name: str) -> bool:

        item_locator = self.get_cart_item_locator(item_name)
        return item_locator.count() > 0

    def remove_item_from_cart(self, item_name: str):
        item_locator = self.get_cart_item_locator(item_name)
        remove_button = item_locator.locator("[data-test^='remove-']")
        expect(remove_button).to_be_visible()
        remove_button.click()
        expect(item_locator).not_to_be_visible()

    def click_checkout(self):

        self.checkout_button.click()

    def click_continue_shopping(self):

        self.continue_shopping_button.click()
