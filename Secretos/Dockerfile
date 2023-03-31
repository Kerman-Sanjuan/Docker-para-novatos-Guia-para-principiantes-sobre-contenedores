# cat Dockerfile
FROM mysql:latest


RUN chown -R mysql:root /var/lib/mysql/


ARG MYSQL_DATABASE=$MYSQL_DATABASE
ARG MYSQL_USER=$MYSQL_USER
ARG MYSQL_PASSWORD=$MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

ADD users.sql /etc/mysql/data.sql

RUN sed -i 's/MYSQL_DATABASE/'$MYSQL_DATABASE'/g' /etc/mysql/data.sql
RUN cp /etc/mysql/data.sql /docker-entrypoint-initdb.d

EXPOSE 3306