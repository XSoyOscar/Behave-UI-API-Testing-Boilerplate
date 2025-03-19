@api
Feature: Users API functionality

  Scenario: Retrieve users successfully
    Given I have the users API
    When I retrieve the list of users
    Then I should receive a 200 response code
    And the response should contain a list of users

  Scenario: Retrieve user details dynamically
    Given I have the users API
    When I retrieve the list of users
    And I retrieve the details of the first user
    Then I should receive a 200 response code
    And the response should contain user details

  Scenario: Create a new user
    Given I have the users API
    When I create a new user with the following details:
      | name     | email                |
      | John Doe | johndoe@example.com  |
    Then I should receive a 201 response code
    And the response should contain a user ID
