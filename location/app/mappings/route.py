import os
from urllib import parse

import logging

from herepy import (
    PlacesApi,
    RoutingApi,
    RouteMode,
    GeocoderApi,
)

import schemas


def get_route_raw(routes_dict):
    logging.debug(routes_dict)

    response = routes_dict.get('response', {})
    logging.debug('response')
    logging.debug(response)

    routes = response.get('route', [])
    logging.debug('routes')
    logging.debug(routes)

    for route in routes:

        lines = route.get('publicTransportLine', [])
        public_transport_count = len(lines)
        summary = route.get('summary', {})

        legs = route.get('leg', [])
        logging.debug('legs')
        for leg in legs:

            if('maneuver' in leg):
                logging.debug('maneuver')
                yield {
                    'maneuvers': leg['maneuver'],
                    'public_transport_count': public_transport_count,
                    'total_distance': summary.get('distance', ''),
                    'total_time': summary.get('travelTime', ''),
                }

def parse_route_raw(route_details):

    maneuvers = route_details['maneuvers']
    route = schemas.RouteSummary(
        waking_distance=0,
        public_transport_count=route_details['public_transport_count'],
        total_distance=route_details['total_distance'],
        total_time=route_details['total_time'],
    )

    for maneuver in maneuvers:
        if(maneuver.get('_type', '') == 'PrivateTransportManeuverType'):

            route.waking_distance = \
                route.waking_distance + int(maneuver.get('length', '0'))
    return route

def get_routes(lat1, long1, lat2, long2):
    routing_api = RoutingApi(api_key=os.environ['HERE_API_KEY'])

    response = routing_api.public_transport(
        waypoint_a=[lat1, long1],
        waypoint_b=[lat2, long2],
        combine_change=True,
        modes=[RouteMode.balanced, RouteMode.publicTransportTimeTable],
    )
    response_dict = response.as_dict()
    ret_ = []
    for route in get_route_raw(response_dict):
        ret_.append(parse_route_raw(route))
    return ret_