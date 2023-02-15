from src.pages.menu.menu_page import MenuPage
from src.pages.dropdown.dropdown_page import DropdownPage
from pytest import mark

"""
Run locally: 
    pytest --headless False tests/test_dropdown.py
"""

@mark.parametrize('item', ['Option 1', 'Option 2'])
def test_dropdown(desktop, item):
    menu = MenuPage(desktop.driver)
    menu.navigate_to('Dropdown')

    dropdown = DropdownPage(desktop.driver)
    dropdown.select_item(item)

    assert dropdown.get_current_item() == item, 'Oops, wrong item selected'