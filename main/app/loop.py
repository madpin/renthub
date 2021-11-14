from datetime import datetime
import dateutil.parser
import json


import requests
from requests.models import to_key_val_list

from sqlmodel import Field, Session, SQLModel, create_engine, select


from database import engine
from models import Listing, Facility, Image, InterestPoint, Route, RouteCreate, PlaceNearby


def get_daft_search_result():
    try:
        response = requests.get('http://daft:8000/search_result')
        response.raise_for_status()
        # Additional code will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        print(error)
    return response.json()


def get_daft_details(url):
    try:
        params = {
            'url': url,
            'method': 'json_details',
        }

        response = requests.get(
            'http://daft:8000/listing_details', params=params)
        response.raise_for_status()
        # Additional code will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        print(error)
    return response.json()


def get_routes_json(from_lat, from_long, to_lat, to_long):
    try:
        data = {
            "from_point": {"lat": from_lat, "long": from_long},
            "to_point": {"lat": to_lat, "long": to_long}
        }

        response = requests.post(
            'http://location:8000/route', data=json.dumps(data))
        response.raise_for_status()
        # Additional code will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        print(error)
    return response.json()


def get_routes(listing: Listing):
    ret_ = []
    with Session(engine) as session:
        interest_points_sttm = select(InterestPoint).\
            where(InterestPoint.is_active == True)
        interest_points = session.exec(interest_points_sttm).all()

        for interest_point in interest_points:
            routes = get_routes_json(
                listing.latitude, listing.longitude,
                interest_point.latitude, interest_point.longitude)
            print('routes')
            print(routes)
            for route in routes:
                ret_.append(Route(
                    interest_point_id=interest_point.id,
                    waking_distance=route['waking_distance'],
                    total_distance=route['total_distance'],
                    total_time=route['total_time'],
                    public_transport_count=route['public_transport_count'],
                ))
    print(ret_)
    return ret_


def get_places_nearby_json(from_lat, from_long, query):
    try:
        data = {"lat": from_lat, "long": from_long}

        response = requests.post(
            'http://location:8000/interest_places_nearby', data=json.dumps(data))
        response.raise_for_status()
        # Additional code will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        print(error)
    return response.json()


def get_places_nearby(listing: Listing):
    ret_ = []
    query = 'Grocery'
    places = get_places_nearby_json(
        from_lat=listing.latitude, from_long=listing.longitude,
        query=query)
    for place in places:
        ret_.append(PlaceNearby(
            name=place['name'],
            latitude=place['lat'],
            longitude=place['long'],
            address=place['address'],
            distance=place['distance'],
            website=place['website'],
            website_domain=place['website_domain'],
            chain_name=place['chain_name'],
            query=query,
        ))
    return ret_


def save_new_listing(search_result, listing_d):

    with Session(engine) as session:
        listing = Listing()
        # Search Result
        listing.source = 'daft'
        listing.is_active = True
        listing.url = search_result['url']
        listing.address = search_result['title']
        listing.price = search_result['monthly_price']
        listing.latitude = search_result['latitude']
        listing.longitude = search_result['longitude']
        listing.publish_date = dateutil.parser.isoparse(
            search_result['publish_date'])

        # Details:
        listing.source_id = listing_d['id']
        listing.source_code = listing_d['daftShortcode']
        listing.title = listing_d['title']
        listing.bedrooms = listing_d['numBedrooms']
        listing.bathrooms = listing_d['numBathrooms']
        listing.description = listing_d['description']
        listing.last_updated = listing_d['lastUpdateDate']
        listing.images_count = listing_d['totalImages']
        listing.views = listing_d['listingViews']

        facilities_arr = []
        for facility in listing_d['facilities']:
            facility_sttm = select(Facility).\
                where(Facility.name == facility.title()).\
                where(Facility.category == 'facilities')
            facility_obj = session.exec(facility_sttm).first()

            if(not facility_obj):
                facility_obj = Facility(
                    name=facility.title(),
                    category='facilities'
                )
            facilities_arr.append(facility_obj)

        for facility in listing_d['propertyOverview']:
            facility_sttm = select(Facility).\
                where(Facility.name == facility.title()).\
                where(Facility.category == 'overview')
            facility_obj = session.exec(facility_sttm).first()

            if(not facility_obj):
                facility_obj = Facility(
                    name=facility.title(),
                    category='overview'
                )
            facilities_arr.append(facility_obj)
        listing.facilities = facilities_arr

        listing.images = [Image(url=x) for x in listing_d['images']]
        listing.routes = get_routes(listing)
        listing.places_nearby = get_places_nearby(listing)

        # Saving it
        session.add(listing)
        session.commit()


def give_it_a_try():
    ret_ = {}

    daft_search_results = get_daft_search_result()
    daft_result_list = daft_search_results['result_list']
    c = 0
    with Session(engine) as session:

        for daft_result in daft_result_list:
            statement = select(Listing).\
                where(Listing.source == 'daft').\
                where(Listing.url == daft_result['url']).\
                where(Listing.price == daft_result['monthly_price'])

            results = session.exec(statement).first()
            if results:
                continue
                pass  # Check telegram sent message
            else:
                print(daft_result['url'])
                details = get_daft_details(daft_result['url'])
                save_new_listing(daft_result, details)

            c += 1
            if c < 10:
                continue
            break
    return details
