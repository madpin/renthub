import json
import re
import hashlib

import requests
from dateutil import parser
from nums_from_string import get_nums
from bs4 import BeautifulSoup
from fastapi.logger import logger

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
    return parser.parse(text_, dayfirst=True)


async def get_listing_details(url):
    response = requests.get(url)

    if(response.status_code == 200):
        html = requests.get(url).text
    else:
        raise ReferenceError('The request didn`t run correctly')

    soup = BeautifulSoup(html, 'html.parser')
    data = json.loads(soup.find(id="__NEXT_DATA__").text)
    pageProps = data['props']['pageProps']
    if "listing" not in pageProps:
        logger.error(f"URL without Listing: {url}")
        return None
    listing = pageProps['listing']
    # print(listing)
    with open(f"/data/raw/{listing.get('id', '')}.json", 'w') as f:
        json.dump(listing, f, indent=2)
        
    result = schemas.DaftListing(
        id=listing.get('id', ''),
        title=listing.get('title', ''),
        seoTitle=listing.get('seoTitle', ''),
        sections=listing.get('sections', ''),
        featuredLevel=listing.get('featuredLevel', ''),
        lastUpdateDate=parse_date(listing.get('lastUpdateDate', None)),
        numBedrooms=int_from_str(listing.get('numBedrooms', '0')),
        numBathrooms=int_from_str(listing.get('numBathrooms', '0')),
        propertyType=listing.get('propertyType', ''),
        daftShortcode=listing.get('daftShortcode', ''),


        ber=str(listing.get('ber', '')),
        seoFriendlyPath=listing.get('seoFriendlyPath', ''),
        category=listing.get('category', ''),
        state=listing.get('state', ''),
        premierPartner=listing.get('premierPartner', ''),
        description=listing.get('description', ''),
        facilities=[x['name'] for x in listing.get('facilities', [])],
        propertyOverview=[
            f"{x['label']}: {x['text']}" for x in listing.get('propertyOverview', [])],
        listingViews=int_from_str(str(pageProps.get('listingViews', '0'))),
    )

    if('media' in listing):
        result.totalImages = listing['media'].get('totalImages', '')
        result.hasVideo = listing['media'].get('hasVideo', '')
        result.hasVirtualTour = listing['media'].get('hasVirtualTour', '')
        result.hasBrochure = listing['media'].get('hasBrochure', '')
        result.images = []
        for image_block in listing['media'].get('images', []):

            url_600 = None
            for key, val in image_block.items():
                print(key, val)
                digit_groups = re.findall("\d+", key)
                if((len(digit_groups) > 0) and (int(re.findall("\d+", key)[0]) <= 600) and val.startswith('http')):
                    url_600 = val
                    break
            result.images.append(
                schemas.Image(
                    url=next(filter(lambda y: y.startswith('http'), image_block.values())),
                    url_600=url_600
                    
                )
            )

    # Price
    if('nonFormatted' in listing and 'price' in listing['nonFormatted']):
        result.price = listing['nonFormatted']['price']
    elif('dfpTargetingValues' in pageProps and 'price' in listing['nonFormatted']):
        result.price = pageProps['dfpTargetingValues']['price']

    result.hash_version = hashlib.md5(
        f"{result.totalImages}{result.description}{result.price}".encode('utf-8')).hexdigest()


    with open(f"/data/jsons/{listing.get('id', '')}.json", 'w') as f:
        json.dump(data, f, indent=2)

    return result
