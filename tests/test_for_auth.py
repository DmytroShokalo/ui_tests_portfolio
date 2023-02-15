from src.pages.menu.menu_page import MenuPage
from src.pages.form_auth.form_auth_page import FormAuthPage
from pytest import mark


"""
Run locally: 
    pytest --headless False tests/test_for_auth.py
"""

class TestFormAuth:
    CREDS = None

    @mark.dependency()
    def test_setup(self, desktop):
        menu = MenuPage(desktop.driver)
        menu.navigate_to('Form Authentication')

        auth = FormAuthPage(desktop.driver)
        TestFormAuth.CREDS = auth.get_credential()

    @mark.dependency(depends=['TestFormAuth::test_setup'])
    def test_login(self, desktop):
        auth = FormAuthPage(desktop.driver)

        auth.fill_username(self.CREDS['username'])
        auth.fill_password(self.CREDS['password'])
        auth.login()

        assert desktop.page_contains_text('You logged into a secure area!')

    @mark.dependency(depends=['TestFormAuth::test_login'])
    def test_logout(self, desktop):
        auth = FormAuthPage(desktop.driver)
        auth.logout()

        assert desktop.page_contains_text('You logged out of the secure area!')

    @mark.dependency(depends=['TestFormAuth::test_logout'])
    def test_unknown_password(self, desktop, fake):
        auth = FormAuthPage(desktop.driver)

        auth.fill_username(self.CREDS['username'])
        auth.fill_password(fake.string(6))
        auth.login()

        assert desktop.page_contains_text('Your password is invalid!')

    @mark.dependency(depends=['TestFormAuth::test_logout'])
    def test_unknown_username(self, desktop, fake):
        auth = FormAuthPage(desktop.driver)

        auth.fill_username(fake.string(6))
        auth.fill_password(self.CREDS['password'])
        auth.login()

        assert desktop.page_contains_text('Your username is invalid!')
