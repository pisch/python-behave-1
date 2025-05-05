from behave import *
from behave.runner import Context


@given("we have behave installed")
def we_have_behave_installed(context):
    pass


@when("we implement a test")
def we_implement_a_test(context):
    assert True is not False


@then("behave will test it for us")
def behave_will_test_for_it_for_us(context):
    assert context.failed is False


@when("you multiply {lhs} by {rhs}")
def you_multiply_by(context: Context, lhs: str, rhs: str):

    lhs_int: int = int(lhs)
    rhs_int: int = int(rhs)

    context.Answer = lhs_int * rhs_int


@then("the answer is 42")
def the_answer_is(context: Context):
    assert context.Answer == 42, f"expected {42}, actual {context.Answer}"
