import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    def __init__(self):
        self.WINDOW_SIZE = ("1440", "768")

    def get_driver(self, browser_name, version, headless, hub):
        if browser_name == "chrome":
            driver = self._get_chrome_driver(version=version, headless=headless, hub=hub)
        else:
            raise KeyError(f'Oops! Wrong browser: "{browser_name}"')
        return driver

    def _get_chrome_driver(self, version, headless, hub):
        options = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        if headless:
            options.add_argument('--headless')
        if hub is not None:
            driver = webdriver.Remote(command_executor=f'{hub}/wd/hub', options=options)
        else:
            service = ChromeService(executable_path=ChromeDriverManager(version=version).install())
            #service = ChromeService(executable_path='/usr/local/bin/chromedriver') # for macos m1
            driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(*self.WINDOW_SIZE)
        return driver
