FROM python:3.9-slim-buster
WORKDIR /
ADD subscriber.py /
RUN pip install paho-mqtt