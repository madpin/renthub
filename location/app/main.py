import os
from pathlib import Path
from fastapi.logger import logger

from pydantic.errors import ExtraError
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import HTMLResponse


import here_public_transit_api
from here_public_transit_api.rest import ApiException

from herepy import (
    PlacesApi,
    GeocoderApi,
)

from custom_logger import CustomizeLogger
# from location.app.schemas import Point.

from points import indeed, bank_house
import schemas
from mappings.InterestPoints import get_interenst_points
from mappings.route import get_routes

config_path=Path(__file__).with_name("custom_logger.json")
def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    return app

app = create_app()
# app = FastAPI()


@app.post("/interest_places_nearby/", response_model=List[schemas.InterestPoint])
async def raw_route(location: schemas.Point = indeed, query: str = 'Grocery'):
    ret_ = get_interenst_points(location.lat, location.long, query)
    return ret_


@app.post("/route/", response_model=List[schemas.RouteSummary])
async def raw_route(from_point: schemas.Point = bank_house, to_point: schemas.Point = indeed):
    print('###### 1')
    ret_ = get_routes(from_point.lat,
                     from_point.long, to_point.lat, to_point.long)
    print('###### 2')
    print(ret_)
    return ret_


@app.post("/herepy/places")
async def raw_route2(from_point: schemas.Point = bank_house, query: str = 'Grocery'):

    places_api = PlacesApi(api_key=os.environ['HERE_API_KEY'])

    # fetches a list of places based on a query string and country code.
    response = places_api.search_in_country(
        coordinates=[from_point.lat,
                     from_point.long], query=query, country_code="IRL"
    )

    return response.as_dict()


@app.post("/herepy/route")
async def raw_route2(from_point: schemas.Point = bank_house, to_point: schemas.Point = indeed):
    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")
    configuration = here_public_transit_api.Configuration()
    configuration.api_key['apiKey'] = os.environ['HERE_API_KEY']

    api_instance = here_public_transit_api.RoutingApi(
        here_public_transit_api.ApiClient(configuration)
    )

    # response = routing_api.public_transport(
    #     waypoint_a=[from_point.lat, from_point.long],
    #     waypoint_b=[to_point.lat, to_point.long],
    #     combine_change=True,
    #     modes=[RouteMode.balanced, RouteMode.publicTransportTimeTable],
    # )
    # return response.as_dict()

    try:
        # Routes
        api_response = api_instance.get_routes(
            origin=f"{from_point.lat},{from_point.long}",
            destination=f"{to_point.lat},{to_point.long}",
            alternatives=5,
            pedestrian_max_distance=2000,  # meters
            pedestrian_speed=1,  # m/s
            _return=[
                "travelSummary",
            ],
        )
        print(api_response)
        return api_response
    except ApiException as e:
        logger.error(str(e))
        Response(status_code=501)


@app.post("/herepy/address")
async def raw_route2(address: str = '17 Leinster Square, Rathmines, Dublin'):

    geocoder_api = GeocoderApi(api_key=os.environ['HERE_API_KEY'])
    response = geocoder_api.free_form(address)
    return response.as_dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
