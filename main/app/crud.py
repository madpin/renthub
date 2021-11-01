from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models, schemas


async def get_user(db: AsyncSession, user_id: int):
    return await db.query(models.User).filter(models.User.id == user_id).first()


async def get_user_by_email(db: AsyncSession, email: str):
    return await db.query(models.User).filter(models.User.email == email).first()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    
    result = await db.execute(
        select(models.User).order_by(models.User.id).offset(skip).limit(limit)
        )
    
    return result.all()


def create_user(db: AsyncSession, user: schemas.UserCreate):
    fake_hashed_password = user.password
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    return db_user


# def get_listings(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Listing).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
