# FastAPI Template

This sample repo contains the recommended structure for a Python FastAPI project. In this sample, we use `fastapi` to build a web application and the `pytest` to run tests.

For a more in-depth tutorial, see our [Fast API tutorial](https://code.visualstudio.com/docs/python/tutorial-fastapi).

The code in this repo aims to follow Python style guidelines as outlined in [PEP 8](https://peps.python.org/pep-0008/).

## Set up instructions

This sample makes use of Dev Containers, in order to leverage this setup, make sure you have [Docker installed](https://www.docker.com/products/docker-desktop).

To successfully run this example, we recommend the following VS Code extensions:

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 

In addition to these extension there a few settings that are also useful to enable. You can enable to following settings by opening the Settings editor (`Ctrl+,`) and searching for the following settings:

- Python > Analysis > **Type Checking Mode** : `basic`
- Python > Analysis > Inlay Hints: **Function Return Types** : `enable`
- Python > Analysis > Inlay Hints: **Variable Types** : `enable`

## Running the sample
- Open the template folder in VS Code (**File** > **Open Folder...**)
- Open the Command Palette in VS Code (**View > Command Palette...**) and run the **Dev Container: Reopen in Container** command.
- Run the app using the Run and Debug view or by pressing `F5`
- `Ctrl + click` on the URL that shows up on the terminal to open the running application 
- Test the API functionality by navigating to `/docs` URL to view the Swagger UI
- Configure your Python test in the Test Panel or by triggering the **Python: Configure Tests** command from the Command Palette
- Run tests in the Test Panel or by clicking the Play Button next to the individual tests in the `test_main.py` file

## Environment Variables (Render, Vercel, Server)

To securely use API keys and other secrets, set environment variables in your deployment platform (e.g., Render).

**How to set on Render:**
1. Go to your service in the Render dashboard.
2. Find the **Environment** or **Environment Variables** section.
3. Add a variable named `CP_KEY` and set its value to your CryptoPanic API key.
4. Save and redeploy your service.

**How it works in code:**
The API key is read from the environment using:
```python
import os
key = os.getenv("CP_KEY")
```
If you send the key as a header (`X-CP-KEY`), it will be used instead. Otherwise, the environment variable is used.

**Example endpoint:**
- `/posts` — Proxy to CryptoPanic API, requires `X-CP-KEY` header or `CP_KEY` environment variable.
