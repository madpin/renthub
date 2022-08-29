import os
from urllib import parse

from fastapi.logger import logger


import here_public_transit_api
from here_public_transit_api.rest import ApiException

import schemas


# def get_route_raw(routes_dict):
#     logger.debug(routes_dict)

#     response = routes_dict.get('response', {})
#     logger.debug('response')
#     logger.debug(response)

#     routes = response.get('route', [])
#     logger.debug('routes')
#     logger.debug(routes)

#     for route in routes:

#         lines = route.get('publicTransportLine', [])
#         public_transport_count = len(lines)
#         summary = route.get('summary', {})

#         legs = route.get('leg', [])
#         logger.debug('legs')
#         for leg in legs:

#             if('maneuver' in leg):
#                 logger.debug('maneuver')
#                 yield {
#                     'maneuvers': leg['maneuver'],
#                     'public_transport_count': public_transport_count,
#                     'total_distance': summary.get('distance', ''),
#                     'total_time': summary.get('travelTime', ''),
#                 }


def parse_route_raw(route_details):

    #     maneuvers = route_details['maneuvers']
    route = schemas.RouteSummary(
        walking_distance=0,
        public_transport_count=0,
        total_distance=0,
        total_time=0,
    )

    for section in route_details["sections"]:
        distance = int(section.get("travelSummary", {}).get("length", 0))
        time = int(section.get("travelSummary", {}).get("length", 0))
        route.total_distance = route.total_distance + distance
        route.total_time = route.total_time + time
        if section.get("type", "") == "pedestrian":
            route.walking_distance = route.walking_distance + distance
        elif section.get("type", "") == "transit":
            route.public_transport_count = route.public_transport_count + 1
    return route




def get_routes(lat1, long1, lat2, long2):

    configuration = here_public_transit_api.Configuration()
    configuration.api_key['apiKey'] = os.environ['HERE_API_KEY']

    api_instance = here_public_transit_api.RoutingApi(
        here_public_transit_api.ApiClient(configuration)
    )

    try:
        # Routes
        api_response = api_instance.get_routes(
            origin="53.34347027177946,-6.276045630904159",
            destination="53.34545621516955,-6.231801040391591",
            alternatives=5,
            pedestrian_max_distance=2000,  # meters
            pedestrian_speed=1,  # m/s
            _return=[
                "travelSummary",
            ],
        )
        # pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutingApi->get_routes: %s\n" % e)
    response_dict = api_response.to_dict()
    ret_ = []
    for route in response_dict.get("routes", []):
        ret_.append(parse_route_raw(route))
    return ret_
