#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from django.conf import settings

import sushi


def save_image_to_sushi_with_string(str):
    try:
        conn = sushi.SushiConnection(settings.SUSHI_URL, settings.SUSHI_SECRET_KEY)
        fid = conn.put(str)
        conn.close()
        return fid
    except sushi.SushiException as e:
        logging.error(str(e))
        return None
    except:
        return None


def save_image_to_sushi(path):
    try:
        conn = sushi.SushiConnection(settings.SUSHI_URL, settings.SUSHI_SECRET_KEY)
        fid = conn.put_from_file(path)
        conn.close()
        os.unlink(path)
        return fid
    except sushi.SushiException as e:
        logging.error(str(e))
        return None
    except:
        return None


def get_image_from_sushi(fid):
    try:
        conn = sushi.SushiConnection(settings.SUSHI_URL, settings.SUSHI_SECRET_KEY)
        image = conn.get(fid)
        conn.close()
        return image
    except sushi.SushiException as e:
        logging.error(str(e))
        return None
    except:
        return None