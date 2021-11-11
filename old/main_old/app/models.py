from sqlalchemy import (
    Table, Column, ForeignKey,
    Boolean, Integer, String, Float, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date

from database import Base
from datetime import datetime

listings_facilities = Table(
    'listings_facilities',
    Base.metadata,
    Column('listing_id', ForeignKey('listings.id'), primary_key=True),
    Column('facility_id', ForeignKey('facilities.id'), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return "<User(id='%s', emails='%s', is_active='%s')>" % (
            self.id, self.email, self.is_active)

    # items = relationship("Item", back_populates="owner")


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)

    title = Column(String, index=True)
    url = Column(String)
    source = Column(String)

    address = Column(String)
    short_postal_code = Column(String)
    postal_code = Column(String)

    ber_code = Column(String(10))
    price = Column(Integer)

    rating_auto = Column(Integer)
    rating_user = Column(Integer)

    telegram_sent_at = Column(DateTime)

    images_count = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)

    notes = Column(String)
    images = relationship("Image", back_populates="listing")
    distances = relationship("ListingDistance", back_populates="listing")
    facilities = relationship(
        "Facility", secondary=listings_facilities, back_populates="listings")


class Facility(Base):
    __tablename__ = "facilities"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    name = Column(String)
    category = Column(String)
    notes = Column(String)
    facilities = relationship(
        "Listing", secondary=listings_facilities, back_populates="facilities")


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    url = Column(String)
    size_x = Column(Integer)
    size_y = Column(Integer)
    notes = Column(String)

    listing_id = Column(Integer, ForeignKey("listings.id"))

    image_tags = relationship("ImageTags", back_populates="image")
    listing = relationship("Listing", back_populates="images")


class ImageTags(Base):
    __tablename__ = "image_tags"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    notes = Column(String)

    image_id = Column(Integer, ForeignKey("images.id"))
    image = relationship("Image", back_populates="image_tags")


class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    is_active = Column(Boolean, default=True)

    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    notes = Column(String)
    distances = relationship("ListingDistance", back_populates="point")


class ListingDistance(Base):
    __tablename__ = "listing_distances"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    distance_km = Column(Float)

    listing_id = Column(Integer, ForeignKey("listings.id"))
    listing = relationship("Listing", back_populates="distances")

    point_id = Column(Integer, ForeignKey("points.id"))
    point = relationship("Point", back_populates="distances")
