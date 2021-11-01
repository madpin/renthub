import uvicorn
from fastapi import FastAPI

import schemas
from mappings.daft_listings import get_daft_search_result
from mappings.listing_details import get_listing_details

app = FastAPI()


@app.get("/search_result/", response_model=schemas.SearchResultList)
async def search_result():
    result = await get_daft_search_result()
    return result


@app.get("/listing_details/", response_model=schemas.DaftListing)
async def daft_listing(url):
    result = await get_listing_details(url)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
