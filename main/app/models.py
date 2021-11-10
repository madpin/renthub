from typing import Optional, List
import sqlalchemy
from sqlmodel import SQLModel, Field, Relationship
from datetime import date, datetime


# #############################################################################
# Links
class ListingFacilityLink(SQLModel, table=True):
    listing_id: Optional[int] = Field(
        default=None, foreign_key="listings.id", primary_key=True
    )
    facility_id: Optional[int] = Field(
        default=None, foreign_key="facilities.id", primary_key=True
    )


# #############################################################################


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: Optional[int] = Field(primary_key=True)
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
    is_active: bool
    title: Optional[str] = None
    url: str
    source: str
    address: str
    short_postal_code: Optional[str] = None
    postal_code: Optional[str] = None
    ber_code: Optional[str] = None
    price: Optional[int] = None
    rating_auto: Optional[int] = None
    rating_user: Optional[int] = None
    telegram_sent_at: Optional[datetime] = None
    images_count: Optional[int] = 0
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    notes: Optional[str] = None


class Listing(ListingBase, table=True):
    __tablename__ = 'listings'
    id: Optional[int] = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})
    images: List["Image"] = Relationship(
        back_populates="listing",
        # sa_relationship_kwargs={'lazy': 'joined'}
    )
    facilities: List["Facility"] = Relationship(link_model=ListingFacilityLink)


class ListingRead(ListingBase):
    id: str
    created_at: datetime
    updated_at: datetime


class ListingCreate(ListingBase):
    pass

# #############################################################################


class FacilityBase(SQLModel):
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
    url: str
    size_x: float
    size_y: float
    listing_id: Optional[int] = Field(default=None, foreign_key="listings.id")


class Image(ImageBase, table=True):
    __tablename__ = 'images'
    id: Optional[int] = Field(primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now(),
                                 sa_column_kwargs={'onupdate': datetime.now()})
    listing: Optional[Listing] = Relationship(back_populates="images",
                                              #   sa_relationship_kwargs={'lazy': 'selectin'}
                                              )


class ImageRead(ImageBase):
    id: int


class ImageCreate(ImageBase):
    pass

# #############################################################################


class ImageReadWithListings(ImageRead):
    listing: Optional[Listing] = None


class ListingReadWithRelations(ListingRead):
    images: List["ImageRead"] = []
    facilities: List["Facility"] = []
class ListingCreateWithRelations(ListingCreate):
    images: List["ImageCreate"] = []
    facilities: List["Facility"] = []
