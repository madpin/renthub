import os
from pydantic.errors import ExtraError
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from points import indeed, bank_house

from herepy import (
    PlacesApi,
    RoutingApi,
    RouteMode,
    GeocoderApi,
)


import schemas

app = FastAPI()


@app.post("/test_places/")
async def raw_route(from_point: schemas.Point, to_point: schemas.Point):
    ret_ = {'test': True}
    return ret_


@app.post("/herepy/places")
async def raw_route2(from_point: schemas.Point = bank_house, query:str = 'Grocery'):

    places_api = PlacesApi(api_key=os.environ['HERE_API_KEY'])

    # fetches a list of places based on a query string and country code
    response = places_api.search_in_country(
        coordinates=[from_point.lat, from_point.long], query=query, country_code="IRL"
    )

    return response.as_dict()


@app.post("/herepy/route")
async def raw_route2(from_point: schemas.Point = bank_house, to_point: schemas.Point = indeed):

    routing_api = RoutingApi(api_key=os.environ['HERE_API_KEY'])
    response = routing_api.public_transport(
        waypoint_a=[from_point.lat, from_point.long],
        waypoint_b=[to_point.lat, to_point.long],
        combine_change=True,
        modes=[RouteMode.balanced, RouteMode.publicTransportTimeTable],
    )
    return response.as_dict()


@app.post("/herepy/address")
async def raw_route2(address: str = '17 Leinster Square, Rathmines, Dublin'):

    geocoder_api = GeocoderApi(api_key=os.environ['HERE_API_KEY'])
    response = geocoder_api.free_form(address)
    return response.as_dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
