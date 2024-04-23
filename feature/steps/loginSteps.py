from datetime import datetime

from behave import *

from feature.pages.HomePage import HomePage


@given(u'navigate to login page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_my_account()
    context.login_page = home_page.select_login_option()


@when(u'enter invalid email and valid password as {password} into the fields')
def step_impl(context, password):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "ginger" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when(u'click on login button')
def step_impl(context):
    context.login_page.click_login_button()


@then(u'valid the warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_status_of_warning_message(expected_warning_message)


@when(u'enter valid email as {email} and invalid password as {password} into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'enter invalid email and invalid password as {password} into the fields')
def step_impl(context, password):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "ginger" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when(u'enter no email and password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
