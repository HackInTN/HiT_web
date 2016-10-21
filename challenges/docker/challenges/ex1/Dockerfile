from ex_template:latest

COPY sql_app.sql sql_app.sql
RUN service mysql start \
	&& mysql -uhackintn -h localhost -e 'CREATE DATABASE sql_app;' \
	&& mysql -uhackintn -h localhost sql_app < sql_app.sql

COPY SQL_app /var/www/html/

