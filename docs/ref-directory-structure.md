# Directory Structure

Names of directories and config files in this repository are mostly based on common conventions and requirements by specific development tools, with few custom ideas added on top:

- `.continue`: Configuration for [Continue.dev](https://github.com/continuedev/continue) AI coding assistant (models, MCPs, etc.)
- `.github`: GitHub-specific files (mostly CI pipelines)
- `.roo`: Configuration for [RooCode](https://github.com/RooCodeInc/Roo-Code) AI coding assistant (models, MCPs, etc.)
- `.venv`: Python virtual environment (*not checked out in Git*)
- `app`: Executable scripts for GUIs, CLIs and APIs (based on library code in `src`)
- `deploy`: Configuration for deploying Web GUIs and APIs on a server
- `docs`: Source files (mostly Markdown) for project documentation (how-tos, API-reference, explanations, etc.)
- `src`: Source code for the core library modules
- `test`: Code for automated testing of library modules (via [pytest](https://pypi.org/project/pytest/))
- `.dockerignore`: Files to ignore when building a container image
- `.gitignore`: Files to ignore when commiting into the Git repository
- `.gitlab-ci.yml`: GitLab-specific CI pipelines
- `.releaserc.yml`: Configuration for auto-generating releases based on commits (via [semantic-release](https://github.com/semantic-release/semantic-release))
- `AGENTS.md`: Common, repo-specific system prompt for all AI agents.
- `Brewfile`: System-dependencies for development on MacOS or Linux (installable via [Homebrew](https://github.com/Homebrew/brew))
- `configuration.winget`: System-dependencies for development on Windows (installable via [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/))
- `pyproject.toml`: Central Python project config ([PyPI](https://pypi.org/) dependencies, name, authors, linting config, etc.)
- `README.md`: Main description of the repository
- `uv.lock`: Exact dependency versions determined by UV (generated file)
