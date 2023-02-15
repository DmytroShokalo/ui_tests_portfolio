from src.pages.menu.menu_page import MenuPage
from src.pages.hovers.hovers_page import HoversPage
from pytest import mark

"""
Run locally: 
    pytest --headless False tests/test_hovers.py
"""

@mark.parametrize('name', ['user1', 'user2', 'user3'])
def test_hovers(desktop, name):
    menu = MenuPage(desktop.driver)
    menu.navigate_to("Hovers")

    hover = HoversPage(desktop.driver)

    assert name in hover.get_img_tip(name), 'Oops, hover tip is wrong'