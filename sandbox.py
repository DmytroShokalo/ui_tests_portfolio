from selenium import webdriver

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
pytest --browser_name firefox --hub True --browser_version 116.0 tests/test_dropdown_list.py
pytest --browser_name firefox --browser_version 100.0 -n 3 --dist loadscope tests/test_dropdown_list.py
pytest --browser_name chrome --hub True --browser_version 115.0 -n 3 --dist loadscope tests/
pytest --browser_name chrome --hub True --browser_version 110.0 -n 3 --dist loadscope tests/
"""