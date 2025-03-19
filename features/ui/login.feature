@ui
Feature: Login functionality

  Scenario: User logs in successfully
    Given I open the login page
    When I login with username 'Admin' and password 'admin123'
    Then I should see the dashboard

  Scenario Outline: Login with multiple credentials
    Given I open the login page
    When I login with username '<username>' and password '<password>'
    Then I should see an error message

    Examples:
      | username  | password     |
      | user1     | pass123      |
      | user2     | securePass   |
      | admin     | adminPass    |