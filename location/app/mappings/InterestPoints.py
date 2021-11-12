import os
from urllib import parse

from herepy import (
    PlacesApi,
    RoutingApi,
    RouteMode,
    GeocoderApi,
)
import schemas


def get_website(place):
    if('contacts' not in place):
        return None
    for contact in place['contacts']:
        if('www' in contact):
            for www in contact['www']:
                if('value' in www):
                    return www['value'].lower()
    return None


def get_chain(place):
    for chain in place.get('chains', []):
        if('name' in chain):
            return chain['name']
    return None


def get_interenst_points(latitude, longitude, query: str):
    places_api = PlacesApi(api_key=os.environ['HERE_API_KEY'])

    # fetches a list of places based on a query string and country code
    response = places_api.search_in_country(
        coordinates=[latitude, longitude], query=query, country_code="IRL"
    )
    places = response.as_dict()
    if('items' not in places):
        raise ReferenceError('There is no `items` in the response')

    ret_ = []
    for place in places['items']:
        place_instance = schemas.InterestPoint(
            lat=place['position']['lat'],
            long=place['position']['lng'],
            name=place['title'].title(),
            address=place['address']['label'],
            distance=place['distance'],
            chain_name=get_chain(place)
        )

        website = get_website(place)
        if(website):
            place_instance.website = website
            place_instance.website_domain = parse.urlsplit(
                website).netloc.lstrip('www.')

        ret_.append(place_instance)

    return ret_
