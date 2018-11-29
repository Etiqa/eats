@ST1000F001
Feature: Homepages
  As a user
  I should be able to ...
  In order to ...

  @S001
  Scenario: Index page url
    When I go to "index" page
    Then I should be on "/index.html" url

  @S002
  Scenario: Index page default
    When I go to "index" page
    Then I should be on "index" page
    And I should see "Angular Test Form" title on "index" page
