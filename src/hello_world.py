"""Demo module for producing hello world output with additional info."""

from datetime import datetime

import requests
from pydantic.dataclasses import dataclass
from structlog.stdlib import get_logger

logger = get_logger()


@dataclass
class Greeter:
    """Class for saying hello."""

    name: str
    """Name of the greeter."""

    correspondent: str = "world"
    """Name of the one who is greeted."""

    tell_time: bool = True
    """Tell the current time along with the greeting."""

    tell_weather: bool = False
    """Inform about the current weather along with the greeting."""

    weather_location: tuple[float, float] = 48.42167, 8.2345051
    """Location coordinates (lat, lon) to tell the weather for."""

    @property
    def _weather_url(self) -> str:
        return (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.weather_location[0]}"
            f"&longitude={self.weather_location[1]}&current=temperature_2m"
        )

    def _gen_weather_text(self) -> str:
        info = requests.get(self._weather_url).json()
        logger.debug("Received weather info", info=info)

        temp: float = info["current"]["temperature_2m"]

        opinion = "hot" if temp > 30 else "comfortable" if temp > 15 else "chilly"
        return f" It's {opinion} {round(temp)} °C outside."

    def say_hello(self) -> str:
        """Return a greet with a hello and optional info about time or weather."""
        greeting = f"Hello {self.correspondent}, {self.name} here!"

        if self.tell_time:
            greeting += f" The current time is {datetime.now().strftime('%H:%M:%S')}."

        if self.tell_weather:
            greeting += self._gen_weather_text()

        return greeting
