from conf_file import BASE_URL
from allure import step
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from src.pages.browser_page import BrowserPage
from datetime import datetime, timedelta


class BasePage(BrowserPage):
    def __init__(self, driver):
        super().__init__(driver)

    #################################################################
    # WAITS #
    @step('wait_for_time')
    def wait_for_time(self, time: float):
        sleep(time)

    @step('wait_element_is_visible')
    def wait_element_is_visible(self, locator: str, timeout: float = 10):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout)
            wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception:
            raise TimeoutError(f'Element not visible after {timeout}s: {locator}')

    @step('wait_element_is_not_visible')
    def wait_element_is_not_visible(self, locator, timeout: float = 10):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout)
            wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))
        except Exception:
            raise TimeoutError(f'Element still visible after {timeout}s: {locator}')

    @step('wait_element_is_clickable')
    def wait_element_is_clickable(self, locator: str, timeout: float = 10):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout)
            wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        except Exception:
            raise TimeoutError(f'Element not clickable after {timeout}s: {locator}')

    @step('wait_page_loading')
    def wait_page_loading(self, timeout: int = 10):
        start_time = datetime.now()
        self.driver.execute_script('return document.readyState')
        end_time = datetime.now()
        load_time = end_time - start_time
        if end_time > start_time + timedelta(seconds=timeout):
            raise TimeoutError(f'Page loaded more than {timeout}s - load_time={load_time.total_seconds()}')

    #################################################################
    # BASE METHODS #
    @step('goto')
    def goto(self, endpoint: str, use_base_url: bool = True):
        if use_base_url:
            self.driver.get(BASE_URL + endpoint)
            self.wait_page_loading()
            self.wait_for_time(2)  # wait fo page loading finish
        else:
            self.driver.get(endpoint)
            self.wait_page_loading()

    @step('switch_to_window_new')
    def switch_to_window_new(self):
        windows_list = self.driver.window_handles
        if len(windows_list) == 1:
            raise Exception('New window not found')
        self.driver.switch_to.window(windows_list[-1])

    @step('close_current_window')
    def close_current_window(self):
        self.driver.close()

    @step('switch_to_window_main')
    def switch_to_window_main(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[0])

    @step('switch_to_iframe')
    def switch_to_iframe(self, name_or_index):
        self.driver.switch_to.frame(name_or_index)

    @step('switch_to_iframe_by_locator')
    def switch_to_iframe_by_locator(self, locator: str):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, locator))

    @step('switch_to_default_content')
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    @step('page_clear_cookies')
    def page_clear_cookies(self):
        self.driver.delete_all_cookies()

    @step('page_clear_local_storage')
    def page_clear_local_storage(self):
        self.driver.execute_script("window.localStorage.clear();")

    @step('page_add_cookies')
    def page_add_cookies(self, cookie_dict: dict):
        self.driver.add_cookie(cookie_dict)

    @step('page_location')
    def page_location(self):
        return self.driver.current_url

    @step('page_title')
    def page_title(self):
        return self.driver.title

    @step('page_contains_text')
    def page_contains_text(self, text: str):
        return self.driver.page_source.__contains__(text)

    @step('page_refresh')
    def page_refresh(self):
        self.driver.refresh()
        try:
            self.driver.switch_to.alert.accept()  # accept page reload
        except Exception:
            pass
        self.switch_to_default_content()
        self.wait_page_loading()

    @step('get_text')
    def get_text(self, locator: str):
        _value = self.driver.find_element(By.XPATH, locator).text
        value = " ".join(_value.split())  # need for safari
        return value

    @step('input_text')
    def input_text(self, locator: str, value):
        """
        insert all text at once
        """
        self.driver.find_element(By.XPATH, locator).clear()
        self.driver.find_element(By.XPATH, locator).send_keys(value)

    @step('type_text')
    def type_text(self, locator: str, value):
        """
        inserting text character by character
        """
        el = self.driver.find_element(By.XPATH, locator)
        action = ActionChains(self.driver)
        action.send_keys_to_element(el, value).perform()

    @step('clear_text')
    def clear_text(self, locator: str):
        self.driver.find_element(By.XPATH, locator).clear()

    @step('clear_value')
    def clear_value(self, locator: str):
        self.driver.execute_script(f'document.evaluate(`{locator}`, '
                                   f'document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, '
                                   f'null).singleNodeValue.value=""')

    @step('is_element_visible')
    def is_element_visible(self, locator: str, timeout: float = 5):
        try:
            self.wait_element_is_visible(locator, timeout)
            return True
        except Exception:
            return False

    @step('click_element')
    def click_element(self, locator: str):
        self.driver.find_element(By.XPATH, locator).click()

    @step('click_element_by_js')
    def click_element_by_js(self, locator: str):
        loc = locator.replace("'", "\'")
        self.driver.execute_script(f'let elem = document.evaluate(`{loc}`, document, null, '
                                   f'XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; elem.click();')

    @step('upload_file')
    def upload_file(self, locator: str, file_path: str):
        self.driver.find_element(By.XPATH, locator).send_keys(file_path)

    @step('mouse_hover')
    def mouse_hover(self, locator: str):
        el = self.driver.find_element(By.XPATH, locator)
        action = ActionChains(self.driver)
        action.move_to_element(el).perform()
        self.wait_for_time(0.5)

    @step('click_and_hold_element')
    def click_and_hold_element(self, locator: str):
        el = self.driver.find_element(By.XPATH, locator)
        action = ActionChains(self.driver)
        action.move_to_element(el).perform()
        action.click_and_hold(el).perform()
        self.wait_for_time(1)
        action.release(el).perform()

    @step('drag_and_drop_by_x_y')
    def drag_and_drop_by_x_y(self, locator: str, x: float = 0, y: float = 0):
        draggable = self.driver.find_element(By.XPATH, locator)
        action = ActionChains(self.driver)
        try:
            action.drag_and_drop_by_offset(draggable, x, y).release().perform()
        except Exception:
            pass

    @step('get_element_attribute')
    def get_element_attribute(self, locator: str, attr: str):
        value = self.driver.find_element(By.XPATH, locator).get_attribute(attr)
        return value

    @step('get_element_count')
    def get_element_count(self, locator: str):
        value = len(self.driver.find_elements(By.XPATH, locator))
        return value

    @step('get_element_object')
    def get_element_object(self, locator: str):
        return self.driver.find_element(By.XPATH, locator)

    @step('scroll_into_view')
    def scroll_into_view(self, locator: str):
        el = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

    @step('scroll_page_to_element')
    def scroll_page_to_element(self, locator: str):
        el = self.driver.find_element(By.XPATH, locator)
        desired_y = (el.size['height'] / 2) + el.location['y']
        window_h = self.driver.execute_script('return window.innerHeight')
        window_y = self.driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    @step('scroll_page_to_top')
    def scroll_page_to_top(self):
        self.driver.execute_script("window.scrollTo(0,0);")

    @step('scroll_page_to_bottom')
    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    @step('press_key_ESC')
    def press_key_ESC(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ESCAPE)
        action.key_up(Keys.ESCAPE)
        action.perform()

    @step('press_key_TAB')
    def press_key_TAB(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.TAB)
        action.key_up(Keys.TAB)
        action.perform()

    @step('press_key_RETURN')
    def press_key_RETURN(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.RETURN)
        action.key_up(Keys.RETURN)
        action.perform()