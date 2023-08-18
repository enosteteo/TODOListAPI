# syntax=docker/dockerfile:1

FROM python:3.11.4-slim-bookworm
WORKDIR /usr/api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "-m", "flask", "--app", "app", "run", "--debug", "--host=0.0.0.0"]
