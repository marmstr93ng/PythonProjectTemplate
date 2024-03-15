# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Requirements

- **Python 3**
- **Python virtual environment** - Setup a folder called `.venv` with `python -m venv .venv` and activate with `.\\.venv\\Scripts\\activate`
- **Dependencies** - Installed by running `pip install -e .[dev]` (remember to do so from inside a virtual environment)
- **Setup Pre-commit hooks** - run `pre-commit install`

## Launching

- To launch via **Python**, call `python src/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.py` from within the virtual environment.
