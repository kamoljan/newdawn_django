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
tar xvzf sphinx-2.1.1-beta.tar.gz
cd sphinx-2.1.1-beta
./configure --prefix=/usr/local/sphinx --with-mysql=/usr/local/mysql
make
make install
cd -
rm -rf ./sphinx-2.1.1-beta

##############################################################################

cd ../
