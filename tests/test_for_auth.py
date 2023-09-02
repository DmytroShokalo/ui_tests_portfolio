from src.pages.menu.menu_page import MenuPage
from src.pages.form_auth.form_auth_page import FormAuthPage
from pytest import mark
import allure


"""
Run locally: 
    pytest --headless False tests/test_for_auth.py
Make report:
    allure generate -c allure-results
"""

@allure.severity(allure.severity_level.NORMAL)
class TestFormAuth:
    CREDS = None

    @mark.dependency()
    def test_setup(self, desktop):
        with allure.step('User on Menu page'):
            pass
        with allure.step('User open Form Authentication page'):
            menu = MenuPage(desktop.driver)
            menu.navigate_to('Form Authentication')
        with allure.step('User get credentials'):
            auth = FormAuthPage(desktop.driver)
            TestFormAuth.CREDS = auth.get_credential()

    @mark.dependency(depends=['TestFormAuth::test_setup'])
    def test_login(self, desktop):
        with allure.step('User input username and password'):
            auth = FormAuthPage(desktop.driver)
            auth.fill_username(self.CREDS['username'])
            auth.fill_password(self.CREDS['password'])
        with allure.step('User login'):
            auth.login()
            assert desktop.page_contains_text('You logged into a secure area!'), 'Oops, authentication failed'

    @mark.dependency(depends=['TestFormAuth::test_login'])
    def test_logout(self, desktop):
        with allure.step('User logout'):
            auth = FormAuthPage(desktop.driver)
            auth.logout()
            assert desktop.page_contains_text('You logged out of the secure area!'), 'Oops, authentication failed'

    @mark.dependency(depends=['TestFormAuth::test_logout'])
    def test_unknown_password(self, desktop, fake):
        with allure.step('User input invalid password'):
            auth = FormAuthPage(desktop.driver)
            auth.fill_username(self.CREDS['username'])
            auth.fill_password(fake.string(6))
        with allure.step('User login failed'):
            auth.login()
            assert desktop.page_contains_text('Your password is invalid!'), 'Oops, authentication failed'

    @mark.dependency(depends=['TestFormAuth::test_logout'])
    def test_unknown_username(self, desktop, fake):
        with allure.step('User input unknown username'):
            auth = FormAuthPage(desktop.driver)
            auth.fill_username(fake.string(6))
            auth.fill_password(self.CREDS['password'])
        with allure.step('User login failed'):
            auth.login()
            assert desktop.page_contains_text('Your username is invalid!'), 'Oops, authentication failed'
