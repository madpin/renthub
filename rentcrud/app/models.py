from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(primary_key=True)


class SongCreate(SongBase):
    pass

class Increment(SQLModel, table=True):
    id: int = Field(primary_key=True)


class Listing(SQLModel, table=True):
    __tablename__ = 'listings'
    id: int = Field(primary_key=True)
    url: str

class ListingWithRelationship(Listing):
    images: List["Image"] = Relationship(back_populates="listing")


class Image(SQLModel, table=True):
    __tablename__ = 'images'
    id: int = Field(primary_key=True)
    url: str
    size_x: float
    size_y: float
    listing_id: Optional[int] = Field(default=None, foreign_key="listings.id")

class ImageWithRelationship(Image):
    listing: Optional[Listing] = Relationship(back_populates="images")
