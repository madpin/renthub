import json
import re
import hashlib

import requests
from dateutil import parser
from nums_from_string import get_nums
from bs4 import BeautifulSoup

import schemas


def int_from_str(text_, default_for_none=None):
    numbers = re.findall("\d+", text_)
    if(len(numbers) == 0):
        return default_for_none
    elif(len(numbers) == 1):
        return numbers[0]
    else:
        raise ValueError('String with multiple numbers')


def parse_date(text_):
    if(text_ is None):
        return None
    return parser.parse(text_, dayfirst=True).date()


async def get_listing_details(url):
    response = requests.get(url)

    if(response.status_code == 200):
        html = requests.get(url).text
    else:
        raise ReferenceError('The request didn`t run correctly')

    soup = BeautifulSoup(html, 'html.parser')
    data = json.loads(soup.find(id="__NEXT_DATA__").text)
    pageProps = data['props']['pageProps']
    listing = pageProps['listing']
    # print(listing)

    result = schemas.DaftListing(
        id=listing.get('id', ''),
        title=listing.get('title', ''),
        seoTitle=listing.get('seoTitle', ''),
        sections=listing.get('sections', ''),
        featuredLevel=listing.get('featuredLevel', ''),
        lastUpdateDate=parse_date(listing.get('lastUpdateDate', None)),

        numBedrooms=listing.get('numBedrooms', ''),
        numBathrooms=listing.get('numBathrooms', ''),
        propertyType=listing.get('propertyType', ''),
        daftShortcode=listing.get('daftShortcode', ''),


        ber=str(listing.get('ber', '')),
        seoFriendlyPath=listing.get('seoFriendlyPath', ''),
        category=listing.get('category', ''),
        state=listing.get('state', ''),
        premierPartner=listing.get('premierPartner', ''),
        description=listing.get('description', ''),
        facilities=[x['name'] for x in listing.get('facilities', [])],
        propertyOverview=listing.get('propertyOverview', {}),
        listingViews=pageProps.get('listingViews', ''),
    )

    if('media' in listing):
        result.images_count = listing['media'].get('totalImages', '')
        result.has_video = listing['media'].get('hasVideo', '')
        result.has_virtual_tour = listing['media'].get('hasVirtualTour', '')
        result.has_brochure = listing['media'].get('hasBrochure', '')
        result.images = [list(x.values())[0]
                         for x in listing['media'].get('images', [])]

    # Price
        if('nonFormatted' in listing and 'price' in listing['nonFormatted']):
            result.price = listing['nonFormatted']['price']
        elif('dfpTargetingValues' in pageProps and 'price' in listing['nonFormatted']):
            result.price = pageProps['dfpTargetingValues']['price']
    result.hash_version = hashlib.md5(
        f"{result.description}{result.price}".encode('utf-8')).hexdigest()

    with open(f"/data/{listing.get('id', '')}.json", 'w') as f:
        json.dump(data, f, indent=2)

    return result
