import pytest
from modules.Driver import Driver
from src.pages.base_page import BasePage


def pytest_addoption(parser):
    """ Pytest options for run tests (command line) """
    parser.addoption("--lang", action="store", default="en")
    parser.addoption("--headless", action="store", default="False")
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default=None)
    parser.addoption("--hub", action="store", default=None)

@pytest.fixture(scope='class')
def desktop(request):
    # 1 - prepare webdriver instance
    headless = eval(request.config.getoption("--headless"))
    browser_name = request.config.getoption("--browser_name")
    browser_version = request.config.getoption("--browser_version")
    hub = request.config.getoption("--hub")
    driver = Driver().get_driver(
        browser_name=browser_name, headless=headless, version=browser_version, hub=hub
    )
    # 2 - setup browser
    browser = BasePage(driver)
    browser.goto('/')
    # 3 - make browser available
    yield browser
    # 4 - teardown browser
    browser.quit()

@pytest.fixture(scope='class')
def fake():
    from modules.Faker import Fake
    yield Fake