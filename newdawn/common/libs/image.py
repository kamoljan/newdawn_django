#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from PIL import Image

import random
import imghdr
import hashlib
import time
import os

def is_valid_image(filename):
    image_type = imghdr.what(filename)
    if image_type in ['jpeg', 'gif', 'png']:
        return True
    return False
    
def image_resize(path, output_size):
    try:
        img = Image.open(path)
    except:
        img = Image.new("RGBA", output_size)
    # RGBA is better support by browsers
    if img.mode != 'RGBA': img = img.convert('RGBA')
    m_width = float(output_size[0])
    m_height = float(output_size[1])
    w_k = img.size[0] / m_width
    h_k = img.size[1] / m_height
    if output_size[0] < img.size[0] or output_size[1] < img.size[1]:
        if w_k > h_k:
            new_size = (int(m_width), int(img.size[1] / w_k))
        else:
            new_size = (int(img.size[0] / h_k), int(m_height))
    else:
        new_size = img.size
    size = (int(new_size[0]), int(new_size[1]))
    return img.resize(size, Image.ANTIALIAS)

def image_resize_and_watermark(image_path, save_path, wk_path):
    """
    Utilities for applying a watermark to an image using PIL.
    Original Source: http://code.activestate.com/recipes/362879/
    """
    img = image_resize(image_path, (640, 480))
    wk = Image.open(wk_path)
    top = random.choice([0, img.size[1] - wk.size[1]])
    left = random.choice([0, img.size[0] - wk.size[0]])
    # create a transparent layer the size of the image & draw the watermark in that layer.
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    layer.paste(wk, (left, top))
    # composite the watermark with the layer
    wk_img = Image.composite(layer, img, layer)
    wk_img.save(save_path, 'JPEG')

def image_generate_thumbnail(image_path, save_path):
    image = image_resize(image_path, (80, 60))
    image.save(save_path, "JPEG")

def image_upload(request):
    try:
        ip = request.META['REMOTE_ADDR'] # get user ip
        # TODO: if ip is spamer, forbidden it.
        
        # get file list
        img = request.FILES['image_file'] 
        
        # name and paths
        fid = hashlib.md5(img.name.encode('ascii','ignore') + ip + str(time.time())).hexdigest()
        original_path = settings.STATIC_ROOT + '/tmp/original/' + fid + '.ori'
        wk_path = settings.STATIC_ROOT + '/tmp/original/watermark.png'
        thumb_path = ad_image_temp_path('thumb', fid)
        large_path = ad_image_temp_path('large', fid)
        
        # save original temp file
        f = open(original_path, 'wb+')
        for chunk in img.chunks():
            f.write(chunk)
        f.close()
        
        # process image and output
        if is_valid_image(original_path):
            image_resize_and_watermark(original_path, large_path, wk_path)
            image_generate_thumbnail(original_path, thumb_path)
            output = { 'status': 0, 'fid': fid, 'thumb': ad_image_temp_url('thumb', fid), 'name': img.name }
        else:
            output = { 'status': 1, 'error': '%s is not a valid image file' % img.name }
            
        # remove original temp file
        os.unlink(original_path)
    except:
        output = { 'status': 2, 'error': 'Internal error' }
    
    return output

# type = 'thumb', 'large'
def ad_image_temp_path(type, fid):
    return '%s/tmp/%s/%s.jpg' % (settings.STATIC_ROOT, type, fid)

# type = 'thumb', 'large'
def ad_image_temp_url(type, fid):
    return '%stmp/%s/%s.jpg' % (settings.STATIC_URL, type, fid)