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


def task_docupdate():
    """update documentation"""
    return {"actions": ["sphinx-apidoc -f -o docs/source scheduler"]}


def task_doc():
    """build documentation"""
    return {
        "actions": ["sphinx-build -M html docs/source docs/build"],
        "task_dep": ["docupdate"],
    }


def task_test():
    """run unit tests"""
    return {"actions": ["python3 -m unittest discover"]}
