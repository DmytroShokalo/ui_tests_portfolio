from allure import step
from src.pages.base_page import BasePage
from src.elements.checkbox import CheckboxElement

class CheckboxesPage:
    def __init__(self, driver):
        self.page = BasePage(driver)
        self.el_checkbox = CheckboxElement(driver)

    @step('get_status_checkbox1')
    def get_status_checkbox1(self):
        return self.el_checkbox.is_checkbox_checked('checkbox 1')

    @step('select_checkbox1')
    def select_checkbox1(self):
        self.el_checkbox.select_checkbox('checkbox 1')

    @step('unselect_checkbox1')
    def unselect_checkbox1(self):
        self.el_checkbox.unselect_checkbox('checkbox 1')

    @step('get_status_checkbox2')
    def get_status_checkbox2(self):
        return self.el_checkbox.is_checkbox_checked('checkbox 2')

    @step('select_checkbox2')
    def select_checkbox2(self):
        self.el_checkbox.select_checkbox('checkbox 2')

    @step('unselect_checkbox2')
    def unselect_checkbox2(self):
        self.el_checkbox.unselect_checkbox('checkbox 2')