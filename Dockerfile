FROM python:3.9.7-slim-buster

RUN apt update
RUN apt install sudo -y


RUN sudo apt-get update -y
RUN sudo apt upgrade -y
RUN sudo apt install gcc -y
RUN sudo apt-get install g++ -y
RUN sudo apt install python3-cffi -y
RUN apt install libffi-dev -y

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade cffi==1.14.2
RUN pip install -r requirements.txt