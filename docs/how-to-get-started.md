# How to get started

> ⚠️ mind all the inline links. They are helpful :-)

There are a few setup steps needing to be done before you can start using this repo and pasting your own code in.

## 1. System setup

A handful of applications need to be installed directly onto your OS. These are all listed in files contained within this repo, which can be directly parsed by a package manager. Exact steps depend on which OS you have:

### Windows

Download the file `configuration.winget` from the repo's top-level directory, open a [PowerShell terminal](https://learn.microsoft.com/en-au/answers/questions/5863977/how-to-access-power-shell-on-win-11), `cd` to your download folder, and run this command:

```powershell
winget configure -f configuration.winget
```

### MacOS or Linux

1. Install [Homebrew](https://brew.sh/)
2. Download the file `Brewfile` from the repo's top-level directory
3. Open a terminal, `cd` to your download folder, and run this command:

  ```bash
  brew bundle install --file Brewfile
  ```

## 2. Clone Git repo via VSCode

See this [offical guide](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes#_clone-repositories).

## 3. Install all recommended VSCode extensions

VSCode should prompt you for exactly that right after cloning the repo. If so, click *Yes*. If not, go to the extensions tab in the left sidebar, enter `@recommended` in the search bar and install all manually.

## 4. Install all Python dependencies via UV

[Open an integrated terminal](https://code.visualstudio.com/docs/terminal/basics#_terminals-in-editor-area) in VSCode and enter `uv sync`. This should rather quickly install all required packages, as defined in `pyproject.toml`.

> If you have trouble executing `uv` in the terminal, try installing it again [via the official script](https://docs.astral.sh/uv/#__tabbed_1_2).

## 5. Configure AI assistants

1. Close and re-open the VSCode window to make sure that all required background tasks are running.

    > A few terminals always pop up when opening the repo in VSCode. No need to be alarmed. They can be closed once all tasks within are done.

2. Go to the *Continue* tab and select the `autocomplete.yaml` config:

    ![alt text](img/continue-autocomplete.png)

3. Go to the *Roo Code* tab, enter settings menua via top-right gear icon ⚙️, and create a new cofiguration profile with details as given by below image. If using the KI-Toolbox by KIT SCC, you can follow [this tutorial](https://www.zml.kit.edu/downloads/KI.Toolbox_API.pdf) (page 4) to generate your API key. Don't forget to hit *Save*.

    ![alt text](img/roo-config.png)

4. Go back to the Roo chat interface by clicking the pencil icon ✏️ on the top, then click on the bottom right database icon. In the open menu, enter details as given by the image below, then hit *Save* and finally *Start Indexing*. The database icon must turn green after some time, if it worked.

    ![alt text](img/roo-indexing-config.png)

> **That's it! Now you should be good to go! 🎉**

## How to continue

- **New to VSCode or IDEs in general?** Check out [the mini VSCode tutorial](./tutorial-ide-vscode.md).
- **New to Roo Code or AI dev assistants in general?** Have a look at [what Roo can doo](./tutorial-roo-code.md) in this repo.
- **Want to get started right away with integrating your code / modules?** Head on over to the [code integration tutorial](./tutorial-code-integration.md).
