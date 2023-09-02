from allure import step
from src.pages.base_page import BasePage
import conf_file as cfg

class MenuPage:
    def __init__(self, driver) -> object:
        self.page = BasePage(driver)

    locAddRemoveElementsLnk = ''
    locBasicAuthLnk = ''
    locBrokenImgLnk = ''
    locChallengingDOMLnk = ''

    @step("navigate_to")
    def navigate_to(self, menu_name: str):
        """ This method allows you to navigate through menu items
        :param menu_name: the menu item name
        """
        loc = f'//a[contains(text(),"{menu_name}")]'
        self.page.wait_element_is_visible(loc, timeout=10)
        self.page.scroll_page_to_element(loc)
        self.page.wait_for_time(1)
        self.page.click_element(loc)
        self.page.wait_page_loading()