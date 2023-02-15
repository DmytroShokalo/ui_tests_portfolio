from allure import step
from src.pages.base_page import BasePage


class InputElement:
    def __init__(self, driver):
        self.page = BasePage(driver)

    @step('get_current_value')
    def get_current_value(self, locator: str):
        value = self.page.get_element_attribute(locator, attr='value')
        return value