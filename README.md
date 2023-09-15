# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):


## Running with Docker Compose

Setup is simple with Docker (and Docker compose)! Simply run:
```bash
docker compose up development
```
to start the development server, which will auto reload on file changes.

To run the production server (using Gunicorn), instead run:
```bash
docker compose up production
```

Either of these servers can be accessed at: http://localhost:8000

## Prebuilt Docker Images

Prebuilt production ready images can be found on Docker Hub: https://hub.docker.com/repository/docker/jdhprojects/devops-course-starter/general

## Azure Hosted todo-app

The todo-app is hosted using azure here: https://jp-todo-app-module-7.azurewebsites.net/

### Updating the Azure app

Login to docker:
```
docker login
```

Build the production image and tag it:
```
docker build --target production --tag jdhprojects/devops-course-starter:prod .
```

Push to Docker Hub:
```
docker push jdhprojects/devops-course-starter:prod
```

Redeploy the Azure web app:
```
curl -dH -X POST "<webhook url with escaped $>"
```

## Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

## Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Deploying with Ansible

This project is setup to be able to be deployed using Ansible. To deploy, run the following:

```bash
$ ansible-playbook playbook.yaml -i inventory.yaml
```
This will prompt you for three values:
* Flask secret key
* Trello token
* Trello API key

Inputting these values will allow ansible to deploy the app. Board IDs are currently hardcoded for convenience into the Jinja template as these values are non-sensitive.

You should now be able to view the hosted app at http://3.11.233.49:5000

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

## Environment Configuration
You'll need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Some additional variables are required to be able to integrate with Trello:
* `TRELLO_TOKEN` - Trello token
* `TRELLO_API_KEY` - Trello API key
* `TRELLO_BOARD_ID` - Board to hold both below lists
* `TRELLO_COMPLETED_LIST` - List to hold completed tasks
* `TRELLO_NOT_STARTED_LIST` - List to hold not yet started tasks
* `TRELLO_IN_PROGRESS_LIST` - List to hold in progress tasks

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing

All tests can be executed with `poetry run pytest`
