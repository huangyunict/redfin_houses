import pandas as pd
import io

from redfin_houses.house_filter import HouseFilter, PropertyTypeEnum, PriceEnum, SqftEnum, BathEnum, LotEnum
from redfin_houses.redfin import query_house_list


def convert_csv_to_dataframe(csv):
    f = io.StringIO(csv)
    df = pd.read_csv(f)
    return df


def get_property_by_zip_code(zipcode, filter=None):
    print("Searching within zipcode: {}".format(zipcode))
    print("Applying filter: {}".format(filter.to_query_str()))
    response = query_house_list("zipcode/{}".format(zipcode), filter)
    return response


if __name__ == "__main__":
    house_filter = HouseFilter(
        property_type_list=[PropertyTypeEnum.HOUSE],
        max_price=PriceEnum.PRICE_800k
    )
    zipcode = 95111
    houses_csv = get_property_by_zip_code(zipcode, filter=house_filter)
    df_houses = convert_csv_to_dataframe(houses_csv)
    with pd.option_context('display.max_columns', None, 'display.expand_frame_repr', False, 'max_colwidth', -1):
        print(df_houses)
