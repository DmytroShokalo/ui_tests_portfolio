from allure import step
from src.pages.base_page import BasePage
from src.elements.checkbox import CheckboxElement

class FileUploadPage:
    def __init__(self, driver):
        self.page = BasePage(driver)

    locUploadButton = '//input[@id="file-upload"]'

    @step('upload_file')
    def upload_file(self):
        self.page.click_element(self.locUploadButton)
