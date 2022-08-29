from fastapi.logger import logger

import schemas
from daftlistings import Daft, SearchType, SortType
from utils import str_to_float, get_attr_try

async def get_daft_search_result(location=None, min_price=None, max_price=None):

    if(location is None):
        location = "Dublin City"
    if(min_price is None):
        min_price = 1000
    if(max_price is None):
        max_price = 1800

    daft = Daft()
    logger.info(f"location: {location}, min_price: {min_price}, max_price:{max_price}")
    daft.set_location("Dublin City")
    daft.set_search_type(SearchType.RESIDENTIAL_RENT)
    daft.set_min_price(min_price)
    daft.set_max_price(max_price)

    daft.set_sort_type(SortType.PUBLISH_DATE_DESC)

    listings = daft.search()
    result_items = []
    for listing in listings:

        url=get_attr_try(listing, "daft_link")
        title=get_attr_try(listing, "title")
        latitude=get_attr_try(listing, "latitude")
        longitude=get_attr_try(listing, "longitude")
        bedrooms=get_attr_try(listing, "bedrooms")
        bathrooms=get_attr_try(listing, "bathrooms")
        publish_date=get_attr_try(listing, "publish_date")
        category=get_attr_try(listing, "category")
        featured_level=get_attr_try(listing, "featured_level")
        sections=get_attr_try(listing, "sections")
        source_code=get_attr_try(listing, "shortcode")
        monthly_price=str_to_float(get_attr_try(listing, "monthly_price")) or -1

        searchItem = schemas.SearchResultItem(                  
            url=url,
            title=title,
            monthly_price=monthly_price,
            latitude=latitude,
            longitude=longitude,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            publish_date=publish_date,
            category=category,
            featured_level=featured_level,
            sections=sections,
            source_code=source_code,
        )
        result_items.append(searchItem)

        result = schemas.SearchResultList(
            result_list=result_items,
            # results_count=daft._total_results,
            # search_rules=daft._make_payload()
            results_count=daft._total_results,
            search_rules={}
        )
    return result
