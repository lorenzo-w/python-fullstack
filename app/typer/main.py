"""Main CLI script."""

import typer

from .commands import hello_world

app = typer.Typer()

app.add_typer(hello_world.app)

if __name__ == "__main__":
    app()
