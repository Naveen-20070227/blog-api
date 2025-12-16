from pydantic import BaseModel
from typing import List, Optional


class Blogs(BaseModel):
    title: str
    body: str
    user_id: int

class Blog1(BaseModel):
    title:str
    body:str
    class Config:
        from_attributes = True

class User(BaseModel):
    name:str
    email:str
    password:str

class User_out(BaseModel):
    name:str
    email:str
    
    class Config:
        from_attributes = True

class Blogwithuser(Blog1):
    creator: User_out
    class Config:
        from_attributes = True

class Userwithblogs(User_out):
    blogs: List[Blog1] = []
    class Config:
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] | None = None




    