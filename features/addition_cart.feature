Feature: shopping cart functions

  Scenario: Addition of items to cart
    Given I am on the Dashboard
    When I select an item
    * navigate to cart
    Then item is added to cart

  Scenario: Removal of objects from cart
    Given I am on the Dashboard
    When I select an item for removal
    * navigate to cart
    Then Item is removed from cart

  Scenario: Sorting of objects on Products Page
    Given I am on the Dashboard
    When I click on the sorting by price in ascending order
    Then Items are sorted in ascending order

