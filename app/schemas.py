from pydantic import BaseModel, ConfigDict, EmailStr, Field, validator
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    model_config = ConfigDict(from_attributes=True) # cho phép Pydantic đọc dữ liệu từ các đối tượng không phải là dictionary vi du doi tuong sqlAlchemy

#users
class UserBase(BaseModel):
    email:EmailStr
    password: str
class UserCreate(UserBase):
    pass
class User(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None