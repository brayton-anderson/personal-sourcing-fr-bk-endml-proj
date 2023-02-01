from typing import List, Optional
from pydantic import BaseModel


class ProfileBase(BaseModel):
    title: str
    body: str

class Profile(ProfileBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    applications : List[Profile] =[]
    class Config():
        orm_mode = True

class ShowProfile(BaseModel):
    title: str
    body:str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
