from selenium import webdriver
import os
from io import BytesIO
from PIL import Image
from conf_file import BASE_DIR
import requests
import time


class ScrolledScreenshot:

    @staticmethod
    def get_image(driver: webdriver):
        driver.execute_script(f"window.scrollTo({0}, {0})")
        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        rectangles = []
        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height
            if top_height > total_height:
                top_height = total_height
            while ii < total_width:
                top_width = ii + viewport_width
                if top_width > total_width:
                    top_width = total_width
                rectangles.append((ii, i, top_width, top_height))
                ii = ii + viewport_width
            i = i + viewport_height
        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if previous is not None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            file_name = f'{BASE_DIR}/data/temp_screenshots/part_{part}.png'
            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])
            stitched_image.paste(screenshot, offset)
            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle
        buf = BytesIO()
        stitched_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        return byte_im

class Files:

    @staticmethod
    def create_md5(file_path):
        import hashlib
        with open(file_path, 'rb') as file:
            m = hashlib.md5()
            m.update(file.read())
            return m.hexdigest()

    @staticmethod
    def chrome_get_downloaded_files(driver):
        driver.get("chrome://downloads/")
        files_data = driver.execute_script(
            "return Array.from(document.querySelector('downloads-manager').shadowRoot.getElementById('downloadsList')"
            ".querySelectorAll('downloads-item')).map(files => [files.shadowRoot.querySelector('#file-link').text, "
            "files.shadowRoot.querySelector('#url').href]);")

        file_list_with_url_and_name = [
            {'fileName': _file_data[0],
             'url': unquote(_file_data[1]),
             } for _file_data in files_data
        ]
        return file_list_with_url_and_name

    @staticmethod
    def download_file_to_my_path(url, path):
        r = requests.get(url, verify=False, timeout=10)
        time.sleep(3)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()

    @staticmethod
    def pdf_file_get_text(path: str, page_index: int = 0):
        import PyPDF2
        pdf_file = open(path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(page_index)
        text = page.extractText()
        pdf_file.close()
        return text
