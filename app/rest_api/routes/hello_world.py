"""REST API for the Hello-World Greeter."""

from collections.abc import Sequence

from fastapi import APIRouter, HTTPException
from sqlalchemy import JSON
from sqlmodel import Column, Field, Session, SQLModel, select

from app.db import get_sql_engine
from src.hello_world import Greeter as GreeterModel


class Greeter(SQLModel, GreeterModel, table=True):
    """Persisted version of the Greeter class."""

    id: int | None = Field(default=None, primary_key=True)
    """Auto-generated primary key."""

    # Re-define attribute with explicit SQL datatype.
    weather_location: tuple[float, float] = Field(
        default=(48.42167, 8.2345051), sa_column=Column(JSON)
    )


router = APIRouter()
engine = get_sql_engine()


@router.post("/greeters/")
def _(greeter: Greeter) -> Greeter:
    """Create a new Greeter and save it."""
    with Session(engine) as session:
        session.add(greeter)
        session.commit()
        session.refresh(greeter)
        return greeter


@router.get("/greeters/")
def _() -> Sequence[Greeter]:
    """Get a list of all saved Greeters."""
    with Session(engine) as session:
        return session.exec(select(Greeter)).all()


@router.get("/greeters/{greeter_id}")
def _(greeter_id: int) -> Greeter:
    """Get info on a specific Greeter by id."""
    with Session(engine) as session:
        res = session.exec(
            select(Greeter).where(Greeter.id == greeter_id)
        ).one_or_none()

        if res is None:
            raise HTTPException(status_code=404, detail="Record not found")

        return res


@router.patch("/greeters/{greeter_id}")
def _(
    greeter_id: int,
    correspondent: str | None = None,
    tell_time: bool | None = None,
    tell_weather: bool | None = None,
    weather_location: tuple[float, float] | None = None,
) -> Greeter:
    """Modify a specific Greeter."""
    with Session(engine) as session:
        res = session.exec(
            select(Greeter).where(Greeter.id == greeter_id)
        ).one_or_none()

        if res is None:
            raise HTTPException(status_code=404, detail="Record not found")

        if correspondent is not None:
            res.correspondent = correspondent

        if tell_time is not None:
            res.tell_time = tell_time

        if tell_weather is not None:
            res.tell_weather = tell_weather

        if weather_location is not None:
            res.weather_location = weather_location

        session.commit()
        return res


@router.post("/greeters/{greeter_id}/say-hello")
def _(greeter_id: int) -> str:
    """Make a specific Greeter say hello."""
    with Session(engine) as session:
        res = session.exec(
            select(Greeter).where(Greeter.id == greeter_id)
        ).one_or_none()

        if res is None:
            raise HTTPException(status_code=404, detail="Record not found")

        return res.say_hello()
