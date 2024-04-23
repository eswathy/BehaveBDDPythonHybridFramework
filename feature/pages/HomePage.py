from feature.pages.BasePage import BasePage
from feature.pages.LoginPage import LoginPage
from feature.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_xpath = "//a[@title='My Account']/following-sibling::ul//a[text()='Login']"
    search_box_name = "search"
    search_icon_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("login_option_xpath", self.login_option_xpath)
        return LoginPage(self.driver)

    def validate_title(self, expected_value):
        return self.driver.title.__eq__(expected_value)

    def enter_search_box(self, search_value):
        self.type_into_element("search_box_name", self.search_box_name, search_value)

    def click_search_icon(self):
        self.click_on_element("search_icon_xpath", self.search_icon_xpath)
        return SearchPage(self.driver)
