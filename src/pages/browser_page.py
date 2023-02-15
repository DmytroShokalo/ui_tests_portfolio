from selenium.webdriver.remote.webdriver import WebDriver

class BrowserPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def quit(self):
        self.driver.quit()