#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from common.libs.utils import cint
from common.libs.sphinxapi import SphinxClient, SPH_SORT_ATTR_DESC, SPH_SORT_ATTR_ASC
from ad.models import Ad, Category


def ad_search(request, category=None):
    # get args
    args = ad_search_get_args(request, category)

    # get context
    context = ad_search_get_context(request, args)

    # set paging
    context['paging'] = {
    'query_string': ad_search_get_query_string(request),
    'pages': range(0, context['total'], args['limit'])
    }

    context['SUSHI_PUBLIC_URL'] = settings.SUSHI_PUBLIC_URL

    return render_to_response('search/search_form.html', context, context_instance=RequestContext(request))


def ad_search_get_args(request, category=0):
    category_id = category.id if category else '0'
    # TODO: put it back later
    #'category_id': cint(request.GET.get('category_id', category_id)),
    args = {
    'query': request.GET.get('query', '').strip(),
    'limit': cint(request.GET.get('limit', '20')),
    'sort_by': request.GET.get('sort_by', 'date_desc'),
    'start': cint(request.GET.get('start', '0')),
    }
    return args


def ad_search_get_context(request, args):
    args['objects'] = {}

    # set category
    #if args['category_id'] and Category.objects.filter(pk=args['category_id'], enabled=True).exists():
    #	args['objects']['category_id'] = Category.objects.get(pk=args['category_id'])
    #else:
    #	args['objects']['category_id'] = None

    # fire a search request
    sp = SphinxClient()
    sp.SetServer(settings.SPHINX_SEARCHD_HOST, int(settings.SPHINX_SEARCHD_PORT))

    # sort_by
    if args['sort_by'] == 'date_desc':
        sp.SetSortMode(SPH_SORT_ATTR_DESC, 'created_time')
    elif args['sort_by'] == 'price':
        sp.SetSortMode(SPH_SORT_ATTR_DESC, 'price')

    # limit
    sp.SetLimits(args['start'], args['limit'], max(args['start'] + args['limit'], 20))

    # default context
    context = {'args': args, 'ads': [], 'total': 0}

    lat = float(request.GET.get('id_latitude', 1.34))
    lon = float(request.GET.get('id_longitude', 103.85))

    sp.SetGeoAnchor('latitude', 'longitude', lat, lon)
    # sorting by distance
    sp.SetSortMode(SPH_SORT_ATTR_ASC, "@geodist")

    res = sp.Query(args['query'].encode('utf-8'), 'newdawn_ad,delta')
    if res:
        ads = []
        for match in res['matches']:
            try:
                # TODO: don't hard code it
                ad = Ad.objects.get(pk=match['id'], ad_status=0)
                ads.append(ad)
            except Ad.DoesNotExist, e:
                continue
        context['ads'] = ads

    return context


def ad_search_get_query_string(request):
    # TODO: is not clean, just want to remove 'start' parameter?
    query_string = '/search?'
    if request.META['QUERY_STRING'] == '':
        return query_string
    params = request.META['QUERY_STRING'].split('&')
    for param in params:
        param = param.split('=')
        if param[0] != 'start':
            query_string = query_string + param[0] + '=' + param[1] + '&'
    return query_string


def to_radians(lat, lon):
    return math.radians(lat), math.radians(lon)
