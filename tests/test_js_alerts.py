from src.pages.menu.menu_page import MenuPage
from src.pages.js_alerts.js_alerts_page import JsAlertsPage
from pytest import mark
import allure


@allure.severity(allure.severity_level.NORMAL)
class TestAlerts:

    @mark.dependency()
    def test_setup(self, desktop):
        with allure.step('User on Menu page'):
            pass
        with allure.step('User open JavaScript Alerts page'):
            menu = MenuPage(desktop.driver)
            menu.navigate_to('JavaScript Alerts')

    @mark.dependency(depends=['TestAlerts::test_setup'])
    def test_js_alert(self, desktop):
        with allure.step('User click on "JS Alert"'):
            alert = JsAlertsPage(desktop.driver)
            alert.call_alert('Click for JS Alert')
            assert alert.get_alert_hint() == 'I am a JS Alert'
        with allure.step('User click OK'):
            alert.accept_alert()
            alert.page.page_contains_text('You successfully clicked an alert')

    @mark.dependency(depends=['TestAlerts::test_setup'])
    def test_js_confirm_alert(self, desktop):
        with allure.step('User click on "JS Confirm"'):
            alert = JsAlertsPage(desktop.driver)
            alert.call_alert('Click for JS Confirm')
            assert alert.get_alert_hint() == 'I am a JS Confirm'
        with allure.step('User click OK'):
            alert.accept_alert()
            alert.page.page_contains_text('You clicked: Ok')
        with allure.step('User click on "JS Confirm"'):
            alert.call_alert('Click for JS Confirm')
        with allure.step('User click Cancel'):
            alert.dismiss_alert()
            alert.page.page_contains_text('You clicked: Cancel')

    @mark.dependency(depends=['TestAlerts::test_setup'])
    def test_js_prompt_alert(self, desktop, fake):
        with allure.step('User click on "Click for JS Prompt"'):
            alert = JsAlertsPage(desktop.driver)
            alert.call_alert('Click for JS Prompt')
            assert alert.get_alert_hint() == 'I am a JS prompt'
        with allure.step('User insert random text in prompt'):
            text = fake.string(6)
            alert.enter_text_alert(text)
            alert.accept_alert()
            assert alert.page.page_contains_text(f'You entered: {text}')
        with allure.step('User click on "JS Prompt"'):
            alert.call_alert('Click for JS Prompt')
        with allure.step('User insert random text in prompt'):
            alert.enter_text_alert(text)
        with allure.step('User dismiss prompt'):
            alert.dismiss_alert()
            assert alert.page.page_contains_text('You entered: null')
