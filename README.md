# References

* https://behave.readthedocs.io/en/latest/more_info/

# Python BDD testing using behave

To execute the tests:

```shell
poetry install
poetry run behave
```

Sample output:

```
Feature: showing off behave # features/first.feature:1

  Scenario: run a simple test       # features/first.feature:3
    Given we have behave installed  # features/steps/step-definitions.py:5 0.000s
    When we implement a test        # features/steps/step-definitions.py:10 0.000s
    Then behave will test it for us # features/steps/step-definitions.py:15 0.000s

  Scenario Outline: calculate 42 -- @1.1   # features/first.feature:19
    When you multiply 21 by 2              # features/steps/step-definitions.py:20 0.000s
    Then the answer is 42                  # features/steps/step-definitions.py:29 0.000s

  Scenario Outline: calculate 42 -- @1.2   # features/first.feature:20
    When you multiply 14 by 3              # features/steps/step-definitions.py:20 0.000s
    Then the answer is 42                  # features/steps/step-definitions.py:29 0.000s

  Scenario Outline: calculate 42 -- @1.3   # features/first.feature:21
    When you multiply 7 by 6               # features/steps/step-definitions.py:20 0.000s
    Then the answer is 42                  # features/steps/step-definitions.py:29 0.000s

  Scenario Outline: calculate 42 -- @1.4   # features/first.feature:22
    When you multiply 6 by 9               # features/steps/step-definitions.py:20 0.000s
    Then the answer is 42                  # features/steps/step-definitions.py:29 0.000s
      Assertion Failed: expected 42, actual 54



Failing scenarios:
  features/first.feature:22  calculate 42 -- @1.4 

0 features passed, 1 failed, 0 skipped
4 scenarios passed, 1 failed, 0 skipped
10 steps passed, 1 failed, 0 skipped, 0 undefined
Took 0m0.000s
```
