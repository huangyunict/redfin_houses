#!/usr/bin/env python3
# coding=utf-8


class HouseFilter(object):
    def __init__(self):
        self._property_type = None
        self._max_price = None
        self._min_beds = None
        self._min_beds = None
        self._min_baths = None
        self._max_baths = None
        self._min_sqrt = None
        self._max_sqft = None
        self._min_year_built = None

    @property
    def property_type(self):
        return self._property_type

    @property
    def max_price(self):
        return self._max_price

    @property
    def min_beds(self):
        return self._min_beds

    @property
    def max_beds(self):
        return self._min_beds

    @property
    def min_baths(self):
        return self._min_baths

    @property
    def max_baths(self):
        return self._max_baths

    @property
    def min_sqft(self):
        return self._min_sqrt

    @property
    def max_sqft(self):
        return self._max_sqft

    @property
    def min_year_built(self):
        return self._min_year_built
