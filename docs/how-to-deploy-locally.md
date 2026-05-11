# How to deploy locally

This document explains how to deploy a combined webapp with the FastAPI REST API, Streamlit UI, docs pages and postgres for persistence on the localhost.

1. Make sure you have [compose set up in Podman-Desktop](https://podman-desktop.io/docs/compose/setting-up-compose).
2. Run the dedicated `deploy-local` task in VSCode (`Ctrl` + `Shift` + `P`, then search for *Run task*).

You should now be able to access the following websites via your browser:

- [`http://localhost:7000`](http://localhost:7000): Streamlit Web UI
- [`http://localhost:8000/docs)`](http://localhost:8000/docs): FastAPI REST API Docs (for API running on [`http://localhost:8000)`](http://localhost:8000))
- [`http://localhost:9000`](http://localhost:9000): Repository Docs

To tear everything down, hit `CTRL` + `C` a couple of times from within the VSCode terminal where the local deployment is running.
