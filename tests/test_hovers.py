from src.pages.menu.menu_page import MenuPage
from src.pages.hovers.hovers_page import HoversPage
from pytest import mark
import allure


"""
Run locally: 
    pytest --headless False tests/test_hovers.py
Make report:
    allure generate -c allure-results
"""

@allure.severity(allure.severity_level.NORMAL)
@mark.parametrize('name', ['user1', 'user2', 'user3'])
def test_hovers(desktop, name):
    with allure.step('User on Menu page'):
        pass
    with allure.step('User open Hovers page'):
        menu = MenuPage(desktop.driver)
        menu.navigate_to("Hovers")
    with allure.step(f'User hover on profile:{name}'):
        hover = HoversPage(desktop.driver)
        hover.hover_on_img(name)
        assert name in hover.get_img_tip(name), 'Oops, hover tip is wrong'