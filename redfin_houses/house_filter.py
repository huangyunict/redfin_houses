#!/usr/bin/env python3
# coding=utf-8

from enum import Enum


class PropertyTypeEnum(Enum):
    HOUSE = 'house'
    CONDO = 'condo'
    TOWN_HOUSE = 'townhouse'
    MULTI_FAMILY = 'multifamily'
    LAND = 'land'


class PriceEnum(Enum):
    PRICE_50k = '50k'
    PRICE_75k = '75k'
    PRICE_100k = '100k'
    PRICE_125k = '125k'
    PRICE_150k = '150k'
    PRICE_175k = '175k'
    PRICE_200k = '200k'
    PRICE_225k = '225k'
    PRICE_250k = '250k'
    PRICE_275k = '275k'
    PRICE_300k = '300k'
    PRICE_325k = '325k'
    PRICE_350k = '350k'
    PRICE_375k = '375k'
    PRICE_400k = '400k'
    PRICE_425k = '425k'
    PRICE_450k = '450k'
    PRICE_475k = '475k'
    PRICE_500k = '500k'
    PRICE_550k = '550k'
    PRICE_600k = '600k'
    PRICE_650k = '650k'
    PRICE_700k = '700k'
    PRICE_750k = '750k'
    PRICE_800k = '800k'
    PRICE_850k = '850k'
    PRICE_900k = '900k'
    PRICE_950k = '950k'
    PRICE_1M = '1M'
    PRICE_1p25M = '1.25M'
    PRICE_1p5M = '1.5M'
    PRICE_1p75M = '1.75M'
    PRICE_2M = '2M'
    PRICE_2p25M = '2.25M'
    PRICE_2p5M = '2.5M'
    PRICE_2p75M = '2.75M'
    PRICE_3M = '3M'
    PRICE_3p25M = '3.25M'
    PRICE_3p5M = '3.5M'
    PRICE_3p75M = '3.75M'
    PRICE_4M = '4M'
    PRICE_4p25M = '4.25M'
    PRICE_4p5M = '4.5M'
    PRICE_4p75M = '4.75M'
    PRICE_5M = '5M'
    PRICE_6M = '6M'
    PRICE_7M = '7M'
    PRICE_8M = '8M'
    PRICE_9M = '9M'
    PRICE_10M = '10M'


class BathEnum(Enum):
    BATH_1 = '1'
    BATH_1p25 = '1.25'
    BATH_2 = '2'
    BATH_3 = '3'
    BATH_4 = '4'
    BATH_5 = '5'
    BATH_6 = '6'


class SqftEnum(Enum):
    SQFT_500 = '500-sqft'
    SQFT_750 = '750-sqft'
    SQFT_1000 = '1k-sqft'
    SQFT_1250 = '1.25k-sqft'
    SQFT_1500 = '1.5k-sqft'
    SQFT_1750 = '1.75k-sqft'
    SQFT_2000 = '2k-sqft'
    SQFT_2250 = '2.25k-sqft'
    SQFT_2500 = '2.5k-sqft'
    SQFT_2750 = '2.75k-sqft'
    SQFT_3000 = '3k-sqft'
    SQFT_3500 = '3.5k-sqft'
    SQFT_4000 = '4k-sqft'
    SQFT_5000 = '5k-sqft'
    SQFT_7500 = '7.5k-sqft'


class LotEnum(Enum):
    SQFT_2000 = '2k-sqft'
    SQFT_4500 = '4.5k-sqft'
    SQFT_6500 = '6.5k-sqft'
    SQFT_8000 = '8k-sqft'
    ACRES_0p25 = '0.25-acre'
    ACRES_0p5 = '0.5-acre'
    ACRES_1 = '1-acre'
    ACRES_2 = '2-acre'
    ACRES_3 = '3-acre'
    ACRES_4 = '4-acre'
    ACRES_5 = '5-acre'
    ACRES_10 = '10-acre'
    ACRES_40 = '40-acre'
    ACRES_100 = '100-acre'


class HouseFilter(object):
    def __init__(self,
                 property_type_list: list = None,
                 min_price: PriceEnum = None,
                 max_price: PriceEnum = None,
                 min_beds: int = None,
                 max_beds: int = None,
                 min_baths: BathEnum = None,
                 min_sqft: SqftEnum = None,
                 max_sqft: SqftEnum = None,
                 min_year_built: int = None,
                 max_year_built: int = None,
                 has_garage=None,
                 min_lot_size: LotEnum = None,
                 max_lot_size: LotEnum = None):
        assert isinstance(property_type_list, list)
        self._property_type_list = property_type_list if property_type_list else [
            PropertyTypeEnum.HOUSE
        ]
        assert isinstance(min_price, PriceEnum)
        self._min_price = PriceEnum(min_price)
        assert isinstance(max_price, PriceEnum)
        self._max_price = PriceEnum(max_price)
        assert isinstance(min_beds, int)
        self._min_beds = int(min_beds)
        assert isinstance(max_beds, int)
        self._max_beds = int(max_beds)
        assert isinstance(min_baths, BathEnum)
        self._min_baths = BathEnum(min_baths)
        assert isinstance(min_sqft, SqftEnum)
        self._min_sqft = SqftEnum(min_sqft)
        assert isinstance(max_sqft, SqftEnum)
        self._max_sqft = SqftEnum(max_sqft)
        assert isinstance(min_year_built, int)
        self._min_year_built = int(min_year_built)
        assert isinstance(max_year_built, int)
        self._max_year_built = max_year_built
        assert isinstance(has_garage, bool)
        self._has_garage = bool(has_garage)
        assert isinstance(min_lot_size, LotEnum)
        self._min_lot_size = LotEnum(min_lot_size)
        assert isinstance(max_lot_size, LotEnum)
        self._max_lot_size = LotEnum(max_lot_size)

    @property
    def property_type_list(self):
        return self._property_type_list

    @property
    def min_price(self):
        return self._min_price

    @property
    def max_price(self):
        return self._max_price

    @property
    def min_beds(self):
        return self._min_beds

    @property
    def max_beds(self):
        return self._max_beds

    @property
    def min_baths(self):
        return self._min_baths

    @property
    def min_sqft(self):
        return self._min_sqft

    @property
    def max_sqft(self):
        return self._max_sqft

    @property
    def min_year_built(self):
        return self._min_year_built

    @property
    def max_year_built(self):
        return self._max_year_built

    @property
    def has_garage(self):
        return bool(self._has_garage)

    @property
    def min_lot_size(self):
        return self._min_lot_size

    @property
    def max_lot_size(self):
        return self._max_lot_size

    def to_query_str(self):
        l = list()
        l.append('property-type=' +
                 '+'.join([str(x.value) for x in self.property_type_list]))
        if self._min_price:
            l.append('min-price=' + str(self._min_price.value))
        if self.max_price:
            l.append('max-price=' + str(self.max_price.value))
        if self.min_beds:
            l.append('min-beds=' + str(self.min_beds))
        if self.max_beds:
            l.append('max-beds=' + str(self.max_beds))
        if self.min_baths:
            l.append('min-baths=' + str(self.min_baths.value))
        if self.min_sqft:
            l.append('min-sqft=' + str(self.min_sqft.value))
        if self.max_sqft:
            l.append('max-sqft=' + str(self.max_sqft.value))
        if self.min_year_built:
            l.append('min-year-built=' + str(self.min_year_built))
        if self.max_year_built:
            l.append('max-year-built=' + str(self.max_year_built))
        if self.has_garage:
            l.append('has-garage')
        if self.min_lot_size:
            l.append('min-lot-size=' + str(self.min_lot_size.value))
        if self.max_lot_size:
            l.append('max-lot-size=' + str(self.max_lot_size.value))
        return 'filter/' + ','.join(l)
