from src.pages.menu.menu_page import MenuPage
from src.pages.checkboxes.checkboxes_page import CheckboxesPage
import allure


"""
Run locally: 
    pytest --headless False tests/test_checkboxes.py
Make report:
    allure generate -c allure-results
"""

@allure.severity(allure.severity_level.NORMAL)
def test_checkboxes(desktop):
    with allure.step('User on Menu page'):
        pass
    with allure.step('User open Checkboxes page'):
        menu = MenuPage(desktop.driver)
        menu.navigate_to('Checkboxes')
    with allure.step('First Checkbox is unselected'):
        check = CheckboxesPage(desktop.driver)
        assert check.get_status_checkbox1() == False
    with allure.step('User select first Checkbox'):
        check.select_checkbox1()
        assert check.get_status_checkbox1() == True
    with allure.step('Second Checkbox is selected'):
        assert check.get_status_checkbox2() == True
    with allure.step('User unselect second Checkbox'):
        check.unselect_checkbox2()
        assert check.get_status_checkbox2() == False