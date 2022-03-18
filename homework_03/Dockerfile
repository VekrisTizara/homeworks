FROM python:3.9.9-buster

ENV PYTOHNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-ansi

CMD uvicorn fastapi_app:app --host=0.0.0.0 --port=8000
