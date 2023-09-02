from allure import step
from src.pages.base_page import BasePage


class HoversPage:
    def __init__(self, driver):
        self.page = BasePage(driver)

    locHoversDiv = '//div[@class="example"]'

    def hover_on_img(self, name: str):
        locItem = f'{self.locHoversDiv}/div[.//*[contains(text(),"{name}")]]/img'
        self.page.mouse_hover(locItem)
    
    def get_img_tip(self, name: str):
        locItemTip = f'{self.locHoversDiv}/div[.//*[contains(text(),"{name}")]]/div/h5'
        value = self.page.get_text(locItemTip)
        return value