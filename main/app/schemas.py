from typing import List, Optional

from pydantic import BaseModel




class UserBase(BaseModel):
    email: str
    is_active: bool


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
