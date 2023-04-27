FROM postgres:15.2-alpine

WORKDIR /usr/src/app

COPY . /usr/src/app

ADD ./sql/sql_def.sql /docker-entrypoint-initdb.d/


