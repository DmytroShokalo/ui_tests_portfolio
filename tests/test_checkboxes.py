from src.pages.menu.menu_page import MenuPage
from src.pages.checkboxes.checkboxes_page import CheckboxesPage

"""
Run locally: 
    pytest --headless False tests/test_checkboxes.py
"""

def test_checkboxes(desktop):
    menu = MenuPage(desktop.driver)
    menu.navigate_to('Checkboxes')

    check = CheckboxesPage(desktop.driver)

    assert check.get_status_checkbox1() == False
    assert check.get_status_checkbox2() == True

    check.select_checkbox1()
    check.unselect_checkbox2()

    assert check.get_status_checkbox1() == True
    assert check.get_status_checkbox2() == False


