#!/usr/bin/env python3
# coding=utf-8

import logging

from redfin_houses.house_filter import HouseFilter
from pyquery import PyQuery as pq
import urllib.request
import urllib.error

_REDFIN_PREFIX = 'https://www.redfin.com'

_REQUEST_HEADER = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64',
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset':
        'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Language':
        'en-US,en;q=0.8',
    'Connection':
        'keep-alive'
}

def query_house_list(area_str: str, house_filter: HouseFilter) -> str:
    if area_str.startswith('/'):
        area_str = area_str[1:]
    if area_str.endswith('/'):
        area_str = area_str[:-1]
    url = '/'.join([_REDFIN_PREFIX, area_str, house_filter.to_query_str()])
    # query list html
    try:
        logging.info('querying {}'.format(url))
        response = urllib.request.urlopen(urllib.request.Request(url, headers=_REQUEST_HEADER))
    except urllib.error.URLError as e:
        logging.critical('{}: cannot open url: {}'.format(e, url))
        raise RuntimeError(e)
    # get download id
    html = pq(response.read())
    link = html('#download-and-save')
    link_url = link.attr('href')
    # query linked csv
    url = '/'.join([_REDFIN_PREFIX, link_url])
    try:
        logging.info('querying {}'.format(url))
        response = urllib.request.urlopen(urllib.request.Request(url, headers=_REQUEST_HEADER))
    except urllib.error.URLError as e:
        logging.critical('{}: cannot open url: {}'.format(e, url))
        raise RuntimeError(e)
    # get linked csv content
    return response.read().decode("utf-8")
