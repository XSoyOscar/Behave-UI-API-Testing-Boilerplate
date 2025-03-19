from behave import given, when, then
from pages.login_page import LoginPage
from utils.config import Config
from utils.logger import logger


@given("I open the login page")
def step_open_login_page(context):
    logger.info("Opening login page")
    context.page = LoginPage(context.driver)
    context.page.open_url(Config.BASE_URL)


@when("I login with username '{username}' and password '{password}'")
def step_login(context, username, password):
    context.page.login(username, password)


@then("I should see the dashboard")
def step_verify_dashboard(context):
    assert context.page.is_dashboard_visible()


@then("I should see an error message")
def step_verify_error_message(context):
    assert context.page.is_error_message_visible()
    assert context.page.get_error_message() == "Invalid credentials"
