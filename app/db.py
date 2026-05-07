"""Common database code and persistent application state."""

import os
from pathlib import Path

from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine

_engine: Engine | None = None


def get_sql_engine() -> Engine:
    """Return the singleton SQLAlchemy engine, create if necessary."""
    global _engine
    if _engine is None:
        if not Path("data").exists():
            Path("data").mkdir()

        _engine = create_engine(
            os.environ.get("APP_DB_URL", "sqlite:///data/local.db"),
        )
        SQLModel.metadata.create_all(_engine)

    return _engine
