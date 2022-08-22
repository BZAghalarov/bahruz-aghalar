FROM python:3.9.7-slim

COPY . /cedarsystems
WORKDIR /cedarsystems

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt