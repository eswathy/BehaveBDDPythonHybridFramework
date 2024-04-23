class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element_type(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element("id", locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element("name", locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element("class_name", locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element("link_text", locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element("xpath", locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element("css", locator_value)

        return element

    def click_on_element(self, locator_type, locator_value):
        element = self.element_type(locator_type, locator_value)
        element.click()

    def type_into_element(self, locator_type, locator_value, text_to_be_entered):
        element = self.element_type(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_be_entered)

    def validate_contains_text(self, locator_type, locator_value, text_to_be_checked):
        element = self.element_type(locator_type, locator_value)
        return element.text.__contains__(text_to_be_checked)
