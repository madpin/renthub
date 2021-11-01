from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

import models as models
import crud as crud
import schemas as schemas
from database import async_session, get_session

# models.Base.metadata.create_all(bind=engine)
# Hopefully not needed with Alembic

app = FastAPI()




@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_session)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        await db.commit()
        return db_user
    except IntegrityError as ex:
        await db.rollback()
        raise ValueError("The city is already stored")

    # return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users


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
