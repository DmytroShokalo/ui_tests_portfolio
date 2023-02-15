from allure import step
from src.pages.base_page import BasePage
from src.elements.input import InputElement

class CheckboxElement:
    def __init__(self, driver):
        self.page = BasePage(driver)

    @step('select_checkbox')
    def select_checkbox(self, text: str):
        loc = self._get_checkbox_loc(text)
        if not self.is_checkbox_checked(text):
            self.page.click_element(loc)
            self.page.wait_for_time(0.2)
        assert self.is_checkbox_checked(text), f'Oops! Checkbox "{text}" not selected'

    @step('unselect_checkbox')
    def unselect_checkbox(self, text: str):
        loc = self._get_checkbox_loc(text)
        if self.is_checkbox_checked(text):
            self.page.click_element(loc)
            self.page.wait_for_time(0.2)
        assert not self.is_checkbox_checked(text), f'Oops! Checkbox "{text}" not unselected'

    @step('get_checkbox_status')
    def is_checkbox_checked(self, text: str):
        loc = self._get_checkbox_loc(text)
        class_value = self.page.get_element_attribute(loc, attr='checked')
        status = True if class_value is not None else False
        return status

    def _get_checkbox_loc(self, text: str):
        if text == 'checkbox 1':
            return self.locCheckbox1
        elif text == 'checkbox 2':
            return self.locCheckbox2