Feature: Cart functionality

Scenario: Removal of item from cart
    Given I am on the cart page
    When I select existing item to remove
    Then item is successfully removed

Scenario: Continue shopping from cart page
    Given I am on the cart page
    When I click on continue shopping button
    Then I am back on products page


Scenario: Successful Navigation to Checkout Page
    Given I am on the cart page
    When I click on checkout button
    Then I am on checkout page




