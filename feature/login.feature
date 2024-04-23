Feature: Login functionality

  @login
  Scenario Outline: Login with invalid email and valid password
    Given navigate to login page
    When enter invalid email and valid password as "<password>" into the fields
    And click on login button
    Then valid the warning message
    Examples:
      | password |
      | 152632   |
      | 154856   |

  @login
  Scenario: Login with valid email and invalid password
    Given navigate to login page
    When enter valid email as "amotooriapril2023@gmail.com" and invalid password as "156265" into the fields
    And click on login button
    Then valid the warning message

  @login
  Scenario: Login with invalid credentials
    Given navigate to login page
    When enter invalid email and invalid password as "125623" into the fields
    And click on login button
    Then valid the warning message

  @login
  Scenario: Login without credentials
    Given navigate to login page
    When enter no email and password into the fields
    And click on login button
    Then valid the warning message