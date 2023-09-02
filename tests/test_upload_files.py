from src.pages.menu.menu_page import MenuPage
from src.pages.checkboxes.checkboxes_page import CheckboxesPage
from src.pages.file_upload.file_upload_page import FileUploadPage

"""
Run locally:
    pytest --headless False tests/test_upload_files.py
"""


def test_upload_files(desktop, fake):
	menu = MenuPage(desktop.driver)
	menu.navigate_to('File Upload')
	
	file = FileUploadPage(desktop.driver)
	
	docx_file = fake.file_docx()
	
	file.page.upload_file('//input[@id="file-upload"]', docx_file['path'])
