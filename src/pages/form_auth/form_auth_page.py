from allure import step
from src.pages.base_page import BasePage
from src.elements.input import InputElement


class FormAuthPage:
    def __init__(self, driver):
        self.page = BasePage(driver)
        self.el_input = InputElement(driver)

    locCredentialSource = '//*[@class="subheader"]/em'
    locUsernameInput = '//input[@id="username"]'
    locPasswordInput = '//input[@id="password"]'
    locLoginBtn = '//button[@type="submit"]'
    locLogoutLnk = '//a[./*[contains(text(),"Logout")]]'

    @step('get_credential')
    def get_credential(self):
        self.page.wait_element_is_visible(self.locCredentialSource)

        username = self.page.get_text(f'{self.locCredentialSource}[1]')
        password = self.page.get_text(f'{self.locCredentialSource}[2]')

        AUTH = dict({'username': username, 'password': password})
        return AUTH

    @step('fill_username')
    def fill_username(self, name: str):
        self.page.wait_element_is_visible(self.locUsernameInput)
        self.page.clear_text(self.locUsernameInput)
        self.page.type_text(self.locUsernameInput, name)

    @step('fill_password')
    def fill_password(self, paswrd):
        self.page.wait_element_is_visible(self.locPasswordInput)
        self.page.clear_text(self.locPasswordInput)
        self.page.type_text(self.locPasswordInput, paswrd)

    @step('login')
    def login(self):
        self.page.wait_element_is_visible(self.locLoginBtn)
        self.page.wait_element_is_clickable(self.locLoginBtn)
        self.page.click_element(self.locLoginBtn)

    @step('logout')
    def logout(self):
        self.page.wait_element_is_visible(self.locLogoutLnk)
        self.page.wait_element_is_clickable(self.locLogoutLnk)
        self.page.click_element(self.locLogoutLnk)