Feature: showing off behave

  Scenario: run a simple test

    As spotted on https://behave.readthedocs.io/en/latest/tutorial/

    Given we have behave installed
    When we implement a test
    Then behave will test it for us

  Scenario Outline: calculate 42

    Another test, with examples.

    When you multiply <lhs> by <rhs>
    Then the answer is 42
  Examples:
    | lhs | rhs |
    | 21  | 2   |
    | 14  | 3   |
    | 7   | 6   |
    | 6   | 9   |
