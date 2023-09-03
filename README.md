# ui_elements_framework
UI framework for selenium practice

Clone project from GIT

```bash
git clone git@github.com:your_project.git
cd your_project
```

Install requirements

```bash
pip install -r requirements.txt
```

For Mac M1 install webdriver and store it in /usr/local/bin/

## Running Tests (locally)

To run tests via native browser, run the following command
```bash
pytest --headless False tests/{path_to_test_folder_or_file}
```

To run tests in parallel (used [xdist](https://pypi.org/project/pytest-xdist/)), run the following command
```bash
pytest -n 6 --dist loadscope tests/{path_to_test_folder_or_file}
```

To set up selenoid env, download suitable [cm_file](https://github.com/aerokube/cm/releases) in ./selenoid/ 
And run command
```bash
source /selenoid/selenoid_helper.sh
```

To run tests via selenoid, run the following command
```bash
pytest --hub True tests/
```

## Project Structure

#### Folders

| Name            | Desc                                                       |
|:----------------|:-----------------------------------------------------------|
| `configs`       | configuration files for different ENV (dev.py, stage.py …) |
| `modules`       | libraries for working with various services, libraries …   |
| `src/elements`  | page_elements for UI                                       |
| `src/pages`     | page_objects for  UI                                       |
| `tests/`        | UI tests                                                   |                       |

#### Files

| Name               | Desc                                                 | 
|:-------------------|:-----------------------------------------------------|
| `conf_file.py`     | main configuration file                              |       
| `conftest.py`      | pytest configuration (options, fixtures...)              |
| `requirements.txt` | list of libraries which are required for the project |

