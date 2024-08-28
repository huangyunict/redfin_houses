"""Test module for the class Redfin."""
from src.redfin_houses.house_filter import HouseFilter, PropertyTypeEnum, PriceEnum, SqftEnum, BathEnum, LotEnum
from src.redfin_houses.redfin import query_house_list


class TestRedfin:
    """Tests for the class Redfin."""

    def test_redfin_house_list(self):
        hf = HouseFilter(property_type_list=[
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

        # Verify response.
        response = query_house_list("zipcode/98033", hf)
        assert len(response) > 0

        # Verify column names.
        response_col_names = response.split("\n")[0].strip().split(',')
        expected_col_names = [
            'SALE TYPE',
            'SOLD DATE',
            'PROPERTY TYPE',
            'ADDRESS',
            'CITY',
            'STATE OR PROVINCE',
            'ZIP OR POSTAL CODE',
            'PRICE',
            'BEDS',
            'BATHS',
            'LOCATION',
            'SQUARE FEET',
            'LOT SIZE',
            'YEAR BUILT',
            'DAYS ON MARKET',
            '$/SQUARE FEET',
            'HOA/MONTH',
            'STATUS',
            'NEXT OPEN HOUSE START TIME',
            'NEXT OPEN HOUSE END TIME',
            'URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)',
            'SOURCE',
            'MLS#',
            'FAVORITE',
            'INTERESTED',
            'LATITUDE',
            'LONGITUDE',
        ]
        assert len(expected_col_names) == len(response_col_names)

        for a, b in zip(expected_col_names, response_col_names):
            if a != b:
                print("[{}] != [{}]".format(a, b))
        assert expected_col_names == response_col_names
