from feature.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_value):
        self.type_into_element("email_address_field_id", self.email_address_field_id, email_value)

    def enter_password(self, password_value):
        self.type_into_element("password_field_id", self.password_field_id, password_value)

    def click_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def display_status_of_warning_message(self, expected_warning_message):
        return self.validate_contains_text("warning_message_xpath", self.warning_message_xpath, expected_warning_message)
