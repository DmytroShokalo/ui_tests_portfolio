from selenium.webdriver.remote.webdriver import WebDriver
from allure import step, attach, attachment_type
from modules.Allure import log_console_entire_to_allure
from modules.Driver import Driver
from modules.Utils import ScrolledScreenshot


class BrowserPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def log_location(self):
        attach(self.driver.current_url,
               name='Location',
               attachment_type=attachment_type.URI_LIST)

    def take_screenshot(self):
        attach(self.driver.get_screenshot_as_png(),
               name="Screenshot",
               attachment_type=attachment_type.PNG)

    def take_scrolled_screenshot(self):
        attach(ScrolledScreenshot.get_image(self.driver),
               name="Scrolled_screenshot",
               attachment_type=attachment_type.PNG)

    def take_full_screenshot(self):
        S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll' + X)
        self.driver.set_window_size(S('Width'), S('Height'))
        attach(self.driver.get_screenshot_as_png(),
               name="Full_screenshot",
               attachment_type=attachment_type.PNG)
        self.driver.set_window_size(*Driver().WINDOW_SIZE)

    def log_console_errors(self):
        if 'chrome' in self.driver.name:
            for entire in self.driver.get_log('browser'):
                log_console_entire_to_allure(entire)
    
    @step('quit')
    def quit(self):
        self.driver.quit()