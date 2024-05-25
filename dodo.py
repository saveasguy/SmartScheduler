DOIT_CONFIG = {"default_tasks": ["lint", "test"]}


def task_lint():
    """Run linter on the project using flake8, black and isort."""
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
    yield {
        "name": "docformatter-check",
        "actions": ["docformatter --recursive --check ."],
    }


def task_format():
    """Format the code."""
    return {"actions": ["isort .", "black .", "docformatter --recursive ."]}


def task_docupdate():
    """Update documentation."""
    return {"actions": ["sphinx-apidoc -f -o docs/source scheduler"]}


def task_doc():
    """Build documentation."""
    return {
        "actions": ["sphinx-build -M html docs/source docs/build"],
        "task_dep": ["docupdate"],
    }


def task_test():
    """Run unit tests."""
    return {"actions": ["python3 -m unittest discover"]}
