import json
import re

import requests
from dateutil import parser
from nums_from_string import get_nums
from bs4 import BeautifulSoup

import schemas

def int_from_str(text_, default_for_none = None):
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

    listing = data['props']['pageProps']['listing']
    print(listing)
    print(listing['media'].get('totalImages', ''))
    
    result = schemas.DaftListing(
        id=listing.get('id', ''),
        title=listing.get('title', ''),
        seoTitle=listing.get('seoTitle', ''),
        sections=listing.get('sections', ''),
        featuredLevel=listing.get('featuredLevel', ''),
        lastUpdateDate=parse_date(listing.get('lastUpdateDate', None)),

        price=listing.get('price', ''),
        numBedrooms=listing.get('numBedrooms', ''),
        numBathrooms=listing.get('numBathrooms', ''),
        propertyType=listing.get('propertyType', ''),
        daftShortcode=listing.get('daftShortcode', ''),

        totalImages=listing['media'].get('totalImages', ''),
        hasVideo=listing['media'].get('hasVideo', ''),
        hasVirtualTour=listing['media'].get('hasVirtualTour', ''),
        hasBrochure=listing['media'].get('hasBrochure', ''),
        ber=str(listing.get('ber', '')),
        seoFriendlyPath=listing.get('seoFriendlyPath', ''),
        category=listing.get('category', ''),
        state=listing.get('state', ''),
        premierPartner=listing.get('premierPartner', ''),
        description=listing.get('description', ''),
        facilities=[x['name'] for x in listing.get('facilities', '')],
        propertyOverview=listing.get('propertyOverview', {}),
        listingViews=listing.get('listingViews', ''),
    )

    return result
