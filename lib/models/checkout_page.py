from playwright.sync_api import Page, expect, Locator
from config import constants

class CheckoutPage:


    def __init__(self, page: Page):
        self.page = page

        # --- Locators for Checkout Step One: Your Information (checkout-step-one.html) ---
        self.url_step_one = "https://www.saucedemo.com/checkout-step-one.html"
        self.page_title_step_one = page.locator("[data-test=\"title\"]")
        self.first_name_input = page.locator("[data-test=\"firstName\"]")
        self.last_name_input = page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")
        self.cancel_button_step_one = page.locator("[data-test=\"cancel\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.error_message_container = page.locator("[data-test=\"error\"]")

        # --- Locators for Checkout Step Two: Overview (checkout-step-two.html) ---
        self.url_step_two = "https://www.saucedemo.com/checkout-step-two.html"
        self.page_title_step_two = page.locator("[data-test=\"title\"]")
        self.page_item_quantity=page.locator("[data-test=\"item-quantity\"]")
        self.payment_info_label = page.locator(".summary_info_label:has-text(\"Payment Information:\")")
        self.shipping_info_label = page.locator(".summary_info_label:has-text(\"Shipping Information:\")")
        self.item_total_price = page.locator(".summary_subtotal_label")
        self.tax_price = page.locator(".summary_tax_label")
        self.total_price = page.locator(".summary_total_label")
        self.cancel_button_step_two = page.locator("[data-test=\"cancel\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")

        # --- Locators for Checkout Step Three: Complete!
        self.url_complete = "https://www.saucedemo.com/checkout-complete.html"
        self.page_title_complete = page.locator("[data-test=\"title\"]")
        self.complete_header = page.locator(".complete-header")
        self.complete_text = page.locator(".complete-text")
        self.pony_express_image = page.locator(".pony_express")
        self.back_home_button = page.locator("[data-test=\"back-to-products\"]")


    # --- Actions and Assertions for Checkout Start Page /Step One  ---
    def is_your_information_page_loaded(self):

        expect(self.page).to_have_url(self.url_step_one)
        expect(self.page_title_step_one).to_have_text("Checkout: Your Information")
        expect(self.first_name_input).to_be_visible()
        print(f"\n--- Checkout: Your Information page loaded: {self.page.url} ---")

    def fill_your_information(self, first_name: str, last_name: str, postal_code: str):

        print(f"Filling checkout info: {first_name}, {last_name}, {postal_code}")
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def click_continue(self):

        print("Clicking Continue...")
        expect(self.continue_button).to_be_visible()
        self.continue_button.click()

    def get_error_message(self) -> str:

        expect(self.error_message_container).to_be_visible()
        return self.error_message_container.text_content()

    def click_cancel_from_info_page(self):

        print("Clicking Cancel from info page...")
        expect(self.cancel_button_step_one).to_be_visible()
        self.cancel_button_step_one.click()



    # --- Actions and Assertions for Checkout Step Two ---
    def is_item_for_checkout(self, item_name: str) -> bool:
        item_locator = self.get_cart_item_locator(item_name)
        return item_locator.count() > 0

    def get_cart_item_locator(self, item_name: str) -> Locator:
        return self.page.locator(f".checkout_list .checkout_item:has-text('{item_name}')")

    def is_overview_page_loaded(self):
        """
        Asserts that the "Checkout: Overview" page is loaded.
        """
        expect(self.page).to_have_url(self.url_step_two)
        expect(self.page_title_step_two).to_have_text("Checkout: Overview")
        expect(self.payment_info_label).to_be_visible()
        expect(self.shipping_info_label).to_be_visible()
        print(f"--- Checkout: Overview page loaded: {self.page.url}")

    def get_displayed_total_price(self) -> float:

        expect(self.total_price).to_be_visible()
        price_text = self.total_price.text_content() # e.g., "Total: $32.39"
        return float(price_text.replace("Total: $", "").strip())

    def click_finish(self):
        """Clicks the 'Finish' button on checkout step two."""
        print("Clicking Finish...")
        expect(self.finish_button).to_be_visible()
        self.finish_button.click()

    def click_cancel_from_overview_page(self):

        print("Clicking Cancel from overview page...")
        expect(self.cancel_button_step_two).to_be_visible()
        self.cancel_button_step_two.click()



    # --- Actions and Assertions for Checkout Step Three ---

    def is_checkout_complete_page_loaded(self):

        expect(self.page).to_have_url(self.url_complete)
        expect(self.page_title_complete).to_have_text("Checkout: Complete!")
        expect(self.complete_header).to_have_text("Thank you for your order!")
        expect(self.pony_express_image).to_be_visible()
        print(f"--- Checkout: Complete! page loaded: {self.page.url}")

    def get_confirmation_message(self) -> str:

        expect(self.complete_header).to_be_visible()
        return self.complete_header.text_content()

    def click_back_home(self):

        print("Clicking Back Home...")
        expect(self.back_home_button).to_be_visible()
        self.back_home_button.click()

