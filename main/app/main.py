
from pathlib import Path
from typing import List
import asyncio
import requests

from fastapi import Depends, FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload, lazyload, subqueryload, raiseload
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import select

from models import (
    Song, SongRead, SongCreate, SongUpdate,
    Listing, ListingCreate, ListingRead, ListingReadWithRelations, ListingCreateWithRelations,ListingUpdate,
    Image, ImageCreate, ImageRead,
    Facility
)
# from database import async_session, get_session
from database import get_session
from backgroud import BackgroundRunner
from loop import give_it_a_try
from custom_logger import CustomizeLogger


# models.Base.metadata.create_all(bind=engine)
# Hopefully not needed with Alembic

config_path=Path(__file__).with_name("custom_logger.json")
def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    return app

app = create_app()
# app = FastAPI()
router = APIRouter(prefix='/api')
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/listing/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str, session: Session = Depends(get_session)):
    result = session.query(Listing).get(id)

    return templates.TemplateResponse("listing_item.html",
                                      {
                                          "request": request,
                                          "listing": result,
                                      })

@app.get("/listings/{page}", response_class=HTMLResponse)
async def read_item(request: Request, page: int, session: Session = Depends(get_session)):
    results = session.query(Listing).order_by(Listing.last_updated).offset(page*10).limit(page).all()

    return templates.TemplateResponse("listing_list.html",
                                      {
                                          "request": request,
                                          "listings": results,
                                      })


# @app.get("/test2/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse("project-detail.html",
#                                       {
#                                           "request": request,
#                                           "listing": Listing
#                                       })


runner = BackgroundRunner()


@app.on_event('startup')
async def app_startup():
    asyncio.create_task(runner.run_main())


@app.get("/runner/is_running", response_model=bool)
def runner_is_running():
    return runner.is_running


@app.put("/runner/is_running")
def runner_is_running_put(is_running: bool):
    runner.is_running = is_running
    return 'ok'


@app.get("/runner/value")
def runner_value():
    return runner.value


@app.get("/test", )
def test():
    try:
        response = requests.get('http://daft:8000/search_result')
        response.raise_for_status()
        # Additional code will only run if the request is successful
    except requests.exceptions.HTTPError as error:
        print(error)
    return response.json()


@app.get("/test_full", )
def test():
    return give_it_a_try()


@app.get("/songs", response_model=List[SongRead])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return songs


@app.post("/songs", response_model=SongRead)
def create_user(song: SongCreate, session: Session = Depends(get_session)):
    db_item = Song(**song.dict())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.patch("/songs/{song_id}", response_model=SongRead)
def update_song(song_id: int, song: SongUpdate, session: Session = Depends(get_session)):
    db_song = session.get(Song, song_id)
    if not db_song:
        raise HTTPException(status_code=404, detail="Song not found")
    song_data = song.dict(exclude_unset=True)
    for key, value in song_data.items():
        setattr(db_song, key, value)
    session.add(db_song)
    session.commit()
    session.refresh(db_song)
    return db_song


@app.get("/listings", response_model=List[ListingReadWithRelations])
def get_songs(session: Session = Depends(get_session)):
    result = session.query(Listing).options(subqueryload('*'))
    songs = result.all()
    # print(songs)
    return songs


@app.post("/listings", response_model=ListingRead)
def listings_post(listing: ListingReadWithRelations, session: Session = Depends(get_session)):
    db_item = Listing(**listing.dict())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@app.post("/listings/withRel", response_model=ListingReadWithRelations)
def listings_post(listing: ListingCreateWithRelations, session: Session = Depends(get_session)):
    db_item = Listing.from_orm(listing)
    facilities_db = []
    for facility in listing.facilities:
        facility_rec = session.query(Facility).where(
            Facility.name == facility.name).first()
        if(facility_rec is None):
            facility_rec = Facility(
                name=facility
            )
        facilities_db.append(facility_rec)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@app.patch("/listing/{id}", response_model=ListingRead)
def update_song(id: int, listing: ListingUpdate, session: Session = Depends(get_session)):
    db_listing = session.get(Listing, id)
    if not db_listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    listing_data = listing.dict(exclude_unset=True)
    for key, value in listing_data.items():
        setattr(db_listing, key, value)
    session.add(db_listing)
    session.commit()
    session.refresh(db_listing)
    return db_listing

@app.post("/images", response_model=ImageRead)
def listings_post(listing: ImageCreate, session: Session = Depends(get_session)):
    db_item = Image(**listing.dict())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
# @app.get("/listings", response_model=List[ListingReadWithRelations])
# async def get_listings(session: AsyncSession = Depends(get_session)):
#     # result = await session.execute(select(ListingWithRelationship, Image).join(Image))
#     result = await session.exec(select(Listing))
#     listings = result.scalars().all()
#     return listings


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
