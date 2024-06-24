FROM python:3.10

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY ./app /app/app

COPY ./data /app/data

COPY ./models /app/models

EXPOSE 80

CMD ["poetry", "run", "flask", "--app=app/app.py", "run", "--host=0.0.0.0", "--port=80"]

