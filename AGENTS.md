# AGENTS.md

## Project type

This is a full-stack Python project, meaning it provides pure library code in `/src` and multiple application interfaces in `/app` (Typer CLI, Jupyter Notebooks, FastAPI, Streamlit UI). It is managed by `uv` wiht main config defined in the `/pyproject.toml`.

## Tooling and coding conventions

- VSCode tasks are defined in `/.vscode/tasks.json` and used extensively for dev-tooling. They can be executed via `vtr TASK_NAME` in the terminal as well (provided by vscode-task-runner package).
- `ruff` is used for linting (config in `pyproject.toml`)
- `black` is used for formatting
- `pyright` is used for type-checking (via PyLance; config in `pyproject.toml`)
- Modern typehints should be used throughout the code and all functions, methods and classes should have Google-style docstrings
- Files are formatted on save
- `pytest` is used for testing (test inn `/test`; config in `pyproject.toml`)
- `properdocs` is used for docs generation
  - config in `/docs/.config.yml`
  - `mkdosctring.python` for API docs
  - `properdocs` = maintained `mkdocs` successor
- dependencies in `pyproject.toml` are split into multiple groups
- `deptry`, `pip-audit` and `licensecheck` are used to check dependency compatibility & health

## CI

- CI pipelines for both GitHub and GitLab exist
- Checks are run on every push to main or every pull request event, involving most of aforementioned tooling
- Semantic-release is run on every push to main, leveraging gitmoji semantics to determine version numbers

## Deployment

The `Dockerfile` and `compose.yaml` in `/deploy` can be used together to deploy a combined webapp with the FastAPI REST API, Streamlit UI, docs pages and postgres for persistence. These can be used standalone or witha tool like Coolify.

## The Agent's Job

Your main job is to assist with improving the quality of code in `/src` (ideally making them pass the CI checks), and help write *glue code* for app interfaces in `/app`.

## Further Infos

Have a look at the Markdown files inside `/docs`, if further infos are required. The docs are structured using the Diataxis framework.
