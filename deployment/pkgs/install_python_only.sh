#!/bin/sh -v
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


