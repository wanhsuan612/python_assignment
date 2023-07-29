FROM python:3.10-slim

WORKDIR /opt

COPY . /opt

RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

EXPOSE 5000