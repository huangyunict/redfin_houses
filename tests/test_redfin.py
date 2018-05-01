#!/usr/bin/env python3
# coding=utf-8

import unittest

from redfin_houses.house_filter import HouseFilter, PropertyTypeEnum, PriceEnum, SqftEnum, BathEnum, LotEnum
from redfin_houses.redfin import query_house_list


class RedfinTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_redfin_house_list(self):
        hf = HouseFilter(
            property_type_list=[
                PropertyTypeEnum.HOUSE, PropertyTypeEnum.CONDO
            ],
            min_price=PriceEnum.PRICE_850k,
            max_price=PriceEnum.PRICE_2M,
            min_beds=2,
            max_beds=5,
            min_baths=BathEnum.BATH_1.BATH_1p25,
            min_sqft=SqftEnum.SQFT_750,
            max_sqft=SqftEnum.SQFT_3000,
            min_year_built=1970,
            max_year_built=2010,
            has_garage=True,
            min_lot_size=LotEnum.SQFT_4500,
            max_lot_size=LotEnum.ACRES_0p5)
        query_house_list("zipcode/98033", hf)