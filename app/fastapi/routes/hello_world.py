"""REST API for the Hello-World Greeter."""

from collections.abc import Sequence

from fastapi import APIRouter, HTTPException
from sqlmodel import Field, Session, SQLModel, select

from src.hello_world import Greeter as GreeterModel

from ..db import get_sql_engine


class Greeter(SQLModel, GreeterModel, table=True):
    """Persisted version of the Greeter class."""

    id: int | None = Field(default=None, primary_key=True)


router = APIRouter()
engine = get_sql_engine()


@router.post("/greeters/")
def _(greeter: Greeter) -> Greeter:
    with Session(engine) as session:
        session.add(greeter)
        session.commit()
        session.refresh(greeter)
        return greeter


@router.get("/greeters/")
def _() -> Sequence[Greeter]:
    with Session(engine) as session:
        return session.exec(select(Greeter)).all()


@router.get("/greeters/{greeter_id}")
def _(greeter_id: int) -> Greeter:
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
