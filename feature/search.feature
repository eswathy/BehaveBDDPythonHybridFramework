Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given navigate to home page
    When enter valid product into search box field
    And click on search button
    Then valid product should get displayed in search results

  @search
  Scenario: Search for a invalid product
    Given navigate to home page
    When enter invalid product into search box field
    And click on search button
    Then proper message should be displayed in search results

  @search
  Scenario: Search without entering any product
    Given navigate to home page
    When enter no value into search box field
    And click on search button
    Then proper message should be displayed in search results