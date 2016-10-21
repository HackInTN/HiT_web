from php:apache
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client mysql-server
RUN docker-php-ext-install pdo pdo_mysql
RUN a2enmod rewrite

WORKDIR /tmp
RUN service mysql start \
	&& echo "GRANT ALL PRIVILEGES ON *.* TO hackintn@localhost IDENTIFIED BY '';" | mysql -uroot

RUN rm -f /usr/local/apache2/htdocs/index.html

ENV ALLOW_OVERRIDE true

CMD service mysql start && apache2-foreground
