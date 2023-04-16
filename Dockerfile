FROM python:3.7-slim


ENV PYTHONBUFFERED=2
WORKDIR /app/


COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt