import pytest
from conf_file import BASE_URL, ENV_PARAM, ALLURE_RESULTS_DIR
from modules.Allure import add_allure_environment_properties
from modules.Driver import Driver
from src.pages.base_page import BasePage


def pytest_addoption(parser):
    """ Pytest options for run tests (command line) """
    parser.addoption("--lang", action="store", default="en")
    parser.addoption("--headless", action="store", default='True')
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default=None)
    parser.addoption("--hub", action="store", default='False')

def pytest_configure(config):
    # to use new markers, add them to the list 'markers_list'
    markers_list = ['smoke', 'regression', 'auth', 'order', 'payment']
    for mark in markers_list:
        config.addinivalue_line("markers", f"{mark}: mark test to run")
    config.addinivalue_line("markers", "on_env(name): mark test to run only on named environment")
    config.addinivalue_line("markers", "skip_env(name): mark test to skip only on named environment")
    config.addinivalue_line("markers", "on_browser(name): mark test to run only on named browser")
    """ add env properties to allure report """
    alluredir = config.getoption("--alluredir")
    br_name = config.getoption("--browser_name")
    env_properties = dict({"ENV": ENV_PARAM, "BASE_URL": BASE_URL, "BROWSER": br_name})
    add_allure_environment_properties(alluredir, env_properties)

@pytest.fixture(scope='class')
def desktop(request):
    # 1 - prepare webdriver instance
    headless = eval(request.config.getoption("--headless"))
    browser_name = request.config.getoption("--browser_name")
    browser_version = request.config.getoption("--browser_version")
    hub = eval(request.config.getoption("--hub"))
    driver = Driver(browser_name=browser_name, version=browser_version, headless=headless, hub=hub)
    # 2 - setup browser
    browser = BasePage(driver.get_driver())
    browser.goto('/')
    # 3 - make browser available
    yield browser
    # 4 - teardown browser
    browser.quit()

@pytest.fixture(scope='class')
def fake():
    from modules.Faker import Fake
    yield Fake
