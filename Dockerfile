FROM python:buster as base

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH
COPY pyproject.toml poetry.toml /
RUN poetry install

FROM base as production

COPY todo_app /todo_app

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0", "todo_app.app:create_app()"]

FROM base as development

EXPOSE 5000
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
