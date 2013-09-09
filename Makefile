TOPDIR:=$(shell pwd)
PYTHON_VERSION=2.7

# Site configurations
DNS=yoglam.com

# MySQL settings
DBLOGIN=root
DBPASSWORD=12345678
DBCOMMAND=/usr/local/mysql/bin/mysql --user=${DBLOGIN} --password=${DBPASSWORD}
DBNAME=newdawn

# Super user settings
SUNAME=admin
SUEMAIL=kamol@${DNS}
SUPASSWORD=12345678

# Runtime
PID_FILE=${TOPDIR}/var/run/newdawn.pid
OUT_LOG=${TOPDIR}/var/logs/out.log
ERROR_LOG=${TOPDIR}/var/logs/error.log
HOST=127.0.0.1
PORT=8080

#.PHONY: clean install

install:
#	clean
	mkdir -p ${TOPDIR}/var/run/
	mkdir -p ${TOPDIR}/var/logs/
	@echo Reset database..
	echo "DROP DATABASE IF EXISTS ${DBNAME};" | ${DBCOMMAND}
	echo "CREATE DATABASE ${DBNAME} CHARACTER SET utf8;" | ${DBCOMMAND}
	@echo Sync database..
	python${PYTHON_VERSION} ${TOPDIR}/newdawn/manage.py syncdb --noinput
	@echo Migrate for social_auth
	python${PYTHON_VERSION} ${TOPDIR}/newdawn/manage.py migrate --noinput
	@echo Create super user...
	python${PYTHON_VERSION} ${TOPDIR}/newdawn/manage.py createsuperuser --username=${SUNAME} --email=${SUEMAIL} --noinput
	python${PYTHON_VERSION} ${TOPDIR}/newdawn/init.py ${SUNAME} ${SUPASSWORD}
	@echo Importing www_catagories.sql...
	${DBCOMMAND} ${DBNAME} < deployment/sql/www_categories.sql
	@echo Creating sphinx_counter.sql...
	${DBCOMMAND} ${DBNAME} < deployment/sql/sphinx_counter.sql
# TODO: no need it for now
# @echo Compile i18n messages...
# `cd ${TOPDIR}/newdawn/ && django-admin.py compilemessages && cd ${TOPDIR}`
	@echo Make static pages
	mkdir -p /var/www/${DNS}/
	make static
	@echo Admin Username: ${SUNAME}
	@echo Admin Password: ${SUPASSWORD}

# clean: stop-fastcgi
#     # if [ -e ${TOPDIR}/newdawn/www/locale/ru/LC_MESSAGES/django.mo ] ; then \
#     #   rm ${TOPDIR}/newdawn/www/locale/ru/LC_MESSAGES/django.mo ; \
#     # fi;
#     # rm -r ${TOPDIR}/newdawn/media/temp/*.*
#     # rm -r ${TOPDIR}/newdawn/static/tmp/*
#     # touch ${TOPDIR}/newdawn/media/temp/readme.txt

start: start-fastcgi start-nginx
	@echo Compile i18n messages...
# TODO: no need it for now
#`cd ${TOPDIR}/newdawn/ && django-admin.py compilemessages && cd ${TOPDIR}`
	@echo NewDawn is running now, make sure following daemons are running:
	@echo MySQL - make start-mysql
	@echo Sphinx - make start-searchd
	@echo Siss - make start-siss
	@echo Please add following hosts for staging server\:
	@echo 127.0.0.1 ${DNS} www.${DNS} siss.${DNS} static.${DNS}
	@echo Visit http\://${DNS} to access the site
	@echo Visit http\://${DNS}/admin to access the admin site

stop: stop-nginx stop-fastcgi

restart: stop start

start-nginx:
	cp ${TOPDIR}/deployment/conf/nginx/*.conf /usr/local/nginx/conf/
	sed -i.bak 's:@NEWDAWN_PATH@:/var/www:g' /usr/local/nginx/conf/static.${DNS}.conf	
	sed -i.bak 's:@NEWDAWN_PATH@:/var/www:g' /usr/local/nginx/conf/siss.${DNS}.conf	
	sed -i.bak 's:@NEWDAWN_PATH@:/var/www/touch-2.2.1:g' /usr/local/nginx/conf/sencha.${DNS}.conf	
	sed -i.bak 's:@NEWDAWN_PATH@:${TOPDIR}/newdawn:g' /usr/local/nginx/conf/${DNS}.conf
	/usr/local/nginx/sbin/nginx

stop-nginx:
	/usr/local/nginx/sbin/nginx -s stop

start-fastcgi:
	python${PYTHON_VERSION} ${TOPDIR}/newdawn/manage.py \
		runfcgi method=prefork host=${HOST} port=${PORT} pidfile=${PID_FILE} \
		outlog=${OUT_LOG} errlog=${ERROR_LOG} --verbosity=2

stop-fastcgi:
	if [ -e ${PID_FILE} ] ; then \
		kill `cat ${PID_FILE}`; \
		rm ${PID_FILE}; \
	fi;

start-memcached:
	/usr/bin/memcached -m 128 -c 5000 -d -r -u root -P ${TOPDIR}/var/run/memcached.pid

stop-memcached:
	kill `cat ${TOPDIR}/var/run/memcached.pid`

start-mysql:
	cp ${TOPDIR}/deployment/conf/mysql/my.cnf /etc/
	/usr/local/mysql/bin/mysqld_safe --user=mysql --general_log&

stop-mysql:
	/usr/local/mysql/bin/mysqladmin shutdown --user=${DBLOGIN} --password=${DBPASSWORD}

start-siss:
	-mkdir /var/siss/
	/usr/local/bin/sissd start

stop-siss:
	/usr/local/bin/sissd stop

start-postfix:
	cp ${TOPDIR}/deployment/conf/postfix/main.cf /etc/postfix/
	postfix start

stop-postfix:
	-postfix stop

start-searchd:
	cp ${TOPDIR}/deployment/conf/sphinx/sphinx.conf /usr/local/sphinx/etc/
	/usr/local/sphinx/bin/searchd

stop-searchd:
	/usr/local/sphinx/bin/searchd --stop

reindex:
	cp ${TOPDIR}/deployment/conf/sphinx/sphinx.conf /usr/local/sphinx/etc/
	/usr/local/sphinx/bin/indexer newdawn_ad --rotate

run-indexer:
	cp ${TOPDIR}/deployment/conf/sphinx/sphinx.conf /usr/local/sphinx/etc/
	/usr/local/sphinx/bin/indexer delta --rotate

static:
	python${PYTHON_VERSION} ${TOPDIR}/newdawn/manage.py collectstatic --link --noinput

start-env: start-mysql stop-postfix start-postfix start-siss start-searchd start

stop-env: stop stop-mysql stop-postfix stop-searchd stop-siss
