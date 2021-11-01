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
    title: str = None
    seoTitle: str = None
    sections: List[str] = None
    featuredLevel: str = None
    lastUpdateDate: datetime.date = None
    price: str = None
    numBedrooms: str = None
    numBathrooms: str = None
    propertyType: str = None
    daftShortcode: str = None
    totalImages: int = None
    hasVideo: bool = None
    hasVirtualTour: bool = None
    hasBrochure: bool = None
    ber: str = None
    seoFriendlyPath: str = None
    category: str = None
    state: str = None
    premierPartner: bool = None
    description: str = None
    facilities: List[str] = None
    images: List[str] = None
    propertyOverview: dict = None
    listingViews: str = None

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