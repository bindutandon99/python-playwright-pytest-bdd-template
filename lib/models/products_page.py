from playwright.sync_api import Page, expect, Locator
from typing import List


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"

        # Locators for common elements on the Products Page
        self.page_title = page.locator("[data-test=\"title\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_sidebar_link = page.locator("#logout_sidebar_link")
        self.all_items_sidebar_link = page.locator("#inventory_sidebar_link")
        self.about_sidebar_link = page.locator("#about_sidebar_link")
        self.reset_app_state_sidebar_link = page.locator("#reset_sidebar_link")
        self.product_prices = page.locator(".inventory_item_price")


    def is_loaded(self):

        expect(self.page).to_have_url(self.url)
        expect(self.page_title).to_have_text("Products")
        print(f"\n--- Products Page loaded: {self.page.url}")

    def get_product_item_locator(self, product_name: str) -> Locator:

        return self.page.locator(f".inventory_item:has-text('{product_name}')")

    def get_add_to_cart_button_locator(self, product_name: str) -> Locator:

        product_item = self.get_product_item_locator(product_name)
        return product_item.locator("[data-test^='add-to-cart-']")

    def get_remove_button_locator(self, product_name: str) -> Locator:

        product_item = self.get_product_item_locator(product_name)
        return product_item.locator("[data-test^='remove-']")

    def add_product_to_cart(self, product_name: str):
        print(f"Attempting to add '{product_name}' to cart...")
        add_button = self.get_add_to_cart_button_locator(product_name)
        expect(add_button).to_be_visible()
        add_button.click()
        # Verify the button changed to 'Remove'
        expect(self.get_remove_button_locator(product_name)).to_be_visible()
        print(f"'{product_name}' added to cart.")

    def remove_product_from_cart(self, product_name: str):
        print(f"Attempting to remove '{product_name}' from cart...")
        remove_button = self.get_remove_button_locator(product_name)
        expect(remove_button).to_be_visible()
        remove_button.click()
        expect(self.get_add_to_cart_button_locator(product_name)).to_be_visible()
        print(f"'{product_name}' removed from cart.")

    def view_product_details(self, product_name: str):

        print(f"Viewing details for '{product_name}'...")
        product_name_link = self.get_product_item_locator(product_name).locator(".inventory_item_name")
        expect(product_name_link).to_be_visible()
        product_name_link.click()
        print(f"Navigated to product detail page for '{product_name}'.")

    def go_to_cart(self):
        print("Navigating to cart page...")
        expect(self.shopping_cart_link).to_be_visible()
        self.shopping_cart_link.click()

    def sort_products_by(self, option: str):
        print(f"Sorting products by: {option}")
        expect(self.sort_dropdown).to_be_visible()
        self.sort_dropdown.select_option(option)

    def open_burger_menu(self):
        expect(self.burger_menu_button).to_be_visible()
        self.burger_menu_button.click()
        expect(self.logout_sidebar_link).to_be_visible()
        print("Burger menu opened.")

    def get_product_prices(self) -> List[float]:
        price_strings = self.product_prices.all_text_contents()
        return [float(price.replace('$', '')) for price in price_strings]

    def logout(self):
        self.open_burger_menu()
        expect(self.logout_sidebar_link).to_be_visible()
        self.logout_sidebar_link.click()
        print("Logged out.")

    def get_url(self):
          return self.url