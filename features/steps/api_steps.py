from behave import given, when, then
from api_clients.users_api import UsersAPI


@given("I have the users API")
def step_setup_users_api(context):
    context.api = UsersAPI()


@when("I retrieve the list of users")
def step_get_users(context):
    context.response = context.api.get_users()


@then("I should receive a {status_code:d} response code")
def step_validate_response_code(context, status_code):
    assert (
        context.response.status_code == status_code
    ), f"Expected {status_code}, got {context.response.status_code}"


@then("the response should contain a list of users")
def step_validate_user_list(context):
    response_data = context.response.json()

    assert "data" in response_data, "Response does not contain 'data' key"
    users_list = response_data["data"]

    assert isinstance(users_list, list), "Users list is not present"
    assert len(users_list) > 0, "Users list is empty"


@when("I retrieve the details of the first user")
def step_get_first_user_details(context):
    response_data = context.response.json()

    assert "data" in response_data, "Response does not contain 'data' key"
    users_list = response_data["data"]
    assert len(users_list) > 0, "No users found in the response"

    first_user_id = users_list[0]["id"]
    context.response = context.api.get_user_by_id(first_user_id)


@then("the response should contain user details")
def step_validate_user_details(context):
    response_data = context.response.json()

    assert "data" in response_data, "Response does not contain 'data' key"
    user_data = response_data["data"]

    assert isinstance(user_data, dict), "Expected a dictionary for user details"

    expected_keys = {"id", "email", "first_name", "last_name", "avatar"}
    assert expected_keys.issubset(
        user_data.keys()
    ), f"User details are incomplete, missing keys: {expected_keys - user_data.keys()}"


@when("I create a new user with the following details")
def step_create_user(context):
    user_data = {row["name"]: row["email"] for row in context.table}
    context.response = context.api.create_user(user_data)


@then("the response should contain a user ID")
def step_validate_user_id(context):
    response_data = context.response.json()
    assert "id" in response_data, "Response does not contain 'id' key"
