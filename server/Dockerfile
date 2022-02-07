FROM ubuntu:20.04

WORKDIR /app

COPY Pipfile .
COPY extract-package.py .


RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install pipfile
RUN python3 extract-package.py
RUN pip install -r requirements.txt

COPY . .
