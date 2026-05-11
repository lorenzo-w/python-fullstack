FROM ghcr.io/astral-sh/uv:alpine AS base

WORKDIR /app
COPY pyproject.toml uv.lock ./

ARG DEPS_GROUP=dev
RUN --mount=type=cache,target=/root/.cache/uv uv sync --group ${DEPS_GROUP} --no-install-project

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv uv sync --group ${DEPS_GROUP}

FROM base AS vtr

ENTRYPOINT ["uv", "run", "vtr"]

FROM base as docs

ARG SITE_URL="http://0.0.0.0:9000"
RUN uv run vtr build-docs

FROM docker.io/nginx:stable AS nginx-docs

COPY --from=docs /app/dist/docs /usr/share/nginx/html

FROM base AS cli

ENTRYPOINT ["uv", "run", "cli"]