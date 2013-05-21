#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newdawn.settings.local")

from django.contrib.auth.models import User
user = User.objects.get(username=sys.argv[1])
user.set_password(sys.argv[2])
user.save()