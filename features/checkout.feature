Feature: Checkout functionality

Scenario: Enter information on checkout overview page
    Given I am on the checkout page
    When I enter my personal information
    And I click continue button
    Then I am on checkout overview page

Scenario: Verify order details
    Given I have added item,entered personal details,I am on checkout overview page
    When I see the 'Sauce labs Backpack' in cart
    Then I should see its correct quantity and price


Scenario: Successful Checkout and Order completion
    Given I am on the checkout overview page
    When I click on finish button
    Then I see the checkout complete page
    And I see the order has been dispatched




