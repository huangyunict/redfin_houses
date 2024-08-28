"""Test module for the class HouseFilter."""
from src.redfin_houses.house_filter import HouseFilter, PropertyTypeEnum, PriceEnum, BathEnum, SqftEnum, LotEnum, HOAEnum, OpenHouseEnum


class TestHouseFilter:
    """Tests for the class HouseFilter."""

    def test_filter_empty(self):
        """Test for creating a query string with empty filters."""

        hf_empty = HouseFilter()

        assert len(hf_empty.to_query_str()) == 0

    def test_filter_full(self):
        """Test for creating a query string with all filters."""

        hf_full = HouseFilter(property_type_list=[
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
                              max_lot_size=LotEnum.ACRES_0p5,
                              max_hoa=HOAEnum.HOA_1000,
                              open_house=OpenHouseEnum.OPEN_HOUSE_THISWEEKEND)
        hf_full_str = 'filter/property-type=house+condo,min-price=850k,max-price=2M,min-beds=2,max-beds=5,min-baths=1.25,min-sqft=750-sqft,max-sqft=3k-sqft,min-year-built=1970,max-year-built=2010,has-garage,min-lot-size=4.5k-sqft,max-lot-size=0.5-acre,hoa=1000,open-house=thisweekend'

        assert hf_full.to_query_str() == hf_full_str
