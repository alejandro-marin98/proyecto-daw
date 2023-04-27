FROM python:3.11.3-alpine3.17

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
RUN pip install --upgrade pip

ADD . /usr/src/app

EXPOSE 8000

