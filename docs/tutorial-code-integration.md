# Tutorial for integrating custom code modules

You can use your own (simple) Python module for this tutorial or rely on the provided example in this repo. For the latter, please switch to the `tutorial-code-integration` branch before you continue.

> You should be familiar with VSCode and RooCode basics for this. See respective tutorials.

This will mostly be a series of prompts to be put into the Roo chat with a bit of extra explanation. Be sure to check out the other docs to find more information about what's going on.

## 1. Add missing dependencies

> This is a pattern for deferred function execution, where you first collect the args as attributes of an object and then execute via a dedicated method. It is rather optional but makes integrating with SQL data-storage easier.

- **File Context**: (Enter `@` in Roo chat and select file in menu)
  - Entire `/src/tube_backpressure.py`
  - Entire `/src/hello_world.py`
- **Prompt**: Convert the function `tube_backpressure` into a pydantic dataclass to enable deferred execution. Name the class `TubeFluidics` and the method for calculating the backpressure `calc_backpressure`.

## 2. Create Typer CLI command

- **File Context**: (Enter `@` in Roo chat and select file in menu)
  - Entire `/src/tube_backpressure.py`
  - Entire `/app/cli` folder
- **Prompt**: Add another Typer CLI command as a separate file in `/app/cli/commands`, which exposes the `TubeFluidics.calc_backpressure` function.

## 3. Create FastAPI route

- **File Context**: (Enter `@` in Roo chat and select file in menu)
  - Entire `/src/tube_backpressure.py`
  - Entire `/app/rest_api` folder
- **Prompt**: Add another FastAPI router as a separate file in `/app/rest_api/routes`, which derives a SQLModel subclass of `TubeFluidics` for database storage and allows for creating, listing and editing of these object via the API. Add a sub-path to expose the `calc_backpressure` method.

## 4. Create Streamlit page

- **File Context**: (Enter `@` in Roo chat and select file in menu)
  - Entire `/src/tube_backpressure.py`
  - Entire `/app/web_gui` folder
- **Prompt**: Add another Streamlit page as a separate file in `/app/web_gui/pages`, which exposes the `TubeFluidics.calc_backpressure` method via a form + submit button + simple display of the returned result.

## 5. Run quality checks to see if code is good

See [how to page](./how-to-check-quality.md).

## 5. Deploy locally to test

See [how to page](./how-to-deploy-locally.md).
