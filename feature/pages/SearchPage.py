from feature.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    display_product_xpath = "//div[@class='product-thumb']//div[2]//h4"
    product_warning_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_product_details(self):
        return self.driver.find_element("xpath", self.display_product_xpath).is_displayed()

    def validate_warning_message(self, expected_result):
        return self.driver.find_element("xpath", self.product_warning_message_xpath).text.__eq__(expected_result)
