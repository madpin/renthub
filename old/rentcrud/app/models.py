from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(primary_key=True)
class SongRead(SongBase):
    id: int


class SongCreate(SongBase):
    pass

class Increment(SQLModel, table=True):
    id: int = Field(primary_key=True)


# #############################################################################
class ListingBase(SQLModel):
    url: str
    
class Listing(ListingBase, table=True):
    __tablename__ = 'listings'
    id: int = Field(primary_key=True)
    images: List["Image"] = Relationship(back_populates="listing", 
    sa_relationship_kwargs={'lazy': 'selectin'})
    
class ListingRead(ListingBase):
    id: str

# #############################################################################

class ImageBase(SQLModel):
    url: str
    size_x: float
    size_y: float
    listing_id: Optional[int] = Field(default=None, foreign_key="listings.id")

class Image(ImageBase, table=True):
    __tablename__ = 'images'
    id: int = Field(primary_key=True)
    listing: Optional[Listing] = Relationship(back_populates="images",
    sa_relationship_kwargs={'lazy': 'selectin'})

class ImageRead(ImageBase):
    id: int
class ImageReadWithListings(ImageRead):
    listing: Optional[Listing] = None

class ListingReadWithImages(ListingRead):
    images: List["ImageRead"] = []
