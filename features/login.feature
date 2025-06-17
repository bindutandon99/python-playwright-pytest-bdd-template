Feature: Login functionality

 Scenario: Invalid user login
    Given I open the login page
    When I enter valid username and invalid password
    Then I should get an error
    *  I should remain on login page

  Scenario: Valid user login
    Given I open the login page
    When I enter valid username and password
    Then I should see the dashboard

