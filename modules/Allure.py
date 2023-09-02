from os import path
import json
import allure
from bs4 import BeautifulSoup
from datetime import datetime


def add_allure_environment_properties(alluredir=None, properties: dict = None):
    if not alluredir or not path.isdir(alluredir) or not properties:
        return
    allure_env_path = path.join(alluredir, "environment.properties")
    with open(allure_env_path, 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in properties.items()])
        _f.write(data)


def log_html_to_allure(content, name: str):
    allure.attach(content,
                  name=f"{name}_content",
                  attachment_type=allure.attachment_type.HTML)


def log_text_to_allure(text, name: str = 'value'):
    allure.attach(str(text),
                  name=name,
                  attachment_type=allure.attachment_type.TEXT)


def log_response_to_allure(resp):
    try:
        allure.attach(_html_format(resp),
                      name=f"{resp.status_code} {resp.request.method} {resp.url}",
                      attachment_type=allure.attachment_type.HTML)
    except Exception:
        pass


def log_console_entire_to_allure(entire):
    entire_time = datetime.fromtimestamp(entire['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
    allure.attach(__dict_to_html(entire),
                  name=f"Console entire ({entire['level']}) - {entire_time}",
                  attachment_type=allure.attachment_type.HTML)


def _html_format(resp):
    if isinstance(resp.request.body, bytes):
        request_body = resp.request.body.decode('utf-8')
    else:
        request_body = resp.request.body
    _html = f"""
    <div style="border:solid;border-color:#41444e;border-radius:10px;background-color:#EBF3FB;padding:10px;white-space:normal">
        <div>
            {__h1_to_html(f"{resp.request.method} Request")}
            <div style="width:96%;padding:15px;border-radius:10px;background:#41444e;color:#fff;">{resp.request.url}</div>
            {__h2_to_html("Request headers")}
            {__dict_to_html(resp.request.headers)}
            {__h2_to_html("Request cookies")}
            {__dict_to_html(resp.request._cookies.get_dict())}
            {__h2_to_html("Request body")}
            {__dict_to_html(request_body)}
        </div>
        <hr>
        <div>
            {__h1_to_html("Response")}
            {__status_code_to_html(resp.status_code)}
            {__h2_to_html(f"{resp.elapsed.total_seconds()} total seconds")}
            {__h2_to_html("Response headers")}
            {__dict_to_html(resp.headers)}
            {__h2_to_html("Response cookies")}
            {__dict_to_html(resp.cookies.get_dict())}
            {__h2_to_html("Response body")}
            {__data_to_html(resp)}
        </div>
    </div>
    """
    return _html


def __h1_to_html(text):
    _style = "line-height:0;font-size:20px;margin:1%;font-weight:600;padding-bottom:10px;"
    return f"""<div style="{_style}">{text}</div>"""


def __h2_to_html(text):
    _style = "line-height:0;font-size:14px;margin:1%;font-weight:600;padding-bottom:10px;"
    return f"""<div style="{_style}">{text}</div>"""


def __status_code_to_html(status_code):
    if str(status_code).startswith('4') or str(status_code).startswith('5'):
        _color = "#880202"
    else:
        _color = "#008640"
    _html = f"""<div style="color:{_color};font-size:20px;margin:1%;font-weight:600;">{status_code}</div>"""
    return _html


def __dict_to_html(_dict):
    if _dict is None:
        _rows_content = ""
    else:
        try:
            _dict = dict(_dict)
            _rows_content = json.dumps(_dict, indent=2)
            _rows_content = _rows_content.replace("\n", "<br />")
            _rows_content = _rows_content.replace("  ", "&emsp;")
        except Exception:
            _rows_content = str(_dict)

    _style = "width:92%;padding:15px;margin-left:4%;margin-bottom:8px;border-radius:10px;background:#41444e;color:#fff;font-size:12px;"
    _html = f"""<div style="{_style}">{_rows_content}</div>"""
    return _html


def __data_to_html(resp):
    def remove_style_from_html(error_html):
        soup = BeautifulSoup(error_html, "html.parser")
        for style in soup(["style"]):
            style.extract()
        return str(soup)

    resp_text = resp.text
    if "content-type" in resp.headers.keys():
        if "application/json" in resp.headers['content-type']:
            _html = __dict_to_html(resp.text)
            return _html
        else:
            resp_text = remove_style_from_html(resp_text)
            _style = "border:solid;border-color:#41444e;border-radius:10px;width:92%;padding:15px;margin-left:4%;"
            _html = f"""<div style="{_style}">{resp_text}</div>"""
            return _html
