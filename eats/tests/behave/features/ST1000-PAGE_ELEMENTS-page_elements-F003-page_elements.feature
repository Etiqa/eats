@ST1000F003
Feature: Page Elements
  As a user
  In order to test page elements

  @S001
  Scenario: Element on page
    When I go to "index" page
    Then I should be on "index" page
    And I should see "title" element

  @S002
  Scenario: Element not on page
    When I go to "index" page
    Then I should be on "index" page
    And I should not see "ELEMENT_NOT_ON_PAGE" element

  @S003
  Scenario: Click element
    When I go to "index" page
    Then I should be on "index" page
    When I click "checkboxTrue" element