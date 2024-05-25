DOIT_CONFIG = {"default_tasks": ["lint", "test"]}


def task_lint():
    """run linter on the project using flake8, black and isort"""
    yield {
        "name": "flake8",
        "actions": ["flake8"],
    }
    yield {
        "name": "black-check",
        "actions": ["black  --check ."],
    }
    yield {
        "name": "isort-check",
        "actions": ["isort --check ."],
    }


def task_format():
    """format the code"""
    return {"actions": ["isort .", "black ."]}


def task_test():
    """run unit tests"""
    return {"actions": ["python3 -m unittest discover"]}