import logging
from pathlib import Path
from enum import Enum


import uvicorn
from fastapi import FastAPI

from custom_logger import CustomizeLogger
import schemas
from mappings.daft_listings import get_daft_search_result
from mappings.listing_details import get_listing_details

logger = logging.getLogger(__name__)

config_path=Path(__file__).with_name("custom_logger.json")

def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app



# app = create_app()
app = FastAPI()


@app.get("/search_result/", response_model=schemas.SearchResultList)
async def search_result():
    result = await get_daft_search_result()
    return result

class DaftMethodListing(str, Enum):
    json_details = "json_details"
    selenium = "selenium"

@app.get("/listing_details/", response_model=schemas.DaftListing)
async def daft_listing(url, method: DaftMethodListing):
    result = await get_listing_details(url)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
