import logging
from lib.models.login_page import LoginPage
from lib.models.products_page import ProductsPage
from config import constants

import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd.scenario import logger


@pytest.fixture(scope="function")
def login_page_instance(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"slow_mo": 500, "headless": False}


@pytest.fixture(scope="session", autouse=True)
def browser(browser_name, browser_type_launch_args):
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        print(f"\n--- Launching {browser_name} browser ---")  # Added print for confirmation
        logging.info(f"--- Launching {browser_name} browser ---")
        browser_instance = browser_type.launch(**browser_type_launch_args)
        # browser = p.launch(headless=False)
        yield browser_instance
        # browser_instance.close()


@pytest.fixture(scope="session")
def logged_in_session_page(browser, page):
    # context = browser.new_context()
    # page = context.new_page()
    logger.info("Performing one-time login for the entire test session...")
    login_page_instance = LoginPage(page)
    login_page_instance.navigate()

    # self.page.wait_for_url("**/inventory.html")  # Wait for the URL to change
    # return InventoryPage(self.page)
    login_page_instance.login(constants.USER_NAME, constants.USER_VALID_PASSWORD)
    assert login_page_instance.is_logged_in(), "User is now successfully logged in"
    logger.info("Login successful for session, page is now logged in.")
    current_page_after_login = ProductsPage(login_page_instance.page)
    #return current_page_after_login
    yield current_page_after_login

    logger.info("--- Closing logged-in session page and context ---")


@pytest.fixture(scope="session")
def page(browser):
    page = browser.new_page()
    yield page
# page.close()
