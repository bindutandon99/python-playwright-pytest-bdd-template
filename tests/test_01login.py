
from playwright.sync_api import expect
from pytest_bdd import given, scenario, then, when
from config import constants


@scenario('../features/login.feature', 'Invalid user login')
def test_user_invalid_login():
    pass

@when("I enter valid username and invalid password")
def enter_invalid_password(login_page_instance):
    login_page_instance.login(constants.USER_NAME,constants.USER_INVALID_PASSWORD)


@then("I should get an error")
def should_get_an_error(login_page_instance):

    val=login_page_instance.get_error_message()
    assert val=="Epic sadface: Username and password do not match any user in this service","The error message is incorrect"


@then("I should remain on login page")
def i_should_remain_on_login_page(login_page_instance):

    expect(login_page_instance.page).to_have_url(login_page_instance.get_url())


@scenario('../features/login.feature', 'Valid user login')
def test_user_login():
    pass


@given('I open the login page')
def step_user_opens_login_page(login_page_instance,browser):
    print(f"\n--- Running test on {browser} ---")  # <
    assert login_page_instance.is_username_field_visible(), "Username field is not visible"


@when('I enter valid username and password')
def step_when_user_enters_credentials(login_page_instance):

    login_page_instance.login(constants.USER_NAME,constants.USER_VALID_PASSWORD)


@then('I should see the dashboard')
def step_then_user_logged_in(login_page_instance):
    assert login_page_instance.is_logged_in(), "login was not successful"
    #assert "Swag Labs" == login_page_instance.page.title()
    print("dashboard visible, login successful")

    #login_page_instance.page.pause()


