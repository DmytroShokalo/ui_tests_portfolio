from allure import step
from src.pages.base_page import BasePage

class DropdownElement:
    def __init__(self, driver):
        self.page = BasePage(driver)

    locDropdown = '//select[@id="dropdown"]'
    locItem = '//select[@id="dropdown"]/*'

    @step('get_items_list')
    def get_items_list(self):
        items_list = []
        self.page.wait_element_is_visible(self.locDropdown)
        n = self.page.get_element_count(self.locDropdown)
        for i in range(1, n + 1):
            items_list.append(self.page.get_text(f'({self.locItem})[{i}]'))
        return items_list

    @step('select_item')
    def select_item(self, name: str):
        loc = f'{self.locItem}[contains(.,"{name}")]'
        self.page.wait_element_is_visible(loc)
        self.page.click_element(loc)

    @step('select_item_by_index')
    def select_item_by_index(self, index: int):
        loc = f'({self.locItem})[{index}]'
        self.page.wait_element_is_visible(loc)
        self.page.click_element(loc)

    @step('get_current_item')
    def get_item(self):
        self.page.wait_element_is_visible(self.locDropdown)
        loc = f'{self.locItem}[@selected="selected"]'
        return self.page.get_text(loc)

