"""Common database code and state for all API routes."""

import os

from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine

_engine: Engine | None = None


def get_sql_engine() -> Engine:
    """Return the singleton SQLAlchemy engine, create if necessary."""
    global _engine
    if _engine is None:
        _engine = create_engine(
            f"postgresql://{os.environ['APP_DB_USER']}:{os.environ['SERVICE_PASSWORD_DB']}@{os.environ['APP_DB_HOST']}/{os.environ['APP_DB_DATABASE']}",
        )
        SQLModel.metadata.create_all(_engine)

    return _engine
