from allure import step
from modules.Allure import log_text_to_allure
from src.pages.base_page import BasePage
from src.elements.dropdown import DropdownElement

class DropdownPage:
    def __init__(self, driver):
        self.page = BasePage(driver)
        self.el_dropdown = DropdownElement(driver)

    @step('select_item')
    def select_item(self, name: str):
        self.page.take_full_screenshot()
        self.page.wait_for_time(1)
        self.el_dropdown.select_item(name)
        self.page.wait_for_time(2)

    @step('get_current_item')
    def get_current_item(self):
        item = self.el_dropdown.get_item()
        log_text_to_allure(item)
        return item