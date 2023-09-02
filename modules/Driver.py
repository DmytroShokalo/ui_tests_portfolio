import os
import logging
import conf_file as cfg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from modules.Allure import log_text_to_allure


class Driver:
    def __init__(self, browser_name=None, version=None, headless=False, hub=False):
        self.WINDOW_SIZE = ("1500", "920")
        self._browser_name = browser_name
        self._version = version
        self._headless = headless
        self._hub = hub
    
    def get_driver(self):
        if self._browser_name == "chrome":
            driver = self._get_chrome_driver()
        elif self._browser_name == "firefox":
            driver = self._get_firefox_driver()
        elif self._browser_name == "safari":
            driver = self._get_safari_driver()
        else:
            raise KeyError(f'Oops! Wrong browser: "{self._browser_name}"')
        log_text_to_allure(self._browser_name, name='browser')
        log_text_to_allure(self._version, name='version')
        log_text_to_allure(driver.get_window_size(), name='window_size')
        log_text_to_allure(driver.command_executor._url, name='HUB')
        return driver

    def _get_chrome_driver(self):
        options = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        if self._headless:
            options.add_argument('--headless')
        if self._version:
            options.set_capability("browserVersion", self._version)
        if self._hub:
            driver = webdriver.Remote(command_executor=f'{cfg.HUB}/wd/hub', options=options)
        else:
            #service = ChromeService(executable_path=ChromeDriverManager(version=self._version).install())
            service = ChromeService(executable_path='/usr/local/bin/chromedriver') # for macos m1
            driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(*self.WINDOW_SIZE)
        return driver

    def _get_firefox_driver(self):
        options = webdriver.FirefoxOptions()
        if self._headless:
            options.add_argument('--headless')
        if self._version:
            options.set_capability("browserVersion", self._version)
        if self._hub:
            driver = webdriver.Remote(command_executor=f'{cfg.HUB}/wd/hub', options=options)
        else:
            service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(service=service, options=options)
        driver.set_window_size(*self.WINDOW_SIZE)
        return driver

    def _get_safari_driver(self):
        options = SafariOptions()
        if self._headless:
            options.add_argument('--headless')
        if self._version:
            options.set_capability("browserVersion", self._version)
        if self._hub:
            driver = webdriver.Remote(command_executor=f'{cfg.HUB}/wd/hub', options=options)
        else:
            driver = webdriver.Safari(service=SafariService(executable_path='/usr/bin/safaridriver'), options=options)
        driver.set_window_size(*self.WINDOW_SIZE)
        return driver

"""
pytest --headless=True --browser-version=safari --hub False  tests/ --alluredir=allure-results
pytest --headless=True --browser_name=safari --hub False  tests/
pytest --headless=True --browser_name=safari --hub False  tests/test_checkboxes.py
pytest --headless=True --browser_name=safari --hub False  tests/test_js_alerts.py
pytest --headless True --browser_name firefox --hub False tests/test_js_alerts.py
pytest --headless True --browser_name firefox --hub True tests/test_js_alerts.py
pytest --headless True --browser_name firefox --browser_version 116.0 --hub True tests/ --alluredir=allure-results
pytest tests/test_checkboxes.py
allure generate -c allure-results

pytest --headless True --browser_name firefox --browser_version 116.0 --hub True tests/test_js_alerts.py
pytest --browser_name chrome --browser_version 116.0 --hub True tests/test_js_alerts.py
pytest --browser_name firefox --browser_version 116.0 tests/test_dropdown_list.py
"""