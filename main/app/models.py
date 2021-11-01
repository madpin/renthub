from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base


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
    updated_at = Column(DateTime)
    is_active = Column(Boolean, default=True)

    title = Column(String, index=True)
    url = Column(String)
    source = Column(String)
    address = Column(String)
    short_postal_code = Column(String)
    postal_code = Column(String)

    pictures = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)

    images = relationship("Picture", back_populates="listing")
    distances = relationship("ListingDistance", back_populates="listing")


class Picture(Base):
    __tablename__ = "pictures"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    url = Column(String)
    size_x = Column(Integer)
    size_y = Column(Integer)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    listing = relationship("Listing", back_populates="images")

class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    distances = relationship("ListingDistance", back_populates="point")

class ListingDistance(Base):
    __tablename__ = "listing_distances"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    distance_km = Column(Float)

    listing_id = Column(Integer, ForeignKey("listings.id"))
    listing = relationship("Listing", back_populates="distances")

    point_id = Column(Integer, ForeignKey("points.id"))
    point = relationship("Point", back_populates="distances")




