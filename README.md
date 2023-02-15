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
## Running Tests (locally)

To run tests, run the following command
```bash
pytest --headless False tests/{path_to_test_folder_or_file}
```

To run tests in parallel (used [xdist](https://pypi.org/project/pytest-xdist/)), run the following command
```bash
pytest -n 6 --dist loadscope tests/{path_to_test_folder_or_file}
```

## Project Structure

#### Folders

| Name            | Desc                                                                                     |
|:----------------|:-----------------------------------------------------------------------------------------|
| `configs`       | файли кофігурацій для різних ENV (dev.py, stage.py …)                                    |
| `modules`       | бібліотеки для роботи з різними сервісами, бібліотеками …                                |
| `src/elements`  | page_elements для UI                                                                     |
| `src/pages`     | page_objects для UI                                                                      |
| `tests/`        | тести UI                                                                                 |                       |

#### Files

| Name               | Desc                                    | 
|:-------------------|:----------------------------------------|
| `conf_file.py`     | основний файл конфігурації              |       
| `conftest.py`      | конфігурація pytest (опції, фікстури …) |
| `requirements.txt` | бібліотеки необхідні для проекту        |

