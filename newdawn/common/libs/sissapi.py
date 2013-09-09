#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from django.conf import settings

import siss


def save_image_to_siss_with_string(str):
    try:
        conn = siss.SissConnection(settings.SISS_URL, settings.SISS_SECRET_KEY)
        fid = conn.put(str)
        conn.close()
        return fid
    except siss.SissException as e:
        logging.error(str(e))
        return None
    except:
        return None


def save_image_to_siss(path):
    try:
        conn = siss.SissConnection(settings.SISS_URL, settings.SISS_SECRET_KEY)
        fid = conn.put_from_file(path)
        conn.close()
        os.unlink(path)
        return fid
    except siss.SissException as e:
        logging.error(str(e))
        return None
    except:
        return None


def get_image_from_siss(fid):
    try:
        conn = siss.SissConnection(settings.SISS_URL, settings.SISS_SECRET_KEY)
        image = conn.get(fid)
        conn.close()
        return image
    except siss.SissException as e:
        logging.error(str(e))
        return None
    except:
        return None