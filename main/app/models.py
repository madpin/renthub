from typing import Optional, List
import sqlalchemy
from sqlmodel import SQLModel, Field, Relationship
from datetime import date, datetime


# #############################################################################
# Links
class ListingFacilityLink(SQLModel, table=True):
    listing_id: int = Field(
        foreign_key="listings.id", primary_key=True
    )
    facility_id: int = Field(
        foreign_key="facilities.id", primary_key=True
    )


# #############################################################################


class SongBase(SQLModel):
    id: Optional[int]
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})


class SongRead(SongBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SongUpdate(SQLModel):
    name: Optional[str] = None
    artist: Optional[str] = None
    year: Optional[int] = None


class SongCreate(SongBase):
    pass


class Increment(SQLModel, table=True):
    id: int = Field(primary_key=True)


# #############################################################################
class ListingBase(SQLModel):
    id: int = Field(primary_key=True)
    is_active: bool
    title: Optional[str] = None
    description: Optional[str] = None
    url: str
    source: str
    source_id: str
    source_code: Optional[str] = None
    address: str
    short_postal_code: Optional[str] = None
    property_type: Optional[str] = None
    postal_code: Optional[str] = None
    ber_code: Optional[str] = None
    views: Optional[int] = None

    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None

    price: Optional[int] = None
    rating_auto: Optional[int] = None
    rating_user: Optional[int] = None
    telegram_sent_at: Optional[datetime] = None
    images_count: Optional[int] = 0
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    notes: Optional[str] = None
    publish_date: Optional[datetime] = None
    last_updated: Optional[datetime] = None


class Listing(ListingBase, table=True):
    __tablename__ = 'listings'
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})
    images: List["Image"] = Relationship(back_populates="listing",
        # sa_relationship_kwargs={'lazy': 'joined'}
    )
    facilities: List["Facility"] = Relationship(link_model=ListingFacilityLink)
    places_nearby: List["PlaceNearby"] = Relationship(
        back_populates="listing",)
    routes: List["Route"] = Relationship(back_populates="listing",)


class ListingRead(ListingBase):
    id: str
    created_at: datetime
    updated_at: datetime


class ListingCreate(ListingBase):
    pass

# #############################################################################


class FacilityBase(SQLModel):
    id: Optional[int]
    name: str
    category: Optional[str] = None
    notes: Optional[str] = None


class Facility(FacilityBase, table=True):
    __tablename__ = 'facilities'
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})


class FacilityRead(FacilityBase):
    id: int
    created_at: datetime
    updated_at: datetime


class FacilityCreate(FacilityBase):
    pass


# #############################################################################


class ImageBase(SQLModel):
    id: Optional[int]
    url: str
    url_small: Optional[str]
    size_x: Optional[float]
    size_y: Optional[float]
    listing_id: Optional[int] = Field(default=None, foreign_key="listings.id")


class Image(ImageBase, table=True):
    __tablename__ = 'images'
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})
    listing: Optional[Listing] = Relationship(back_populates="images",
                                              #   sa_relationship_kwargs={'lazy': 'selectin'}
                                              )


class ImageRead(ImageBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ImageCreate(ImageBase):
    pass

# #############################################################################


class PlaceNearbyBase(SQLModel):
    id: Optional[int]
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    query: Optional[str] = None
    name: str
    address: str
    distance: int
    website: Optional[str] = None
    website_domain: Optional[str] = None
    chain_name: Optional[str] = None
    listing_id: Optional[int] = Field(default=None, foreign_key="listings.id")


class PlaceNearby(PlaceNearbyBase, table=True):
    __tablename__ = 'places_nearby'
    id: Optional[int] = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})
    listing: Optional[Listing] = Relationship(back_populates="places_nearby",)


class PlaceNearbyRead(PlaceNearbyBase):
    id: int
    created_at: datetime
    updated_at: datetime


class PlaceNearbyCreate(PlaceNearbyBase):
    pass

# #############################################################################


class InterestPointBase(SQLModel):
    id: Optional[int]
    name: str
    is_active: bool
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class InterestPoint(InterestPointBase, table=True):
    __tablename__ = 'interest_points'
    id: Optional[int] = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})


class InterestPointRead(InterestPointBase):
    id: int
    created_at: datetime
    updated_at: datetime


class InterestPointCreate(InterestPointBase):
    pass

# #############################################################################


class RouteBase(SQLModel):
    id: Optional[int]
    waking_distance: Optional[int] = 0
    total_distance: Optional[int] = 0
    total_time: Optional[int] = 0
    public_transport_count: Optional[int] = 0
    
    listing_id: Optional[int] = Field(default=None, foreign_key="listings.id")
    interest_point_id: Optional[int] = Field(
        default=None, foreign_key="interest_points.id")


class Route(RouteBase, table=True):
    __tablename__ = 'routes'
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(
        default=datetime.now(),
        sa_column_kwargs={'onupdate': datetime.now()})

    listing: Optional[Listing] = Relationship(back_populates="routes",)
    interest_point: Optional[InterestPoint] = Relationship()
    

class RouteRead(RouteBase):
    id: int
    created_at: datetime
    updated_at: datetime


class RouteCreate(RouteBase):
    id: Optional[int] = None


# #############################################################################


# #############################################################################


class ImageReadWithListings(ImageRead):
    listing: Optional[Listing] = None


class ListingReadWithRelations(ListingRead):
    images: List["ImageRead"] = []
    facilities: List["Facility"] = []
    places_nearby: List["PlaceNearby"] = []
    routes: List["Route"] = []

class ListingCreateWithRelations(ListingCreate):
    images: List["ImageCreate"] = []
    facilities: List["Facility"] = []