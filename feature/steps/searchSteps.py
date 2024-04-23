from behave import *

from feature.pages.HomePage import HomePage


@given(u'navigate to home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    expected_title = "Your Store"
    assert context.home_page.validate_title(expected_title)


@when(u'enter valid product into search box field')
def step_impl(context):
    context.home_page.enter_search_box("HP")


@when(u'click on search button')
def step_impl(context):
    context.search_page = context.home_page.click_search_icon()


@then(u'valid product should get displayed in search results')
def step_impl(context):
    assert context.search_page.display_product_details()


@when(u'enter invalid product into search box field')
def step_impl(context):
    context.home_page.enter_search_box("Honda")


@then(u'proper message should be displayed in search results')
def step_impl(context):
    expected_result = "There is no product that matches the search criteria."
    assert context.search_page.validate_warning_message(expected_result)


@when(u'enter no value into search box field')
def step_impl(context):
    context.home_page.enter_search_box("")
