from typing import List, Optional
import datetime

from pydantic import BaseModel


class SearchResultItem(BaseModel):
    url: str
    title: str
    monthly_price: float
    latitude: float
    longitude: float
    bedrooms: str = None
    bathrooms: str = None
    publish_date: datetime.datetime
    category: str = None
    featured_level: str = None
    sections: List[str]
    source_code: str


class SearchResultList(BaseModel):
    results_count: int
    search_rules: dict
    result_list: List[SearchResultItem]


class DaftListing(BaseModel):
    id: str = None
    hash_version: str = None
    title: str = None
    seo_title: str = None
    sections: List[str] = None
    featured_level: str = None
    last_updated: datetime.date = None
    price: str = None
    num_beds: str = None
    num_baths: str = None
    property_type: str = None
    shortcode: str = None
    images_count: int = None
    has_video: bool = None
    has_virtual_tour: bool = None
    has_brochure: bool = None
    ber: str = None
    seo_friendly_path: str = None
    category: str = None
    state: str = None
    premier_partner: bool = None
    description: str = None
    facilities: List[str] = None
    images: List[str] = None
    property_overview: dict = None
    listing_views: str = None

def DaftSeller(BaseModel):
    sellerId: int
    name: str
    phone: str
    alternativePhone: str
    phoneWhenToCall: str
    branch: str
    address: str
    standardLogo: str
    squareLogo: str
    backgroundColour: str
    licenceNumber: str
    sellerType: str
    showContactFor: bool