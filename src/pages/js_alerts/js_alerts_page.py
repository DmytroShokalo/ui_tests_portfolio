from allure import step
from src.pages.base_page import BasePage
from src.elements.input import InputElement


class JsAlertsPage:
    def __init__(self, driver):
        self.page = BasePage(driver)

    locAlertBtn = '//button[contains(text(),"{}")]'

    @step('call_alert')
    def call_alert(self, name: str):
        loc = self.locAlertBtn.format(name)
        self.page.wait_element_is_visible(loc)
        self.page.wait_element_is_clickable(loc)
        self.page.click_element_by_js(loc)

    @step('get_alert_hint')
    def get_alert_hint(self):
        alert = self.page.driver.switch_to.alert
        return alert.text

    @step('accept_alert')
    def accept_alert(self):
        alert = self.page.driver.switch_to.alert
        alert.accept()

    @step('dismiss_alert')
    def dismiss_alert(self):
        alert = self.page.driver.switch_to.alert
        alert.dismiss()

    @step('enter_text_alert')
    def enter_text_alert(self, text: str):
        alert = self.page.driver.switch_to.alert
        alert.send_keys(text)