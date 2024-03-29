FROM python:buster as base

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH
COPY pyproject.toml poetry.toml /app/
RUN poetry install

FROM base as production

COPY todo_app todo_app

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0", "todo_app.app:create_app()"]

FROM base as development

EXPOSE 5000
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as test

COPY todo_app todo_app
ENTRYPOINT ["poetry", "run", "pytest", "todo_app"]

FROM base as check-format

COPY . .
ENTRYPOINT ["poetry", "run", "pre-commit", "run", "--all-files"]
