from src.pages.menu.menu_page import MenuPage
from src.pages.dropdown.dropdown_page import DropdownPage
from pytest import mark
import allure


"""
Run locally: 
    pytest --headless False tests/test_dropdown_list.py
Make report:
    allure generate -c allure-results
"""

@allure.severity(allure.severity_level.NORMAL)
@mark.parametrize('item', ['Option 1', 'Option 2'])
def test_dropdown(desktop, item):
    with allure.step('User on Menu page'):
        pass
    with allure.step('User open Dropdown page'):
        menu = MenuPage(desktop.driver)
        menu.navigate_to('Dropdown')
    with allure.step(f'User select Dropdown option: {item}'):
        dropdown = DropdownPage(desktop.driver)
        dropdown.select_item(item)
        assert dropdown.get_current_item() == item, 'Oops, wrong item selected'