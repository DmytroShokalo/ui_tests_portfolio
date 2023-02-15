from src.pages.menu.menu_page import MenuPage
from src.pages.js_alerts.js_alerts_page import JsAlertsPage
from pytest import mark


class TestAlerts:

    @mark.dependency()
    def test_setup(self, desktop):
        menu = MenuPage(desktop.driver)
        menu.navigate_to('JavaScript Alerts')

    @mark.dependency(depends=['TestAlerts::test_setup'])
    def test_js_alert(self, desktop):
        alert = JsAlertsPage(desktop.driver)

        alert.call_alert('Click for JS Alert')
        assert alert.get_alert_hint() == 'I am a JS Alert'
        alert.accept_alert()
        alert.page.page_contains_text('You successfully clicked an alert')

    @mark.dependency(depends=['TestAlerts::test_setup'])
    def test_js_confirm_alert(self, desktop):
        alert = JsAlertsPage(desktop.driver)

        alert.call_alert('Click for JS Confirm')
        assert alert.get_alert_hint() == 'I am a JS Confirm'
        alert.accept_alert()
        alert.page.page_contains_text('You clicked: Ok')

        alert.call_alert('Click for JS Confirm')
        alert.dismiss_alert()
        alert.page.page_contains_text('You clicked: Cancel')

    @mark.dependency(depends=['TestAlerts::test_setup'])
    def test_js_prompt_alert(self, desktop, fake):
        alert = JsAlertsPage(desktop.driver)

        alert.call_alert('Click for JS Prompt')
        assert alert.get_alert_hint() == 'I am a JS prompt'

        text = fake.string(6)
        alert.enter_text_alert(text)
        alert.accept_alert()
        assert alert.page.page_contains_text(f'You entered: {text}')

        alert.call_alert('Click for JS Prompt')
        alert.enter_text_alert(text)
        alert.dismiss_alert()
        assert alert.page.page_contains_text('You entered: null')
