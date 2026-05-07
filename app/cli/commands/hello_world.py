"""CLI interface for the Hello-World Greeter."""

from typing import Annotated

from typer import Option, Typer

from src.hello_world import Greeter

app = Typer()


@app.command()
def say_hello(
    name: Annotated[str, Option(help="Name of the greeter")],
    correspondent: Annotated[
        str, Option(help="Name of the one who is greeted")
    ] = "world",
    tell_time: Annotated[
        bool, Option(help="Tell the current time along with the greeting")
    ] = True,
    tell_weather: Annotated[
        bool, Option(help="Inform about the current weather along with the greeting")
    ] = False,
    weather_location: Annotated[
        tuple[float, float],
        Option(help="Location coordinates (lat, lon) to tell the weather for."),
    ] = (48.42167, 8.2345051),
) -> None:
    """Create an ad-hoc Greeter and make it say hello."""
    print(
        Greeter(
            name, correspondent, tell_time, tell_weather, weather_location
        ).say_hello()
    )
