#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from django.core.validators import MinLengthValidator, MaxLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=128)
    position = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'www_categories'
        ordering = ['position']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/search/category_id=' + str(self.id)


class Ad(models.Model):
    subject = models.CharField(max_length=128, validators=[MinLengthValidator(3), MaxLengthValidator(128)])
    body = models.TextField(max_length=140, validators=[MinLengthValidator(10), MaxLengthValidator(140)])
    category = models.ForeignKey(Category, related_name='category_set')
    image_fid = models.CharField(max_length=256)
    thumb_fid = models.CharField(max_length=256)
    price = models.IntegerField(null=False, blank=False)
    sold = models.BooleanField(default=False)
    AD_STATUS = ((0, 'Published'), (1, 'Refused'), (2, 'Sold'), (3, 'Deleted'))
    ad_status = models.IntegerField(choices=AD_STATUS, default=0, db_index=True)
    user_name = models.CharField(max_length=40, validators=[MinLengthValidator(3), MaxLengthValidator(40)])
    user_ip = models.GenericIPAddressField()
    user_phone = models.CharField("Phone Number", max_length=32,
                                  validators=[MinLengthValidator(9), MaxLengthValidator(32)])
    user_email = models.EmailField()
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    secret_token = models.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    moderated_time = models.DateTimeField(auto_now=False, null=True, blank=True)

    class Meta:
        db_table = 'www_ads'
        ordering = ['-created_time']
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __unicode__(self):
        return self.subject

    def get_absolute_url(self):
        return '/ad/' + str(self.id)
