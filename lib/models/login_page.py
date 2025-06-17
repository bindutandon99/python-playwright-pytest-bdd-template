from playwright.sync_api import Page



URL = "https://www.saucedemo.com/"

class LoginPage:

      def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

      def navigate(self):
        self.page.goto(URL)

      def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()


      def get_error_message(self):
        return self.error_message.text_content()

      def is_username_field_visible(self):
        return self.username_field.is_visible()

      def is_logged_in(self):

        return "inventory.html" in self.page.url

      def get_url(self):
          return URL