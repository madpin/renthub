from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import select

from models import Song, Listing, Image, SongRead, ListingRead
# from database import async_session, get_session
from database import get_session
# from models import ImageWithRelationship, ListingWithRelationship,ListingReadWithImages
from models import ListingReadWithImages

# models.Base.metadata.create_all(bind=engine)
# Hopefully not needed with Alembic

app = FastAPI()




@app.get("/songs", response_model=List[SongRead])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return songs


@app.get("/listings", response_model=List[ListingReadWithImages])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Listing))
    # result = await session.execute(select(Listing).options(selectinload(Listing.images))) # Works!!!!
    # result = await session.execute(select(Listing, Image).where(Listing.id == Image.listing_id))
    # result = await session.execute(select(Listing).options(joinedload(Listing.images)) # Failed
    songs = result.scalars().all()
    return songs
# @app.get("/listings", response_model=List[ListingReadWithImages])
# async def get_listings(session: AsyncSession = Depends(get_session)):
#     # result = await session.execute(select(ListingWithRelationship, Image).join(Image))
#     result = await session.exec(select(Listing))
#     listings = result.scalars().all()
#     return listings

@app.get("/listings2", response_model=List[ListingRead])
async def get_listings2(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Listing))
    listings = result.scalars().all()
    return listings

# @app.get("/images", response_model=List[ImageWithRelationship])
# async def get_images(session: AsyncSession = Depends(get_session)):
#     result = await session.execute(select(ImageWithRelationship))
#     listings = result.scalars().all()
#     return listings

# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################
# ################################################################################
# @app.post("/users/", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_session)):
#     db_user = await crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     try:
#         result = crud.create_user(db=db, user=user)
#         await db.commit()
#     except IntegrityError as ex:
#         await db.rollback()
#         raise ValueError("The city is already stored")

#     return result


# @app.get("/users/", response_model=List[schemas.User])
# async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
#     users = await crud.get_users(db, skip=skip, limit=limit)
#     return users

# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: AsyncSession = Depends(get_session)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: AsyncSession = Depends(get_session)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/listings/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
#     items = crud.get_listings(db, skip=skip, limit=limit)
#     return items
