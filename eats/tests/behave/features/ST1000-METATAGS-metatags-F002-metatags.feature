@ST1000F002
Feature: Metatag
  As a user
  In order to test metatag
  I should be able to see all relevant tag on the html code

  @S001
  Scenario: Value of a metatag
    When I go to "index" page
    Then I should be on "index" page
    And I should see "Angular Test From" value on "apple-mobile-web-app-title" meta

  @S002
  Scenario Outline: Value of multiple metatags
    When I go to "index" page
    Then I should be on "index" page
    And I should see on "<meta_name>" meta the following value
    """
    <meta_value>
    """

    Examples:
      | meta_name                | meta_value      |
      | google-site-verification | XXXXXXXXYYYYYYY |
      | msvalidate.01            | XXXXXYYYYYYYYY  |

  @S003
  Scenario: Metatag not exist
    When I go to "index" page
    Then I should be on "index" page
    And I should not see "METANOTEXIST" meta
