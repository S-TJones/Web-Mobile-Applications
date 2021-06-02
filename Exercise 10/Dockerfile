FROM ubuntu:18.04
RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list 
RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list 
RUN sed -i "s/security.debian.org/mirrors.aliyun.com\/debian-security/g" /etc/apt/sources.list

FROM python:3.6-alpine

RUN adduser --gecos "Thomas Xu,RoomNumber,WorkPhone,HomePhone" --disabled-password thomas
WORKDIR /home/thomas

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN venv/bin/pip install gunicorn pymysql -i https://mirrors.aliyun.com/pypi/simple/

COPY app app
COPY migrations migrations
COPY finalsystem.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP finalsystem.py

RUN chown -R thomas:thomas ./
USER thomas

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
