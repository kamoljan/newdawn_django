#!/bin/sh -v

cd ./universal

############################## PCRE ##########################################
# pcre (darwin only), for nginx
if [ `uname` = Darwin ]; then
    tar xvzf pcre-8.32.tar.gz
    cd pcre-8.32
    ./configure
    make
    make install
    cd -
    rm -rf ./pcre-8.32
fi

############################## libjpeg #######################################
# freetype libraries for PIL ttf fonts (The _imagingft C module is not installed)
if [ `uname` = Darwin ]; then
    tar xvzf freetype-2.4.11.tar.gz
    cd freetype-2.4.11
    ./configure
    make
    make install
    cd -
    rm -rf ./freetype-2.4.11
fi

############################## libjpeg #######################################
# libjpeg (darwin only), for PIL
if [ `uname` = Darwin ]; then
    tar xvzf jpegsrc.v9.tar.gz
    cd jpeg-9
    ln -s `which glibtool` ./libtool
    set env MACOSX_DEPLOYMENT_TARGET 10.6
    ./configure --enable-shared
    make
    make install
    cd -
    rm -rf ./jpeg-9
fi

############################## libevent #########################################
tar xvzf libevent-2.0.21-stable.tar.gz
cd libevent-2.0.21-stable
./configure
make
make install
cd -
rm -rf ./libevent-2.0.21-stable

############################## memcached #########################################
tar xvzf memcached-1.4.15.tar.gz
cd memcached-1.4.15
./configure
make
make install
cd -
rm -rf ./memcached-1.4.15

############################## Nginx #########################################
tar xvzf nginx-1.4.0.tar.gz
cd nginx-1.4.0
./configure --with-http_gzip_static_module
make
make install
cd -
rm -rf ./nginx-1.4.0

############################## MySQL #########################################

# add user for mysql, linux only, mac with a internal mysql account
if [ `uname` = Linux ]; then
    groupadd mysql
    useradd -g mysql mysql
fi

# build and install
tar xvzf mysql-5.1.52.tar.gz
cd mysql-5.1.52
./configure --prefix=/usr/local/mysql --with-plugins=innobase
make
make install
cd -
rm -rf ./mysql-5.1.52

# post-installation
cd /usr/local/mysql
chown -R mysql .
chgrp -R mysql .
bin/mysql_install_db --user=mysql
chown -R root:root .
chown -R mysql:mysql var
cp share/mysql/my-small.cnf /etc/my.cnf
bin/mysqld_safe --user=mysql --general_log &
sleep 5

# secure installation
echo "DELETE FROM mysql.user WHERE User='';" | bin/mysql -u root
echo "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');" | bin/mysql -u root
echo "DROP DATABASE test;" | bin/mysql -u root
echo "UPDATE mysql.user SET Password=PASSWORD('12345678') WHERE User='root';" | bin/mysql -u root
echo "FLUSH PRIVILEGES;" | bin/mysql -u root

sleep 3

bin/mysqladmin --user=root --password=12345678 shutdown
sleep 5
cd -

############################# Sphinx #########################################
tar xvzf sphinx-2.0.8.tar.gz
cd sphinx-2.0.8-release
./configure --prefix=/usr/local/sphinx --with-mysql=/usr/local/mysql
make
make install
cd -
rm -rf ./sphinx-2.0.8-release

##############################################################################

cd ../

############################ Python ##########################################
cd ./python

# Django
tar xvzf Django-1.5.1.tar.gz
cd Django-1.5.1
python setup.py install
cd -
rm -rf ./Django-1.5.1

# django social authorization
tar xvzf django-social-auth-0.7.23.tar.gz
cd django-social-auth-0.7.23
python setup.py install
cd -
rm -rf ./django-social-auth-0.7.23

# PIL
tar xvzf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
# python setup.py install
env ARCHFLAGS="-arch x86_64" python setup.py install
cd -
rm -rf ./Imaging-1.1.7

# mysql-python
tar xvzf MySQL-python-1.2.4b4.tar.gz
cd MySQL-python-1.2.4b4
#python setup.py install
env ARCHFLAGS="-arch x86_64" python setup.py install
cd -
rm -rf ./MySQL-python-1.2.4b4

# flup
tar xvzf flup-1.0.2.tar.gz
cd flup-1.0.2
python setup.py install
cd -
rm -rf ./flup-1.0.2

# reportlab
tar xvzf reportlab-2.7.tar.gz
cd reportlab-2.7
# python setup.py install
env ARCHFLAGS="-arch x86_64" python setup.py install
cd -
rm -rf ./reportlab-2.7

# tornado
tar xvzf tornado-3.0.1.tar.gz
cd tornado-3.0.1
python setup.py install
cd -
rm -rf ./tornado-3.0.1

# python-memcached
tar xvzf python-memcached-1.47.tar.gz
cd python-memcached-1.47
python setup.py install
cd -
rm -rf ./python-memcached-1.47

# sushi
tar xvzf sushi-2.0.tar.gz
cd sushi-2.0
python setup.py install
cd -
rm -rf ./sushi-2.0

# google data library
tar xvzf gdata-2.0.17.tar.gz
cd gdata-2.0.17
python setup.py install
cd -
rm -rf ./gdata-2.0.17

# PyJade is a high performance port of Jade-lang for python, that converts any .jade
# source to the each Template-language (Django, Jinja2, Mako or Tornado).
tar xvzf pyjade-2.0.2.tar.gz
cd pyjade-2.0.2
python setup.py install
cd -
rm -rf ./pyjade-2.0.2

# Mixins to add easy functionality to Django class-based views, forms, and models.
tar xvzf django-braces-1.0.0.tar.gz
cd django-braces-1.0.0
python setup.py install
cd -
rm -rf ./django-braces-1.0.0

# Django debug toolbar - git@github.com:django-debug-toolbar/django-debug-toolbar.git
tar xvzf django-debug-toolbar-0.9.4.tar.gz
cd django-debug-toolbar-0.9.4
python setup.py install
cd -
rm -rf ./django-debug-toolbar-0.9.4

# South is an intelligent database migrations library for the Django web framework
tar xvzf South-0.7.6.tar.gz
cd South-0.7.6
python setup.py install
cd -
rm -rf ./South-0.7.6

# A Django test runner based on unittest2's test discovery.
tar xvzf django-discover-runner-0.4.tar.gz
cd django-discover-runner-0.4
python setup.py install
cd -
rm -rf ./django-discover-runner-0.4


cd ../


