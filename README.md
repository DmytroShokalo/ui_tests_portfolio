# ui_elements_framework
UI framework for selenium practice

Clone project from GIT with following command
```bash
git clone git@github.com:your_project.git
cd your_project
```

Install requirements
```bash
pip install -r requirements.txt
```

## Running Tests (locally)

Install webdriver and store it in /usr/local/bin/

To run tests via local browser, run the following command
```bash
pytest --hub False tests/{path_to_test_folder_or_file}
```

To run tests in parallel (used [xdist](https://pypi.org/project/pytest-xdist/)), run the following command
```bash
pytest -n 6 --dist loadscope tests/{path_to_test_folder_or_file}
```

To set up selenoid env, download suitable [cm_file](https://github.com/aerokube/cm/releases) in selenoid_config/ directory 
Then **start Docker service** and run command
```bash
bash selenoid_config/selenoid_helper.sh
```

To run tests via selenoid, run the following command
```bash
pytest --hub True tests/
```
To run tests via selenoid with special browser, run the following command
```bash
pytest --browser_name {browser_name} --hub True tests/
```
To run tests via selenoid with special browser, and special browser version, run the following command
```bash
pytest --browser_name {browser_name} --browser_version {browser_version} --hub True tests/
```

## Project Structure

#### Folders

| Name               | Desc                                                       |
|:-------------------|:-----------------------------------------------------------|
| `configs`          | configuration files for different ENV (dev.py, stage.py …) |
| `modules`          | libraries for working with various services, libraries …   |
| `src/elements`     | page_elements for UI                                       |
| `src/pages`        | page_objects for  UI                                       |
| `tests/`           | UI tests                                                   |                       
| `selenoid_config/` | configuration files for setting up selenoid                |                       

#### Files

| Name               | Desc                                                 | 
|:-------------------|:-----------------------------------------------------|
| `conf_file.py`     | main configuration file                              |       
| `conftest.py`      | pytest configuration (options, fixtures...)              |
| `requirements.txt` | list of libraries which are required for the project |

