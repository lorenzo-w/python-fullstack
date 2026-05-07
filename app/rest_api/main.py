"""Python FullStack REST API."""

from fastapi import FastAPI

from app.rest_api.routes import hello_world

app = FastAPI()


app.include_router(hello_world.router, prefix="/hello-world")
