@ST1000F001
Feature: Homepages
  As a user
  I should be able to ...
  In order to ...

  @S001
  Scenario: Index page url
    Given "gianni" user
    And "pippo" user
    When "gianni" user go to "index" page
    And "pippo" user go to "index" page
