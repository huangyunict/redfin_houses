from typing import Set, List
import pandas as pd
import requests
import argparse
from pyquery import PyQuery as pq
from redfin_houses.redfin import _REDFIN_PREFIX, _REQUEST_HEADER


def parse_links(doc: pq) -> Set:
    links = {"{}{}".format(_REDFIN_PREFIX, x.attrib['href']) for x in doc.find('a')}
    return links


def parse_text(doc: pq) -> List:
    return doc.text()


def parse_table(doc: pq) -> str:
    table = doc('table')
    table_html = "<table>{}</table>".format(table.html())
    df = pd.read_html(table_html)[0]
    return df.to_csv(index=False)


def get_details(uri):
    resp = requests.get(uri, headers=_REQUEST_HEADER)
    if resp.ok:
        doc = pq(resp.text)
    else:
        raise Exception("can't get url")
    result = dict()
    result['marketing-remarks'] = parse_text(doc.find('#marketing-remarks-scroll'))
    result['property-details'] = parse_text(doc.find('#property-details-scroll'))
    result['property-history'] = parse_table(doc.find('#property-history-scroll'))
    result['schools'] = parse_table(doc.find('#schools-scroll'))
    result['similar-homes'] = parse_links(doc.find('#lsis-listings'))
    result['recently-sold'] = parse_links(doc.find('#lsis-solds'))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get details from redfin given url')
    parser.add_argument('--url', required=True, help="Property url")
    args = parser.parse_args()
    print("Getting details from {}".format(args.url))
    res = get_details(args.url)
    for k, v in res.items():
        print(k)
        print(v)
        print()

