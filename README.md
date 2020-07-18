# redfin_houses

Python library to retrieve house information from Redfin.

### Algorithm

- Generate redfin url with given filters. For example: https://www.redfin.com/zipcode/98004/filter/property-type=house,min-price=125k,min-sqft=1.75k-sqft,max-sqft=2.5k-sqft
- Parse the the webpage of generated url and find the Download link (with id="download-and-save").
- Navigate to the download link and save the csv file.

### Supported filter

- Property types (e.g. "property-type=house+condo").
- Minimum price (e.g. "min-price=750k").
- Maximum price (e.g. "max-price=1.5M").
- Minimum number of bedrooms (e.g. "min-beds=2").
- Maximum number of bedrooms (e.g. "max-beds=3").
- Minimum number of bathrooms (e.g. "min-baths=1.25").
- Minimum square footage of the property (e.g. "min-sqft=1.5k-sqft").
- Maximum square footage of the property (e.g. "max-sqft=2.5k-sqft").
- Minimum square footage of the lot (e.g. "min-lot-size=4.5k-sqft").
- Maximum square footage of the lot (e.g. "max-lot-size=6.5k-sqft").
- Oldest year built (e.g. "min-year-built=2017").
- Newest year built (e.g. "max-year-built=2019").
- Maximum HOA fee (e.g. "hoa=50").

